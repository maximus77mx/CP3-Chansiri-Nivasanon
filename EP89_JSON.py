import json
def readJson():
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    print(y["name"])
def writeJson():
    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }
    y = json.dumps(x)
    print(y)

readJson()
writeJson()