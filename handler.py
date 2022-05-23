from parser import parser
from input_error import input_error


@input_error
def handler(sentence, phone_dict={}):
    def all_function(sentence):
        if parser(sentence) == 'HELLO':
            return "How can I help you?"

        if parser(sentence) == 'ADD':
            _, name, number, *args = sentence.split(' ')
            phone_dict[name] = number

        if parser(sentence) == 'CHANGE':
            _, name, new_number, *args = sentence.split(' ')
            phone_dict[name] = new_number

        if parser(sentence) == 'PHONE':
            _, name, *args = sentence.split(' ')
            return phone_dict.get(name, 'Такого пользователья нет')

        if parser(sentence) == 'SHOW ALL':
            dict_list = ''
            for key, value in phone_dict.items():
                dict_list += f'{key}: {value}\n'
            return dict_list

        if parser(sentence) == 'EXIT' or \
           parser(sentence) == 'CLOSE' or \
           parser(sentence) == 'GOOD BYE':
            print('До новых встреч!')
            return 'exit'

        if parser(sentence) is None:
            return 'Введите команду из списка доступных команд!'

        return 'Операция прошла успешно'
    return all_function(sentence)


if __name__ == '__main__':
    sentence = 'add Vlad 067 Vlad 050 vfd    ljh'
    print(handler(sentence))