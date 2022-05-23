def input_error(func):
    def inner(sentence):
        try:
            result = func(sentence)
            return result
        except ValueError:
            return 'Введите все параметры'
        except KeyError:
            return 'Такого пользователя нет'
        except IndexError:
            return 'Превышен размер словаря'
    return inner

