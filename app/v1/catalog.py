class Catalog:
    def __init__(self):
        self.items = {}

    def add(self, item):
        if item.id.value in self.items:
            raise ValueError("Already in catalog")
        self.items[item.id.value] = item
    
    def get(self, id):
        if id in self.items:
            item = self.items[id]
            return item
        else:
            raise ValueError("Item does not exist")


