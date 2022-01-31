
class shortcut:
    category_sc_dict = {'s': 'spozywcze', 't': 'transport', 'j': 'jedzenie + dom', 'pw': 'pewne wplywy', 'w': 'wyglad', 'e': 'elektronika', 'd': 'datki', 'a': 'abonamenty i subskrybcje', 'ed': 'edukacja', 'el': 'elektronika'}
    shop_sc_dict = {}
    date_sc_dict = {}


    def return_long_category_ver(self):
        try:
            short = input("podaj kategorie: ")
            long = self.category_sc_dict[short]
            print(long)
            return long
        except:
            return short

    def return_long_shop_ver(self):
        short = input("podaj kategorie: ")
        long = self.shop_sc_dict[short]
        print(long)
        return long

    def return_long_date_ver(self):
        short = input("podaj kategorie: ")
        long = self.date_sc_dict[short]
        print(long)
        return long

    def add_to_dict_beta(self):
        short = input('skrot: ')
        long = input('pelna: ')
        self.category_sc_dict[str(short)] = str(long)
        print(f'Dodano skrót: {short} jako: {long}')
        return short

def adding_to_dict(dict):
        odp = " "
        while odp != "/p":
            if odp == '/p':
                print(sc.category_sc_dict)
            else:
                odp = sc.add_to_dict_beta()
                sc.add_to_dict_beta()



sc = shortcut()

