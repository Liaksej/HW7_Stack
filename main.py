from stack import Stack


def check_balance_parenthesis(list_for_check) -> str:
    list_for_check = list(list_for_check)
    if Stack(list_for_check).size() % 2 == 0 and (Stack(list_for_check).peek() != ']'
                                                  or Stack(list_for_check).peek() != ')'
                                                  or Stack(list_for_check).peek() != '}'):
        stack = []
        for item in list_for_check:
            if item == '(' or item == '[' or item == '{':
                Stack(stack).push(item)
            elif (item == ')' or item == ']' or item == '}') and [Stack(stack).peek(), item] == ['(', ')'] \
                    or [Stack(stack).peek(), item] == ['[', ']'] \
                    or [Stack(stack).peek(), item] == ['{', '}']:
                Stack(stack).pop()
            else:
                return 'Несбалансирован'
        if Stack(stack).size() == 0:
            return 'Сбалансирован'
        else:
            return 'Несбалансирован'
    else:
        return 'Несбалансирован'


if __name__ == '__main__':
    parenthesis_list = input('Введите строку со скобками для проверки: ')
    print(check_balance_parenthesis(parenthesis_list))
