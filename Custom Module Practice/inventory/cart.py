from dataclasses import dataclass

@dataclass()
class Cart():
    name: str
    items = []
    def add_item(self, item):
        self.items.append(item)