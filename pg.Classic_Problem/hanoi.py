from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic(T)):
    def __init__(self) -> None:
        self._container:List[T] = []
    
    def push(self, item:T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs:int = 3
tower_a:stack[int] = stack()
tower_b:stack[int] = stack()
tower_c:stack[int] = stack()
for i in range(1, num_discs+1):
    tower_a.push(i)
    