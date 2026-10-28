class MyList:
    def __init__(self, *data):
        self.capacity = len(data)
        self._size = self.capacity
        self._data = [None] * self.capacity

        for i in range(self._size):
            self._data[i] = data[i]

    def count(self):
        return self._size

    def get(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("Индекс вне списка")
        return self._data[index]

    def first(self):
        if self._size == 0:
            raise IndexError("Список пуст")
        return self.get(0)

    def last(self):
        if self._size == 0:
            raise IndexError("Список пуст")
        return self.get(self._size - 1)

    def includes(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return True
        return False

    def _up_capacity(self):
        new_capacity = max(1, self.capacity * 2)
        new_data = [None] * new_capacity

        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
        self.capacity = new_capacity

    def append(self, item):
        if self._size == self.capacity:
            self._up_capacity()

        self._data[self._size] = item
        self._size += 1

    def prepend(self, item):
        if self._size == self.capacity:
            self._up_capacity()

        for i in range(self._size, 0, -1):
            self._data[i] = self._data[i - 1]

        self._data[0] = item
        self._size += 1

    def remove(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                for j in range(i, self._size - 1):
                    self._data[j] = self._data[j + 1]

                self._size -= 1
                self._data[self._size] = None
                return True

        return False

    def remove_first(self):
        if self._size == 0:
            raise IndexError("Список пуст")

        item = self.first()

        for i in range(self._size - 1):
            self._data[i] = self._data[i + 1]

        self._size -= 1
        self._data[self._size] = None
        return item

    def remove_last(self):
        if self._size == 0:
            raise IndexError("Список пуст")

        self._size -= 1
        item = self._data[self._size]
        self._data[self._size] = None
        return item

    def remove_all(self):
        self._data = [None] * self.capacity
        self._size = 0


class MyIterator:
    def __init__(self, iter_obj: MyList):
        self._obj = iter_obj
        self._pos = 0
        self._obj_len = self._obj.count()

    def first(self):
        self._pos = 0

    def next(self):
        if not self.is_done():
            self._pos += 1

    def is_done(self):
        return self._pos >= self._obj_len

    def cur_item(self):
        if self.is_done():
            raise IndexError("Итератор завершен")
        return self._obj.get(self._pos)

    def __iter__(self):
        self.first()
        return self

    def __next__(self):
        if self.is_done():
            raise StopIteration

        item = self.cur_item()
        self.next()
        return item


class MyListIterator(MyList):
    def __iter__(self):
        return MyIterator(self)


# Проверка работы
my_list = MyList(10, 20, 30)

my_list.append(40)
my_list.prepend(5)

print("Количество:", my_list.count())
print("Первый:", my_list.first())
print("Последний:", my_list.last())
print("Есть 20:", my_list.includes(20))

iterator = MyIterator(my_list)

print("Обход через итератор:")
iterator.first()

while not iterator.is_done():
    print(iterator.cur_item())
    iterator.next()

print("Удаляем 20:", my_list.remove(20))
print("Удаляем первый:", my_list.remove_first())
print("Удаляем последний:", my_list.remove_last())

print("Осталось элементов:", my_list.count())

print("Обход через for:")
another_list = MyListIterator(1, 2, 3)
for item in another_list:
    print(item)
