
import addressbook_pb2

data = b'\n\x08John Doe\x10\xd2\t\x1a\x10jdoe@example.com"\x0c\n\x08555-4321\x10\x02'

person = addressbook_pb2.Person()
person.ParseFromString(data)

print(person)