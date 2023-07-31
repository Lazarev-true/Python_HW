from dataclasses import dataclass


@dataclass
class User:
    name: str
    id_: int
    level: int = None

    def __eq__(self, other):
        return  self.id_ == other.id_ and self.name == other.name

if __name__ == "__main__":
    e1 = User('asd', 5, 6)
    e2 = User('asd', 3, 6)
    print(e1.level > e2.level)
    