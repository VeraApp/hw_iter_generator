class FlatIterator:

    def __init__(self, list_of_list):
        self.cursor = -1
        self.start = 0
        self.list = list_of_list
        self.len_list = len(self.list)


    def __iter__(self):
        self.cursor += 1
        self.start = 0
        return self

    def __next__(self):
        if self.start == len(self.list[self.cursor]):
            iter(self)

        if self.cursor == self.len_list:
            raise StopIteration

        self.start += 1
        item = self.list[self.cursor][self.start - 1]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



if __name__ == '__main__':
    test_1()