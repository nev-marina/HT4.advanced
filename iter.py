nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

my_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', [5, 10, 'f']],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, lst):
        self.lst = sum(lst, [])

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        else:
            return self.lst[self.index]


class FlatIterator2:
    def __init__(self, deep_of_lists):
        self.flat = []
        for item in deep_of_lists:
            if isinstance(item, list):
                self.flat.extend(FlatIterator2(item))
            else:
                self.flat.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.flat:
            raise StopIteration
        item = self.flat[0]
        del self.flat[0]
        return item


print('\n1. Итератор:')
for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print('\n3*. Итератор:')
for item in FlatIterator2(my_list):
    print(item)

flat_list = [item for item in FlatIterator2(my_list)]
print(flat_list)
