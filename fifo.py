from collections import deque

# +
# Простота понимания и отладки кода
# Фиксированное использование памяти

# -
# Ограниченная размерность
# Удаление данных в ручную, если буффер заполнен

class CircularBufferList:
    # Инициализация
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    # Добавление элемента
    def put(self, item):
        if self.size == self.capacity:
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
    # Удаление элемента
    def pop(self):
        if self.size == 0:
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item
    # Проверка буффера на пустоту
    def is_empty(self):
        return self.size == 0
    # Проверка на заполненность буффера
    def is_full(self):
        return self.size == self.capacity

    def __repr__(self):
        return f"CircularBufferList({self.buffer}, head={self.head}, tail={self.tail}, size={self.size})"


#+
# Автоматическое управление памятью.
# Чтение/запись за O(1)
# Легкость использования - стандартный класс делает код понятние для чтения.

#-
# Ограниченный контроль над реализацией - deque - уже написанный класс.
# Больший расход по памяти из-за внутреннего устройства deque.


class CircularBufferDeque:
    # Инициализация
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.buffer = deque(maxlen=capacity)
        self.capacity = capacity
    # Добавление элемента
    def put(self, item):
        if len(self.buffer) == self.capacity:
            raise OverflowError("Buffer is full")
        self.buffer.append(item)
    # Удаление элемента
    def pop(self):
        if not self.buffer:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()
    # Проверка буффера на пустоту
    def is_empty(self):
        return len(self.buffer) == 0
    # Проверка на заполненность буффера
    def is_full(self):
        return len(self.buffer) == self.capacity

    def __repr__(self):
        return f"CircularBufferDeque({list(self.buffer)})"
