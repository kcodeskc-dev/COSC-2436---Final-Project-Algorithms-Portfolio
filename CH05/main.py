
from typing import List, Any

class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key: Any) -> int:
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> None:
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key: Any) -> Any:
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                return None
        return None

if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.insert("apple", 100)
    hash_table.insert("banana", 200)
    hash_table.insert("orange", 300)
    print(hash_table.search("apple"))
    print(hash_table.search("banana"))
    print(hash_table.search("orange"))
    print(hash_table.search("grape"))
