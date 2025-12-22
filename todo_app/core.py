from typing import List


class TodoList:
    def __init__(self) -> None:
        self.items: List[str] = []

    def add_item(self, item: str) -> None:
        if not item.strip():
            return
        self.items.append(item)

    def delete_item(self, index: int) -> None:
        if 0 <= index < len(self.items):
            self.items.pop(index)

    def save(self, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            for item in self.items:
                f.write(item + "\n")
