class Inventory:
    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.items = []
        self.real_capacity = __capacity

    def add_item(self, item: str):
        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.real_capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
