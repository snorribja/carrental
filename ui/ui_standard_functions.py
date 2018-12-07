from datetime import date


class UIStandard(object):
    def __init__(self, name, a_type):
        self.__name = name
        self.__a_type = a_type

    def show_menu(self, text, prompt):
        '''Prentar það menu sem notandi er staddur á.'''
        self.print_header()
        print(text)
        choice = input(prompt)
        return choice

    def print_header(self):
        '''Prentar haus fyrir Kerfisstjóra'''
        print("{:40s} {:>55}".format(
            "{} - notandi: {}".format(self.__a_type, self.__name), str(
                date.today())))
        print(("-"*100))