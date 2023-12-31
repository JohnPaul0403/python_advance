import json

json.dumps
json.dumps

json.load
json.loads

entero = 33

json_int = json.dumps(entero)

print(json_int)

py_int = json.loads(json_int)

print(py_int)

lista = [1,2,'tres',4]

json_list = json.dumps(lista)

print(type(json_list))

dicc = {
    'int' : 1,
    'str' : 'Hello World!',
    'list' : [1,2,3]
}

json_dict = json.dumps(dicc)

with open("archivo_json.json" , 'w') as archivo:
    json.dump(dicc, archivo)

with open("archivo_json.json" , 'r') as archivo:
    dta = json.load(archivo)

print(dta)
