class Inventory:
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []
    def add_item(self, item: str):
        if len(self.items) == self.__capacity:
            return "not enough room in the inventory"
        self.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = len(self.items) - self.__capacity
        items = ', ' .join(self.items)
        return f"Items: {items}.\nCapacity left: {left_capacity}"



