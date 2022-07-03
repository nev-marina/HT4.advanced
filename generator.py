nested_list = [['a', 'b', 'c'],
               ['d', 'e', 'f', 'h', False],
               [1, 2, None],
               ]

my_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', [5, 10, 'f']],
    [1, 2, None],
]


def flat_generator(list_of_lists):
    for some_list in list_of_lists:
        for item in some_list:
            yield item


def flat_generator_2(deep_of_lists):
    for item in deep_of_lists:
        if isinstance(item, list):
            yield from flat_generator_2(item)
        else:
            yield item


print('\n2. Генератор:')

for item in flat_generator(nested_list):
    print(item)
print(list(flat_generator(nested_list)))

print('\n4*. Генератор:')

for item in flat_generator_2(my_list):
    print(item)
print(list(flat_generator_2(my_list)))
