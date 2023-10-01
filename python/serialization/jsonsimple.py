from json import dumps, loads

from pessoa import Pessoa

pessoa = Pessoa("Joao da Silva", 'Quixada', '999990000', '2014')

pessoa_json = dumps(pessoa.__dict__)

# __dict__ vai converter o objeto em um dicionario, ai o dumps converte o dicionario em json

print(pessoa.__dict__)
print(pessoa_json)

print(type(pessoa_json))

print(loads(pessoa_json))

print(dumps(["a", "b", "c"]))
print(dumps({ "hello": "world" }))