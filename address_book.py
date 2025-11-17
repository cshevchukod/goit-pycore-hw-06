from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self._validate(value)
        super().__init__(value)

    def _validate(self, value):
        # валідація: строка, 10 цифр
        if not isinstance(value, str):
            raise ValueError("Phone number must be a string")
        digits = value.strip()
        if not (digits.isdigit() and len(digits) == 10):
            raise ValueError("Phone number must contain exactly 10 digits")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        #Додати новий телефон до контакту.
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        #Видалити телефон зі списку. Повертає True/False.
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        #Змінити існуючий телефон на новий.
        for p in self.phones:
            if p.value == old_phone:
                # перевірка нового номера
                p._validate(new_phone)
                p.value = new_phone
                return True
        #Якщо за завданням хочеться мʼякше – можна замість raise повернути False
        raise ValueError("Phone to edit not found")

    def find_phone(self, phone):
        #Повертає обʼєкт Phone або None.
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        #Додати Record до книги. Ключ — імʼя (рядок).
        self.data[record.name.value] = record

    def find(self, name):
        #Знайти Record за імʼям. Повертає Record або None.
        return self.data.get(name)

    def delete(self, name):
        #Видалити Record за імʼям.
        if name in self.data:
            del self.data[name]
