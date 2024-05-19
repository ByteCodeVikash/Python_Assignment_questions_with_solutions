"""
9. Write a python script to create an application like Truecaller where names
and numbers are stored. Truecaller class will have 2 methods
(1st to fetch the name of a number and 2nd to add a new entry).

"""
class TrueCaller:
    def __init__(self):
        self.contacts = {}

    def fetch_name(self, number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return "Name not found for this number"

    def add_entry(self, name, number):
        self.contacts[number] = name
        print("Entry added:", name, number)

app = TrueCaller()

app.add_entry("Vikash", "123456")
app.add_entry("Shivan", "2657890")

print("Name of 123456:", app.fetch_name("123456"))
print("Name of 2657890:", app.fetch_name("2657890"))
print("Name of 1111111111111:", app.fetch_name("1111111111111"))
