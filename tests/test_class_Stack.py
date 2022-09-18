import pytest

from stack import Stack


class TestStack:

    @pytest.fixture
    def setup(self):
        self.some_list = [1, 2, 3]
        self.element = '4'
        yield

    def test_is_empty(self, setup):
        assert Stack(self.some_list).is_empty() is False

    def test_push(self, setup):
        Stack(self.some_list).push(self.element)
        assert self.some_list[0] == self.element

    def test_pop(self, setup):
        control_list = self.some_list.copy()
        assert Stack(self.some_list).pop() == control_list[0]

    def test_peek(self, setup):
        control_list = self.some_list.copy()
        assert Stack(self.some_list).peek() == control_list[0]

    def test_size(self, setup):
        control_list = self.some_list
        assert Stack(self.some_list).size() == len(control_list)


if __name__ == '__main__':
    TestStack()
