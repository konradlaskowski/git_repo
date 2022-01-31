import ast
import time
#date
from datetime import date
today = date.today()
today_date = today.strftime("%d.%m.%Y")

#selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service #for error repairing
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("--headless")
#option.add_argument("-incognito")
#option.add_argument("disable-gpu")

amount = 0
category = ""
which_store = ""
date = ""
descr = ""

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
            ### go to adding bill function
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


while True:
    kategoria = Shortcut("kategorie")

    print(kategoria.use_shortcut(input("podaj kategorie: ")))




#apk_core
class bill:
    file_name = "bill_file.txt"
    bills_list = []

    def send_bill_to_google_sheet(self, amount, category, which_store, date, descr):
        global browser
        #form_link_Type = "viewform"
        #form_link_Type = "formResponse"
        formURL = "https://docs.google.com/forms/d/e/1FAIpQLScd-bzDGa8E4g1qwIzk-ijl6y0LMRb0N2eAGNQ3-Zi1TfebCw/viewform"
        s = Service("chromedriver.exe")
        browser = webdriver.Chrome(service=s, options=option)

        full_url = f"{formURL}?entry.2080550111={amount}&entry.468806156={category}&entry.1402840532={which_store}&entry.196396817={date}&entry.1982941332={descr}"
        browser.get(full_url)
        submit = browser.find_element(By.CLASS_NAME, "appsMaterialWizButtonPaperbuttonContent")
        time.sleep(2)
        submit.click()

    def create_bills_file(self, name):
        global file_name
        file_name = name + ".txt"

        try:
            with open(file_name, 'x', encoding='utf8') as f:
                f.write("")
                print(f"File {file_name} created")
                f.close()

        except FileExistsError:
            print('You are adding a bill to an existing file named: '+ file_name)


    def return_file_as_list(self):
        bills_file = open(file_name,'r', encoding='utf8')

        if bills_file.readable():
            file_list = bills_file.readlines()
        bills_file.close()
        return file_list


    def return_sum_all_bills(self):
        bills_file = open(file_name, 'r', encoding='utf8')

        if bills_file.readable():
            file_line_list = bills_file.readlines()
            sum_all_bills = 0

            for line in file_line_list:
                line_js = ast.literal_eval(line)
                sum_all_bills += int(line_js['sum'])
        bills_file.close()
        return sum_all_bills



    def input_and_return_dict(self):
        global amount
        global category
        global which_store
        global date
        global descr
        amount = input('Podaj kwote: ')
        category = input('Podaj kategorie: ')
        which_store = input('gdzie zrobiono zakupy: ')
        date = input('Podaj date dd.MM.yyyy: ')
        descr = input('Opis: ')
        final_dict = {'sum': str(amount), 'category': str(category), 'which_store': str(which_store), 'date': str(date), 'descr': str(descr)}
        return final_dict

    def check_shortcuts(self, input, short, full):
        if input == short:
            return full

    def add_to_file(self, bill):
        global file_name
        global bills_list

        bills_file = open(file_name, 'a+', encoding='utf8')

        if bills_file.writable():
            bills_file.write(f'{bill}\n')
        else:
            print("You can't write in this file")
        bills_file.close()

    def confirmation_page(self):
        try:
            global browser
            global file_name
            confirmation_message = browser.find_element(By.XPATH, "//div[@class='freebirdFormviewerViewResponseConfirmationMessage']").text
            if confirmation_message == "Twoja odpowiedź została zapisana.":
                print("-------\nUdało się!\n-------")
                print(f"Kwota: {amount} PLN\nKategoria: {category}\nSklep: {which_store}\nData: {date}\nOpis: {descr}\n-------\n * RACHUNEK ZOSTAŁ DODANY DO GOOGLE FORM\n** RACHUNEK ZOSTAŁ ZAPISANY DO PLIKU ->{file_name}")
        except:
            print("błąd podczas wysylania")
        finally:
            browser.close()


new_bill = bill()
new_bill.create_bills_file("all_bills_file")

while True:
    global file_name
    bill_as_dict = new_bill.input_and_return_dict()
    new_bill.add_to_file(bill_as_dict)
    print(f"Suma wszystkich pragonów w -> {file_name}: {new_bill.return_sum_all_bills()} zł.")
    print("Wysyłanie do Google Form...")
    new_bill.send_bill_to_google_sheet(amount, category, which_store, date, "brak")
    new_bill.confirmation_page()




