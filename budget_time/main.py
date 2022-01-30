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
option.add_argument("-incognito")
#option.add_argument("disable-gpu")

sume = 0
category = ""
which_store = ""
date = ""
descr = ""

#apk_core
class bill:
    file_name = "all_bill_file.txt"
    bills_list = []

    def send_bill_to_google_sheet(self, sume, category, which_store, date, descr):
        global browser
        #form_link_Type = "viewform"
        #form_link_Type = "formResponse"
        formURL = "https://docs.google.com/forms/d/e/1FAIpQLScd-bzDGa8E4g1qwIzk-ijl6y0LMRb0N2eAGNQ3-Zi1TfebCw/viewform"
        s = Service("chromedriver.exe")
        browser = webdriver.Chrome(service=s, options=option)

        full_url = f"{formURL}?entry.2080550111={sume}&entry.468806156={category}&entry.1402840532={which_store}&entry.196396817={date}&entry.1982941332={descr}"
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
        global sume
        global category
        global which_store
        global date
        global descr
        sume = input('Podaj kwote: ')
        category = input('Podaj kategorie: ')
        which_store = input('gdzie zrobiono zakupy: ')
        date = input('Podaj date dd.MM.yyyy: ')
        final_dict = {'sum': str(sume), 'category': str(category), 'which_store': str(which_store), 'date': str(date)}
        return final_dict


    def add_to_file(self, bill):
        global file_name
        global bills_list

        bills_file = open(file_name, 'a+', encoding='utf8')

        if bills_file.writable():
            bills_file.write(f'{bill}\n')
        else:
            print("You can't write in this file")
        bills_file.close()

    def on_next_page(self):
        try:
            global browser
            confirmation_message = browser.find_element(By.XPATH, "//div[@class='freebirdFormviewerViewResponseConfirmationMessage']").text
            if confirmation_message == "Twoja odpowiedź została zapisana.":
                print("Udało się!")
                print(f"Rachunek na kwote: {sume} PLN\nZ kategorii: {category}\nZrobiony w: {which_store}\nDnia: {date}\nOpis: {descr}\n ZOSTAŁ DODANY DO GOOGLE FORM")
        except:
            print("błąd podczas wysylania")
        finally:
            browser.close()


new_bill = bill()
new_bill.create_bills_file("all_bills_file")

while True:
    bill_as_dict = new_bill.input_and_return_dict()
    new_bill.add_to_file(bill_as_dict)
    print(f"Suma wszystkich pragonów: {new_bill.return_sum_all_bills()} zł.")
    new_bill.send_bill_to_google_sheet(sume, category, which_store, date, "brak")
    new_bill.on_next_page()




