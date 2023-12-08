from collections import UserDict

# The base class for storing field values
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Class representing the name field, inheriting from Field
class Name(Field):
    def __init__(self, value):
        super().__init__(value)

# Class representing the phone field, inheriting from Field
class Phone(Field):
    def __init__(self, value):
        # Validates and sets the phone number value
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits.")
        super().__init__(value)

    # Allows changing the phone number value with validation
    def set_value(self, new_value):
        if len(new_value) != 10 or not new_value.isdigit():
            raise ValueError("Phone number must contain 10 digits.")
        self.value = new_value

# Class representing a record
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Adds a phone number to the record
    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    # Removes a phone number from the record
    def remove_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                self.phones.remove(p)
                break

    # Edits an existing phone number in the record
    def edit_phone(self, old_phone, new_phone):
        phone_exists = False
        for p in self.phones:
            if str(p) == old_phone:
                p.set_value(new_phone)
                phone_exists = True
                break
        
        if not phone_exists:
            raise ValueError(f"Phone number '{old_phone}' does not exist in this record.")

    # Finds a phone number in the record
    def find_phone(self, phone_number):
        for p in self.phones:
            if str(p) == phone_number:
                return p  # Returns the phone number value
        return None  # Returns None if the phone is not found

    # String representation of the record
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

# AddressBook class extending UserDict for managing records
class AddressBook(UserDict):
    # Adds a record to the address book
    def add_record(self, record):
        self.data[record.name.value] = record

    # Finds a record by name in the address book
    def find(self, name):
        return self.data.get(name)
    
    # Deletes a record by name from the address book
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"The record '{name}' does not exist in the address book.")


# Creating a new address book
book = AddressBook()

# Creating a record for John and adding phones
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Adding John's record to the address book
book.add_record(john_record)

# Creating and adding a new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Displaying all records in the book
for name, record in book.data.items():
    print(record)

# Finding and editing John's phone number
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

# Finding a specific phone number in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Output: 5555555555

# Deleting Jane's record
book.delete("Jane")