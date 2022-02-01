#short_cut class - in future place in new module

import ast



class Shortcut:
    def __init__(self,name):
        self.dictionary = {}
        self.file_name = f"sc_dict_{name}.txt"
        self.name = name
        try:
            dict_file = open(self.file_name, 'rt')


            if dict_file.readable():
                file = dict_file.read()
                if len(file) > 0:
                    self.dictionary = ast.literal_eval(file)


            try:
                dict_file = open(self.file_name, 'wt')
                dict_file.write(str(self.dictionary))
                dict_file.close()

            except:
                print("Unable to write to file")
        except:
            # create fille if nescesery
            dict_file = open(self.file_name, 'a+')
            dict_file.write(str(self.dictionary))
            print(f'* Utworzono plik ze slownikiem skrotow: {self.file_name}')

    def add_shortcut_auto(self, short):
        dict_file = open(self.file_name, 'rt')

        if dict_file.readable():
            file = dict_file.read()
            if len(file) > 0:
                self.dictionary = ast.literal_eval(file)
        long = input(f'Podaj pelna nazwe dla  " {short} "  : ')
        self.dictionary[short] = long

        try:
            dict_file = open(self.file_name, 'wt')
            dict_file.write(str(self.dictionary))
            dict_file.close()

        except:
            print("Unable to write to file")

    def add_shortcut_manual(self):
        dict_file = open(self.file_name, 'rt')

        if dict_file.readable():
            file = dict_file.read()
            if len(file) > 0:
                self.dictionary = ast.literal_eval(file)
        print(f'-Dodaj skrot do slownika: {self.name}')
        short = input("Skrot: ")
        long = input(f'Podaj pelna nazwe dla  " {short} "  : ')
        if short == "/back" or long == "/back":


            pass
        else:
            self.dictionary[short] = long

        try:
            dict_file = open(self.file_name, 'wt')
            dict_file.write(str(self.dictionary))
            dict_file.close()

        except:
            print("Unable to write to file")

    def use_shortcut(self, input0):
        short = input0
        try:
            long = self.dictionary[short]
            print(f'*** Uzyłeś skrótu do: {long}')
            return long
        except:
            if len(short) < 4:
                answer = input(f'***  " {short} "  ma mniej niz 4 znaki, czy chcesz dodać skrót? t/n: ')
                if answer == 't' or answer == 'T':
                    self.add_shortcut_auto(short)
                    return self.dictionary[short]
                else:
                    return short
            elif short == "/add":
                print("***  Przeszedłes do funkcji dodawania skrotow do slownkika")
                self.add_shortcut_manual()
            else:
                return short


from datetime import date,  timedelta
today = date.today()

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def spec_cmd(input0):
    if input0 == "t":
        date0 = today.strftime("%d.%m.%Y")
        print(date0)
        return date0
    if is_digit(input0):
        delta0 = int(input0) * -1
        date0 = date.today() - timedelta(days=delta0)
        date1 = date0.strftime("%d.%m.%Y")
        print(date1)
        return date1



    else:
        return input0




