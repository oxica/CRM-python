import io

from flask import (
    Flask,
    json,
    request,
    redirect,
    url_for,
    jsonify,
    render_template,
    flash,
    send_file,
)
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
            raise IncorrectInput(f"Переданное значение индекса не является целым числом")

    return inner


def get_rate_stat(developers):
    rates = []
    stat = {"mean": None, "min": None, "max": None, "item_number": 0, "total":0}
    
    for developer in developers:
        rate = developer.get_rate()
        if rate:
            rates.append(rate)
    
    if rates:
        stat.update(
            {
                "mean": statistics.mean(rates),
                "min": min(rates),
                "max": max(rates),
                "item_number": len(rates),
                "total": sum(rates)
            }
        )
    return stat


class DataField:
    field_description = "General"

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def to_json(self):
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
        return item in str(self.value)

    def __eq__(self, other):
        try:
            return float(other) == self.value
        except (ValueError, TypeError):
            return False

    def validate(self, value):
        try:
            self.value = float(value)
        except ValueError:
            raise IncorrectInput(f"value {value} can't be converted to float")


REGISTERED_FIELDS = {
    FirstNameField.field_description: FirstNameField,
    CityField.field_description: CityField,
    SkillField.field_description: SkillField,
    PhoneField.field_description: PhoneField,
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


class Developer:
    def __init__(self):
        self.fields = []
        self.phone = ""
        self.skill = ""
        self.city = ""

    def __len__(self):
        return len(self.fields)

    def __getitem__(self, key):
        return self.fields[key]

    def __iter__(self):
        return enumerate(self.fields)

    def to_json(self):
        return {"fields": [field.to_json() for field in self.fields]}

    def from_json(self, dict_developer):
        field_list = dict_developer["fields"]
        if field_list:
            for field_dict in field_list:
                field = field_decoder(field_dict)
                self.add(field)

    def get_rate(self):
        for field in self.fields:
            if field.field_description == "Rate":
                return field.value

    def get_phone(self):
        phones = []
        for field in self.fields:
            if field.field_description == "Phone":
                phones.append(field.value)
        return "; ".join(phones) if phones else ""

    def name(self):
        names = []
        surnames = []
        for field in self.fields:
            if field.field_description == "Name":
                names.append(field.value)
            if field.field_description == "Surname":
                surnames.append(field.value)

        name = " ".join(names) if names else ""
        surname = " ".join(surnames) if surnames else ""
        result = " ".join((name, surname))
        return result if result != " " else "No name"

    def get_skills(self):
        skills = []
        for field in self.fields:
            if field.field_description == "Skill":
                skills.append(field.value)
        return "; ".join(skills) if skills else ""

    def get_city(self):
        for field in self.fields:
            if field.field_description == "City":
                return field.value
        return ""

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
        return self.name()


class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def __getitem__(self, key):
        return self.developers[key]

    def dumps(self):
        developers = {rec_id: rec.to_json() for rec_id, rec in self.developers.items()}
        return json.dumps(developers)

    def loads(self, bytes_developers): #Достать из файла и сделать объектом
        self.developers.clear()
        self.last_developer_id = 0
        json_developers = json.loads(bytes_developers)
        for _, developer_list in json_developers.items():
            developer = Developer()
            developer.from_json(developer_list)
            self.add(developer)
            # self.developers[int(developer_id)] = developer
        # self.last_developer_id = max(self.developers.keys()) + 1

    def add(self, developer):  # Добавить элемент
        self.developers[self.last_developer_id] = developer
        developer_id = self.last_developer_id
        self.last_developer_id += 1
        return developer_id

    def replace(self, developer_id, developer):   #Заменить
        if developer_id not in self.developers:
            raise KeyError(f"developer {developer_id} not found")
        self.developers[developer_id] = developer

    @index_error_decorator
    def delete(self, developer_id):   #Удалить
        key = int(developer_id)
        self.developers.pop(key)

    def str_search(self, search_str: str):   #поиск строки
        result = {}
        for developer_id, developer in self.developers.items():
            if search_str in developer:
                result[developer_id] = developer
        return result

    def multiple_search(self, **search_items): # множественный поиск (убрать, т.к. указатели)
        result = {}
        for developer_id, developer in self.developers.items():
            if developer.multiple_search(**search_items):
                result[developer_id] = developer
        return result

    def clear(self):    #очистить
        self.developers.clear()
        self.last_developer_id = 0


app = Flask("answer")
AB = AddressBook()
# CORS(app)
with open("ab.json") as file:
    # developers = json.load(file)
    AB.loads(file.read())


@app.errorhandler(KeyError)
def handle_developer_not_found(_):
    return render_template("error.jinja", message="Запись не найдена")


@app.errorhandler(IndexError)
def handle_field_not_found(_):
    return render_template("error.jinja", message="Поле не найдено")


@app.errorhandler(IncorrectInput)
def handle_invalid_input(error):
    return render_template("error.jinja", message=str(error))


@app.errorhandler(FieldDecodeError)
def handle_invalid_format(error):
    return render_template("error.jinja", message=str(error))


@app.route("/")
def ab():
    return render_template(
        "developers.jinja", developers=AB.developers, stat_url=url_for("search_stat")
    )


@app.route("/dump")
def ab_dump():
    fh = io.BytesIO(AB.dumps().encode())
    return send_file(fh, attachment_filename="AB.json")


@app.route("/clear")
def ab_clear():
    AB.clear()
    return redirect(url_for("ab"))


@app.route("/load", methods=("GET", "POST"))
def ab_load():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        AB.loads(file.stream.read())
        return redirect(url_for("ab"))
    return render_template("load.jinja")


@app.route("/search", methods=("GET", "POST"))
def search():
    if request.method == "GET":
        return render_template("search.jinja", fields=REGISTERED_FIELDS.keys())

    if request.form["value"] != "":
        stat_url = url_for("search_stat", all=request.form["value"])
        search_result = AB.str_search(request.form["value"])
    else:
        fields = [field for field in request.form.to_dict(flat=False)["field"]]
        values = [value for value in request.form.to_dict(flat=False)["value"]]
        search_query = {
            field: value for field, value in filter(lambda x: x[1], zip(fields, values))
        }
        print(search_query)
        stat_url = url_for("search_stat", **search_query)
        search_result = AB.multiple_search(**search_query)
    return render_template("developers.jinja", developers=search_result, stat_url=stat_url)


@app.route("/search/stat")
def search_stat():
    search_query = request.args.to_dict()
    if search_query:
        if "all" in search_query:
            search_result = AB.str_search(search_query["all"])
        else:
            search_result = AB.multiple_search(**search_query)
        print(search_query, search_result)
        search_statistics = get_rate_stat(search_result.values())
    else:
        search_statistics = get_rate_stat(AB.developers.values())
    return render_template(
        "statistics.jinja", statistics=search_statistics, search=search_query
    )


@app.route("/ab/developer", methods=("GET", "POST"))
def new_developer():
    developer = Developer()
    developer_id = AB.add(developer)
    return redirect(url_for(endpoint="developer", developer_id=developer_id))


@app.route("/ab/developer/<int:developer_id>/delete")
def delete_developer(developer_id):
    AB.delete(developer_id)
    return redirect(url_for(endpoint="ab", developer_id=developer_id))


@app.route("/ab/developer/<int:developer_id>", methods=("GET", "POST"))
def developer(developer_id):
    current_developer = AB[developer_id]
    if request.method == "POST":
        if "idx" in request.form:
            idxs = [int(idx) for idx in request.form.to_dict(flat=False)["idx"]]
            types = [f_type for f_type in request.form.to_dict(flat=False)["type"]]
            values = [value for value in request.form.to_dict(flat=False)["value"]]
            for idx, f_type, value in zip(idxs, types, values):
                current_developer.update(idx, value)
        else:
            field_class = REGISTERED_FIELDS[request.form["type"]]
            field = field_class(request.form["value"])
            current_developer.add(field)

    return render_template(
        "developer.jinja",
        developer=current_developer,
        developer_id=developer_id,
        fields=REGISTERED_FIELDS.keys(),
    )


@app.route("/ab/developer/<int:developer_id>/field/<int:field_index>/delete")
def delete_field(developer_id, field_index):
    current_developer = AB[developer_id]
    current_developer.delete(field_index)
    return redirect(url_for("developer", developer_id=developer_id))


def main():
    from werkzeug.serving import run_simple

    run_simple("0.0.0.0", 5050, app)
    # BEGIN SOLUTION
    # app.run(host="0.0.0.0", port=8080)
    # END SOLUTION


if __name__ == "__main__":
    main()
