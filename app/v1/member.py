class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def borrow(self, id):
        if len(self.borrowed_items) < 5:
            for item_id in self.borrowed_items:
                if item_id == id:
                    raise ValueError("Duplicate Item")
            self.borrowed_items.append(id)
        elif len(self.borrowed_items) >= 5:
            raise ValueError("5 items borrowed")
    
    def return_item(self, id):
        for item_id in self.borrowed_items:
            if item_id == id:
                self.borrowed_items.remove(id)
                return
        raise ValueError("Item Not Borrowed")

    def borrowed_ids(self):
        return self.borrowed_items

    def list_details(self, catalog):
        detail_list = []
        for item_id in self.borrowed_items:
            item = catalog.get(item_id)
            line = item_id + "-" + item.title + " (" + str(item.days_allowed()) + " days)"
            detail_list.append(line)
        return detail_list
