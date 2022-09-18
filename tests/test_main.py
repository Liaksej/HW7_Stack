import pytest

from main import check_balance_parenthesis

fixture_balanced = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]

fixture_nobalanced = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]',
]


@pytest.mark.parametrize('example', fixture_balanced)
def test_check_balance_parenthesis_1(example):
    assert check_balance_parenthesis(example) == 'Сбалансирован'


@pytest.mark.parametrize('example', fixture_nobalanced)
def test_check_balance_parenthesis_2(example):
    assert check_balance_parenthesis(example) == 'Несбалансирован'


if __name__ == '__main__':
    test_check_balance_parenthesis_1()
    test_check_balance_parenthesis_2()
