#1day
print("Hello, World. I have startup!")

#--------------------------

str1 = 'Hello, World.'
str2 = 'I have startup!'
result = str1 + ' ' + str2

#--------------------------

my_int = 50
my_float = 33.33

#--------------------------

price1 =50000
price_limit1 = 100000
decision1 = price1 < price_limit1

price2 =100001
price_limit2 = 100000
decision2 = price2 < price_limit2

wanted_price = 100000
price = 100000
guaranteed_deal = (wanted_price == price)

#--------------------------

rate = 800

if rate < 1000:
    qualification = 'junior'

if rate>=1000:
    qualification = 'middle&senior'

#--------------------------

rate = 1800

if rate < 1000: 
    qualification = 'junior'    
if rate >= 1000 and rate <= 2200:  
    qualification = 'middle'
    
if rate > 2200:
    qualification = 'senior'

#--------------------------

name = "Max"
rate = 999
my_qualification = "junior"

if rate <1000:
  qualification = "junior"
  
if rate >=1000 and rate <=2200:
  qualification = "junior"
  
if rate >1000:
  qualification = "senior"

answer = "My name is "+name+"! I am the "+qualification+" developer."
print(answer)

#--------------------------

sum = 0
for i in range(11):
  sum=sum+i  

print(sum)

#--------------------------

string = ''
for i in range(11):
    string = string + str(i) + ' '

print(string)

#--------------------------

rate_list = [600, 800, 1800, 2500, 3300]

developer_number = len(rate_list)


#--------------------------

slogan = ['We','are','team']
string = ''
for elem in slogan:
  string = string + elem + ' '

print(string)

#--------------------------15

developer_rates = [600, 800, 1800, 2500, 3300]

sum = 0
for developer_rate in developer_rates:
  sum+=developer_rate
    
print(sum)

#--------------------------16

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
result = []
for day in month:
  if not day%2:
    result.append(day)

print(result)

#--------------------------

developer_rates = [600, 800, 1800, 2500, 3300]

total_juniors = 0

for rate in developer_rates:
    if rate < 1000:
        total_juniors +=rate

#--------------------------

developer_rates = [600, 800, 1800, 2500, 3300]
min_rate = min(developer_rates)
max_rate = max(developer_rates)

#--------------------------

rates = [600, 800, 1800, 2500]

rates_min = min(rates) 
rates_max = max(rates)   

mean = sum(rates)/len(rates)
item_number = len(rates)
total = sum(rates)

#--------------------------

rates = [600, 800, 1800, 2500]
stat = {"mean": None, "min": None, "max": None, "item_number": 0, "total": 0}


stat["mean"] = sum(rates)/len(rates)    
stat["min"] = min(rates)
stat["max"] = max(rates)
stat["item_number"] = len(rates)
stat["total"] = sum(rates)

#--------------------------

developer = {
    'Name': 'Peter',
    'City': 'Kyiv',
    'Skill': 'Python',
    'Phone': '+380631234567',
    'Rate': 1800
}

name = developer['Name']
rate = developer['Rate']

#--------------------------

developer1 = {'Name': 'Vlad',  "City": "Kyiv", "Skill": "Python", "Rate": 1300, 'Phone': '+380631234570'}
developer2 = {'Name': 'Max',   "City": "Lviv", "Skill": "Python", "Rate": 1200, 'Phone': '+380631234571'}
developer3 = {'Name': 'Ivan',  "City": "Kyiv", "Skill": "Python", "Rate": 2800, 'Phone': '+380631234572'}
developer4 = {'Name': 'Anton',  "City": "Kyiv", "Skill": "Python", "Rate": 3800, 'Phone': '+380631234573'}
developer5 = {'Name': 'Alex',  "City": "Lviv", "Skill": "Python", "Rate": 4800, 'Phone': '+380631234574'}

developers = [developer1, developer2, developer3, developer4, developer5]

sum_1_3_5 = developers[0]["Rate"]+developers[2]["Rate"]+developers[4]["Rate"]
tel_5 = developers[4]['Phone']

#--------------------------

def plus(new_team,old_team):
    s=new_team+old_team
    return s

def minus(new_team,old_team):
    m=new_team-old_team
    return m

sum = plus(8900,4200)
different = minus(8900,4200)

#--------------------------

developer1 = {'Name': 'Kseniya',  'City': 'Odessa', 'Skill': 'Python', 'Rate': 600,'Phone': '+380631234573'}
developer2 = {'Name': 'Peter','City': 'Kyiv','Skill': 'Python','Rate': 1800,'Phone': '+380631234567'}
developer3 = {'Name': 'Vlad',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1300, 'Phone': '+380631234570'}
developer4 = {'Name': 'Ivan',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 2800, 'Phone': '+380631234572'}
developer5 = {'Name': 'Alex',  'City': 'Lviv', 'Skill': 'Python', 'Rate': 4800, 'Phone': '+380631234574'}

developers_list = [developer1, developer2, developer3, developer4, developer5]


def get_rates(developers):
    developer_rates = []
    for developer in developers:
      developer_rates.append(developer['Rate'])

    return developer_rates

#--------------------------

developer1 = {
'Name': 'Kseniya',  'City': 'Odessa', 'Skill': 'Python', 'Rate': 600,'Phone': '+380631234573'}
developer2 = {'Name':'Peter','City': 'Kyiv','Skill': 'Python','Rate': 1800,'Phone': '+380631234567'}
developer3 = {'Name': 'Vlad',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1300, 'Phone': '+380631234570'}
developer4 = {'Name': 'Ivan',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 2800, 'Phone': '+380631234572'}
developer5 = {'Name': 'Alex',  'City': 'Lviv', 'Skill': 'Python', 'Rate': 4800, 'Phone': '+380631234574'}

devs = [developer1, developer2, developer3, developer4, developer5]


def get_rate_stat(developers):
    rates = []
    stat = {"mean": None, "min": None, "max": None, "item_number": 0}
    
    for developer in developers:
        rate = developer["Rate"]
        rates.append(rate)

    stat.update(
      {
        "mean":sum(rates)/len(rates),
        "min":min(rates),
        "max":max(rates),
        "item_number":len(rates) 
  }
)
    return stat

#2day

class Developer:
  skill="Python"
  rate=1100

#------------

class Developer: 
    skill = "python"
    rate = 1100 
developer1 = Developer()
developer2 = Developer()
developer3 = Developer()

#------------

class Developer: 
    skill = "python"
    rate = 1100 

developer1 = Developer()
developer2 = Developer()
developer3 = Developer()

developer1.rate = 1300

total_rate = developer1.rate + developer2.rate + developer3.rate
print(total_rate)

#---------

class Developer:
  def __init__(self):
    self.skill = "Python"
    self.rate = 1000
developer1 = Developer()

#-------

class Developer:
    def __init__(self,name,phone):
      self.city = "Kyiv"
      self.skill = "Python"
      self.rate = 1300
      self.name = name
      self.phone = phone

user = Developer('Vlad','+380631234570')

#------

class Developer:
    def __init__(self,name,phone):
        self.name = name
        self.city = 'Kyiv'
        self.skill = 'Python'
        self.rate = 1300
        self.phone = phone

user = Developer('Vlad','+380631234570')

out = f"{user.name} {user.city} {user.skill} {user.rate} {user.phone}"

#-------

class Developer:
    def __init__(self,name,city,skill,rate,phone):
        self.name = name
        self.city = city
        self.skill = skill
        self.rate = rate
        self.phone = phone

    def __str__(self):
      return f"{user.name} {user.city} {user.skill} {user.rate} {user.phone}"


user = Developer('Vlad','Kyiv',"Python",'1300','+380631234570')

#-------

class Developer:
    def __init__(self): 
        self.fields = [] 


developer = Developer()

developer.fields.append('name')
developer.fields.append('city')
developer.fields.append('developer_skill')
developer.fields.append('rate')
developer.fields.append('phone')

developer.fields[2] = "skill"

developer.fields.pop(4)
developer.fields.pop(3)

out = f"{developer.fields[0]} {developer.fields[1]} {developer.fields[2]}" 
#-------

class Developer:
    def __init__(self):
        self.fields = []

    def __contains__(self, item: str):
      for field in self.fields:
        if item in field:
          return True
      return False

#------

class Developer:
    def __init__(self):
        self.fields = []
    def add(self, field_item):
      self.fields.append(field_item)

#----

class Developer:
    def __init__(self):
        self.fields = []

    def add(self, field_item):
        self.fields.append(field_item)  

    def delete(self, idx):
        self.fields.pop(idx)

#-------

class Developer:
    def __init__(self):
        self.fields = ['name','city','email']

    def add(self, field_item):
        self.fields.append(field_item)  

    def delete(self, idx):
        idx = int(idx)
        self.fields.pop(idx)

    def update(self, idx, value):
        idx= int(idx)
        self.fields[idx] = value


#--13---

class DataField:
    field_description = 'General'
    def __init__(self, value):
      self.value = value
    def __str__(self):
      return f"{self.field_description}:{self.value}"
      
class FirstNameField(DataField):
  field_description="Name"

#---14----

class DataField:
    field_description = "General"

class FirstNameField(DataField):   
    field_description = "Name"   

class CityField(DataField):   
    field_description = "City"
    
class SkillField(DataField):   
    field_description = "Skill" 
    
class RateField(DataField):   
    field_description = "Rate" 
    
class PhoneField(DataField):   
    field_description = "Phone" 

#--15---

out = ''
value = 'f' 
try:
    value = float(value)
except ValueError:
  out = f"value {value} can't be converted to float"
if out:
  print(out)

#---16--

def validate(value):
    try:
        out = float(value)
    except ValueError:
      out = None
    return out

#---17--

class IncorrectInput(Exception):
    pass


class RateField:
    field_description = "Rate"

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        try:
            self.value = float(value)
        except ValueError:
            raise IncorrectInput(f"value {value} can't be converted to float")

#-----

class Developer:
    def __init__(self):
        self.fields = []

    def add(self, field_item):
        self.fields.append(field_item)  

    def delete(self, idx):
        idx = int(idx)
        self.fields.pop(idx)

    def update(self, idx, value):
        idx = int(idx)
        self.fields[idx] = value

class DataField:
    field_description = "General"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}:{self.value}"

class FirstNameField(DataField):   
    field_description = "Name"   

class CityField(DataField):  
    field_description = "City"  

class SkillField(DataField): 
    field_description = "Skill" 

class PhoneField(DataField): 
    field_description = "Phone" 

class RateField(DataField): 
    field_description = "Rate" 


developer1 = Developer()
developer1.add(FirstNameField("Vlad"))
developer1.add(CityField("Kyiv"))
developer1.add(SkillField("Python"))
developer1.add(PhoneField("+3806312345670"))
developer1.add(RateField(1300))

developer2 = Developer()
developer2.add(FirstNameField("Max"))
developer2.add(CityField("Lviv"))
developer2.add(SkillField("Python"))
developer2.add(PhoneField("+3806312345671"))
developer2.add(RateField(1200))

developer3 = Developer()
developer3.add(FirstNameField("Ivan"))
developer3.add(CityField("Kyiv"))
developer3.add(SkillField("Python"))
developer3.add(PhoneField("+3806312345672"))
developer3.add(RateField(2800))

#3day

class AddressBook:
  def __init__(self):
    self.developers = {}
    self.last_developer_id = 0
    
ab = AddressBook()


#-----

class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
      self.developers[self.last_developer_id] = developer
      self.last_developer_id += 1

#-------

class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0


    def add(self, developer):
        self.developers[self.last_developer_id] = developer 
        self.last_developer_id += 1

    def delete(self,developer_id: int):
      key = int(developer_id)
      self.developers.pop(key)

#-----

class IncorrectInput(Exception):
    pass

class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
        self.developers[self.last_developer_id] = developer  
        self.last_developer_id += 1

    def delete(self, developer_id: int): 
        try:
          key = int(developer_id)
          self.developers.pop(key)
        except TypeError:
          raise IncorrectInput(f"Developer ID {developer_id} is not int")
        except KeyError:
          raise IncorrectInput(f"Developer {developer_id} not found")

#------

class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
        self.developers[self.last_developer_id] = developer  
        self.last_developer_id += 1

    def delete(self, developer_id: int):
        try:
            key = int(developer_id)
            self.developers.pop(key)  
        except TypeError:
            raise IncorrectInput(f"Developer ID {developer_id} is not int")
        except KeyError:
            raise IncorrectInput(f"Developer {developer_id} not found")

    def update_developer(self, developer_id, field_idx, value):
      developer = self.developers[developer_id]
      developer.update(field_idx, value)

#------

class IncorrectInput(Exception):
    pass

class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
        self.developers[self.last_developer_id] = developer  
        self.last_developer_id += 1

    def delete(self, developer_id: int):
        try:
            key = int(developer_id)
            self.developers.pop(key)  
        except TypeError:
            raise IncorrectInput(f"Developer ID {developer_id} is not int")
        except KeyError:
            raise IncorrectInput(f"Developer {developer_id} not found")

    def update_developer(self, developer_id, field_idx, value): 
        developer = self.developers[developer_id]
        developer.update(field_idx, value)

    def clear_developer(self):
        self.developers.clear()
        self.last_developer_id = 0

#-------

import json

class AddressBook:
    def __init__(self):
        self.developers = {}

    def add(self, developer):
        self.developers[self.last_developer_id] = developer  
        self.last_developer_id += 1

    def delete(self, developer_id: int):
        try:
            key = int(developer_id)
            self.developers.pop(key)  
        except TypeError:
            raise IncorrectInput(f"Developer ID {developer_id} is not int")
        except KeyError:
            raise IncorrectInput(f"Developer {developer_id} not found")

    def update_developer(self, developer_id, field_idx, value): 
        developer = self.developers[developer_id]
        developer.update(field_idx, value)

    def clear(self):    
        self.developers.clear()
        self.last_developer_id = 0

    def dumps(self):
        return json.dumps(self.developers)   

#-----

import json


class IncorrectInput(Exception):
    pass


class AddressBook:
    def __init__(self):
        self.developers = {}

    def add(self, developer):
        self.developers[self.last_developer_id] = developer  
        self.last_developer_id += 1

    def delete(self, developer_id: int):
        try:
            key = int(developer_id)
            self.developers.pop(key)  
        except TypeError:
            raise IncorrectInput(f"Developer ID {developer_id} is not int")
        except KeyError:
            raise IncorrectInput(f"Developer {developer_id} not found")

    def update_developer(self, developer_id, field_idx, value): 
        developer = self.developers[developer_id]
        developer.update(field_idx, value)

    def clear(self):    
        self.developers.clear()
        self.last_developer_id = 0

    def dumps(self):
        return json.dumps(self.developers)  

    def loads(self,json_bytes):
      self.developers=json.loads(json_bytes)

#------

import json
lst = []

lst.append(5)
lst.append(6)
lst.append(7)
lst.append(8)


jsn = json.dumps(lst)

#-----

import json

jsn = '["name", "city", "skill", "rate", "phone"]'
obj = json.loads(jsn)

#-----

import json

developer1 = {'name': 'Max', 'rate': 1500 }
developer2 = {'name': 'Vlad', 'rate': 2300 }
developer3 = {'name': 'Ivan', 'rate': 2700 }

developer_list = [developer1, developer2, developer3]

jsn = json.dumps(developer_list)

#-----

import json

developer = {
    'Name': 'Serhii',
    'City': 'Kyiv',
    'Skill': 'Python',
    'Phone': '+380631234567',
    'Rate': 1700
}

developer['Rate'] = 2000

jsn = json.dumps(developer)

#-----

import json

jsn ='''{
"0": {"fields": [
    {"value": "Vlad", "field_name": "Name"}, 
    {"value": 1300, "field_name": "Rate"}]}, 
"1": {"fields": [
    {"value": "Max", "field_name": "Name"}, 
    {"value": 1200, "field_name": "Rate"}]}, 
"2": {"fields": [
    {"value": "Ivan", "field_name": "Name"}, 
    {"value": 2800, "field_name": "Rate"}]}
}''' 

elem = json.loads(jsn)

name_3 = elem["2"]["fields"][0]["value"]
rate_1_2_3 = elem['0']['fields'][1]['value'] + elem['1']['fields'][1]['value'] + elem['2']['fields'][1]['value']

#----

import json
class DataField:
    field_description = "General"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}:{self.value}"

class FirstNameField(DataField):   
    field_description = "Name"  

jsn ='{"value": "Ivan", "field_name": "Name"}'

elem = json.loads(jsn)

key = elem["field_name"]
val = elem["value"]

obj = FirstNameField(val)

#-----

class DataField:
    field_description = "General"
    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}: {self.value}"

class FirstNameField(DataField):
    field_description = "Name"

class RateField(DataField):
    field_description = "Rate"


REGISTERED_FIELDS = {
    FirstNameField.field_description: FirstNameField,
    RateField.field_description: RateField
    }

def field_decoder(json_in):
    name = json_in["field_name"] 
    value = json_in["value"] 

    base_class = REGISTERED_FIELDS[name] 
    field = base_class(value)
    return field 
  

#-----

from flask import Flask

app = Flask("start")


@app.route("/hello")
def fields():
    response = 'Hello, World! I have startup!'
    return response


if __name__ == '__main__':
    app.run()

#-----

from flask import Flask, jsonify

FIELDS = ["Name", "City", "Skill", "Rate", "Phone"]

app = Flask("answer")

@app.route("/fields")
def fields():
    response =jsonify(FIELDS)
    return response

#-----

from flask import Flask, jsonify

developer = {"Name": "Peter", "Rate": "1800"}

app = Flask("developer")


@app.route("/developer")
def developer_out():
    response = jsonify(developer)  
    return response

#-----



#-----

from flask import Flask, request, jsonify

app = Flask("answer")

@app.route("/ab/search")
def search():
    search_query = request.args.to_dict()
    response_name = request.args["Name"]
    response_rate =request.args['Rate']
    response = "{'Name':'"+response_name+",'Rate':'"+ response_rate+"'}"
    return jsonify(response)

#----

from flask import Flask, request

app = Flask("answer")

@app.route("/ab/developer/<developer_id>/field", methods=["POST"])
def new_field(developer_id):
    field_name = request.json["name"]
    return f"Name {field_name}, developer: {developer_id}"

#-----

from flask import Flask, request, jsonify


class AddressBook:
    def __init__(self):
        self.developers = {}
        self.last_developer_id = 0

    def add(self, developer):
        self.developers[self.last_developer_id] = developer
        self.last_developer_id += 1

    def str_search(self, search_str: str):
        result = {}
        for developer_id, developer in self.developers.items():
            if search_str in developer:
                result[developer_id] = developer
        return result

    def multiple_search(self, **search_items):
        result = {}
        for developer_id, developer in self.developers.items():
            if developer.multiple_search(**search_items):
                result[developer_id] = developer
        return result


AB = AddressBook()
app = Flask("answer")


@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(message=str(e))


@app.route("/ab/search")
def search():
    search_query = request.args.to_dict()
    search_result = {}
    if "all" in search_query:
        search_result = AB.str_search(search_query["all"])  
    else:
        search_result = AB.multiple_search(**search_query)
    search_result_dict = {}
   
    for key, rec in search_result.items():
        search_result_dict[str(key)] = rec.to_dict()
    response = jsonify(**search_result_dict)
    return response