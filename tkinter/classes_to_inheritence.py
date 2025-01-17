class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (98, 89, 67, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)
    
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


#ClassTest.static_method()

class Book:
    TYPES = ("hard", "paper")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weigthing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

#print(Book.TYPES) - hardcoded variables inside class
#book = Book("Hary", "hard", 1500)

#hard = Book.hardcover("Hary", 1500)

#print(hard)

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.conected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.conected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected")
    
#printer = Device("Printer", "USB")
#print(printer)
#printer.disconnect()

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaning)"
    
    def printing(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        else:
            print(f"Printing {pages} pages. ")
            self.remaining_pages -= pages

printer1 = Printer("Printer", "USB", 100)
printer1.printing(20)

print(printer1)

