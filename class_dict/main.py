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
        long = input("Pelna nazwa: ")
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
        long = input("Pelna nazwa: ")

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
                answer = input(f'"{short}" ma mniej niz 4 znaki, czy chcesz dodać skrót? t/n: ')
                if answer == 't' or answer == 'T':
                    self.add_shortcut_auto(short)
                    return self.dictionary[short]
            elif short == "/add":
                print("Przeszedłes do funkcji dodawania skrotow do slownkika")
                self.add_shortcut_manual()
            else:
                return  short


while True:
    kategoria = Shortcut("kategorie")

    print(kategoria.use_shortcut(input("podaj kategorie: ")))