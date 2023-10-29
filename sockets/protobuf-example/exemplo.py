import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "Joaquim Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PhoneType.WORK

# serializar

person_binary = person.SerializeToString()

print(person_binary)

