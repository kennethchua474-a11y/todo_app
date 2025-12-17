import os
from todo_app.core import TodoList

def test_add_item():
    todo = TodoList()
    todo.add_item("Buy milk")

    assert todo.items == ["Buy milk"]

def test_add_empty_item_is_ignored():
    todo = TodoList()
    todo.add_item("")
    
    assert todo.items == []

def test_delete_item():
    todo = TodoList()
    todo.add_item("Buy milk")
    todo.add_item("Read book")

    todo.delete_item(0)
    
    assert todo.items == ["Read book"]

def test_delete_invalid_index_does_nothing():
    todo = TodoList()
    todo.add_item("Buy milk")

    todo.delete_item(99)

    assert todo.items == ["Buy milk"]

def test_save(tmp_path):
    todo = TodoList()
    todo.add_item("Buy milk")
    todo.add_item("Read book")

    file_path = tmp_path / "test_todo.txt"
    todo.save(file_path)
    
    assert file_path.read_text().splitlines() == [
            "Buy milk",
            "Read book",
            ]
