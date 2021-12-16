from flask import Flask, json, request, redirect, url_for, jsonify
import re
import json
import statistics


class IncorrectInput(Exception):
    pass


class FieldDecodeError(Exception):
    pass


def index_error_decorator(function):
    def inner(*args):
        try:
            result = function(*args)
            return result
        except ValueError:
            raise IncorrectInput(f"Передане значення індексу не є цілим числом")

    return inner


def get_rate_stat(records):
    rates = []
    stat = {"mean": None, "min": None, "max": None, "item_number": 0}
    for record in records:
        rate = record.get_rate()
        if rate:
            rates.append(rate)
    if rates:
        stat.update(
            {
                "mean": statistics.mean(rates),
                "min": min(rates),
                "max": max(rates),
                "item_number": len(rates),
            }
        )
    return stat


class DataField:
    field_description = "General"

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def to_dict(self):
        return {"value": self.value, "field_name": self.field_description}

    def validate(self, value):
        self.value = value

    def __contains__(self, item):
        return item in self.value

    def __str__(self):
        return f"{self.field_description}: {self.value}"


class FirstNameField(DataField):
    field_description = "Name"


class LastNameField(DataField):
    field_description = "Surname"


class OrganizationField(DataField):
    field_description = "Organization"


class CityField(DataField):
    field_description = "City"


class SkillField(DataField):
    field_description = "Skill"


class PhoneField(DataField):
    field_description = "Phone"
    PHONE_REGEX = re.compile(r"^\+?(\d{2})?\(?(0\d{2})\)?(\d{7}$)")

    def __init__(self, value):
        self.country_code: str = ""
        self.operator_code: str = ""
        self.phone_number: str = ""
        super().__init__(value)

    def validate(self, value: str):
        value = value.replace(" ", "")
        search = re.search(self.PHONE_REGEX, value)
        try:
            country, operator, phone = search.group(1, 2, 3)
        except AttributeError:
            raise IncorrectInput(f"No phone number found in {value}")

        if operator is None:
            raise IncorrectInput(f"Operator code not found in {value}")

        self.country_code = country if country is not None else "38"
        self.operator_code = operator
        self.phone_number = phone
        self.value = f"+{self.country_code}{self.operator_code}{self.phone_number}"


class EmailField(DataField):
    field_description = "Email"
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def validate(self, value: str):
        if not self.EMAIL_REGEX.match(value):
            raise IncorrectInput(f"{value} is not an email.")
        self.value = value


class RateField(DataField):
    field_description = "Rate"

    def __contains__(self, item):
        try:
            return float(item) == self.value
        except (ValueError, TypeError):
            return False

    def validate(self, value):
        try:
            self.value = float(value)
        except ValueError:
            raise IncorrectInput(f"value {value} can't be converted to float")


REGISTERED_FIELDS = {
    DataField.field_description: DataField,
    FirstNameField.field_description: FirstNameField,
    LastNameField.field_description: LastNameField,
    OrganizationField.field_description: OrganizationField,
    CityField.field_description: CityField,
    SkillField.field_description: SkillField,
    PhoneField.field_description: PhoneField,
    EmailField.field_description: EmailField,
    RateField.field_description: RateField,
}


def field_decoder(field_dict):
    try:
        field_class = REGISTERED_FIELDS[field_dict["field_name"]]
        field = field_class(field_dict["value"])
    except KeyError:
        raise FieldDecodeError(
            "Wrong message format. 'field_name' and 'value' required"
        )
    return field


class Record:
    def __init__(self):
        self.fields = []

    def __len__(self):
        return len(self.fields)

    def __getitem__(self, key):
        return self.fields[key]

    def to_dict(self):
        return [field.to_dict() for field in self.fields]

    def from_json(self, field_list):
        if field_list:
            for field_dict in field_list:
                field = field_decoder(field_dict)
                self.add(field)

    def get_rate(self):
        for field in self.fields:
            if field.field_description == "Rate":
                return field.value

    def add(self, field_item):
        self.fields.append(field_item)
        return self.fields.index(field_item)

    @index_error_decorator
    def replace(self, index, field_item):
        self.fields[index] = field_item

    @index_error_decorator
    def delete(self, idx):
        idx = int(idx)
        self.fields.pop(idx)

    @index_error_decorator
    def update(self, field_idx, value):
        field_idx = int(field_idx)
        field = self.fields[field_idx]
        field.validate(value)

    def field_search(self, field_name, search_value):
        for field in self.fields:
            if field.field_description == field_name:
                return search_value in field
        return False

    def multiple_search(self, **search_items):
        for field_name, search_value in search_items.items():
            current_search = self.field_search(field_name, search_value)
            if not current_search:
                return False
        return True

    def __contains__(self, item: str):
        for field in self.fields:
            if item in field:
                return True
        return False

    def __str__(self) -> str:
        result_str = "\n"
        for idx, field in enumerate(self.fields):
            result_str += f"{idx}.: {str(field)}\n"
        return result_str


class AddressBook:
    def __init__(self):
        self.records = {}
        self.last_record_id = 0

    def __getitem__(self, key):
        return self.records[key]

    def dumps(self):
        records = {rec_id: rec.to_dict() for rec_id, rec in self.records.items()}
        return json.dumps(records)

    def loads(self, json_records):
        self.records.clear()
        for record_id, record_list in json_records.items():
            record = Record()
            record.from_json(record_list)
            self.records[int(record_id)] = record
        self.last_record_id = max(self.records.keys()) + 1

    def add(self, record):
        self.records[self.last_record_id] = record
        record_id = self.last_record_id
        self.last_record_id += 1
        return record_id

    def replace(self, record_id, record):
        if record_id not in self.records:
            raise KeyError(f"Record {record_id} not found")
        self.records[record_id] = record

    @index_error_decorator
    def delete(self, record_id):
        key = int(record_id)
        self.records.pop(key)

    def str_search(self, search_str: str):
        result = {}
        for record_id, record in self.records.items():
            if search_str in record:
                result[record_id] = record
        return result

    def multiple_search(self, **search_items):
        result = {}
        for record_id, record in self.records.items():
            if record.multiple_search(**search_items):
                result[record_id] = record
        return result


app = Flask("answer")
AB = AddressBook()


@app.errorhandler(KeyError)
def handle_record_not_found(_):
    response = jsonify({"message": "Record not found"})
    response.status_code = 404
    return response


@app.errorhandler(IndexError)
def handle_field_not_found(_):
    response = jsonify({"message": "Field not found"})
    response.status_code = 404
    return response


@app.errorhandler(IncorrectInput)
def handle_invalid_input(error):
    response = jsonify({"message": str(error)})
    response.status_code = 422
    return response


@app.errorhandler(FieldDecodeError)
def handle_invalid_format(error):
    response = jsonify({"message": str(error)})
    response.status_code = 422
    return response


@app.route("/ab", methods=["GET", "POST"])
def ab():
    if request.method == "POST":
        AB.loads(request.json)

    response = app.response_class(response=AB.dumps(), mimetype="application/json")
    return response


@app.route("/ab/stat")
def stat():
    ab_statistics = get_rate_stat(AB.records.values())
    response = jsonify(**ab_statistics)
    return response


@app.route("/ab/search")
def search():
    search_query = request.args.to_dict()
    if "all" in search_query:
        search_result = AB.str_search(search_query["all"])
    else:
        search_result = AB.multiple_search(**search_query)
    response = jsonify(
        **{str(key): rec.to_dict() for key, rec in search_result.items()}
    )
    return response


@app.route("/ab/search/stat")
def search_stat():
    search_query = request.args.to_dict()
    if "all" in search_query:
        search_result = AB.str_search(search_query["all"])
    else:
        search_result = AB.multiple_search(**search_query)
    search_statistics = get_rate_stat(search_result.values())
    response = jsonify(**search_statistics)
    return response


@app.route("/ab/record", methods=["POST"])
def new_record():
    record_dict = request.json
    record = Record()
    record.from_json(record_dict)
    record_id = AB.add(record)
    return redirect(url_for(endpoint="record", record_id=record_id))


@app.route("/ab/record/<int:record_id>", methods=["GET", "DELETE", "PUT"])
def record(record_id):
    if request.method == "DELETE":
        AB.delete(record_id)
        return {"status": "OK"}

    if request.method == "PUT":
        record_dict = request.json
        record = Record()
        record.from_json(record_dict)
        AB.replace(record_id, record)

    current_record = AB[record_id]
    response = app.response_class(
        response=json.dumps(current_record.to_dict()), mimetype="application/json"
    )
    return response


@app.route("/ab/record/<int:record_id>/field", methods=["POST"])
def new_field(record_id):
    current_record = AB[record_id]
    field = field_decoder(request.json)
    field_index = current_record.add(field)
    return redirect(url_for("field", record_id=record_id, field_index=field_index))


@app.route(
    "/ab/record/<int:record_id>/field/<int:field_index>",
    methods=["GET", "PUT", "DELETE", "PATCH"],
)
def field(record_id, field_index):
    current_record = AB[record_id]

    if request.method == "DELETE":
        current_record.delete()
        return {"status": "OK"}

    if request.method == "PUT":
        current_field = field_decoder(request.json)
        current_record.replace(field_index, current_field)

    current_field = current_record[field_index]
    if request.method == "PATCH":
        value = request.json["value"]
        current_field.validate(value)

    response = app.response_class(
        response=json.dumps(current_field.to_dict()), mimetype="application/json"
    )
    return response


@app.route("/fields", methods=["GET"])
def fields():
    response = app.response_class(
        response=json.dumps(list(REGISTERED_FIELDS.keys())), mimetype="application/json"
    )
    return response


def main():
    app.run (host="0.0.0.0",port=8080)


if __name__ == "__main__":
    main()