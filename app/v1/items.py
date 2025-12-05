class Id:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value

class Item():
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def days_allowed(self):
        raise NotImplementedError

class Book(Item):
    def __init__(self, id, title):
        super().__init__(id, title)
    
    def days_allowed(self):
        return 10

class Dvd(Item):
    def __init__(self, id, title):
        super().__init__(id, title)
    
    def days_allowed(self):
        return 7