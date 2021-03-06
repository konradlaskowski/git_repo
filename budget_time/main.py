import ast
import time
import shortcut
from datetime import date

# selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # for error repairing
from selenium.webdriver.common.by import By

sc = shortcut

# date
today = date.today()
today_date = today.strftime("%d.%m.%Y")


option = webdriver.ChromeOptions()
option.add_argument("--headless")
# option.add_argument("-incognito")
# option.add_argument("disable-gpu")

amount = 0
category = ""
which_store = ""
date = ""
descr = ""


# apk_core
def send_bill_to_google_sheet(amount0, category0, which_store0, date0, descr0):
    global browser
    # form_link_Type = "viewform"
    # form_link_Type = "formResponse"
    form_url = "https://docs.google.com/forms/d/e/" \
               "1FAIpQLScd-bzDGa8E4g1qwIzk-ijl6y0LMRb0N2eAGNQ3-Zi1TfebCw" \
               "/viewform"
    service = Service("chromedriver.exe")
    browser = webdriver.Chrome(service=service, options=option)

    full_url = f"{form_url}?" \
               f"entry.2080550111={amount0}" \
               f"&entry.468806156={category0}" \
               f"&entry.1402840532={which_store0}" \
               f"&entry.196396817={date0}" \
               f"&entry.1982941332={descr0}"
    browser.get(full_url)
    submit = browser.find_element(
        By.CLASS_NAME, "appsMaterialWizButtonPaperbuttonContent"
    )
    time.sleep(2)
    submit.click()


class Bill:
    file_name = "bill_file.txt"
    bills_list = []

    def create_bills_file(self, name):
        global file_name
        file_name = name + ".txt"

        try:
            with open(file_name, "x", encoding="utf8") as f:
                f.write("")
                print(f"File {file_name} created")
                f.close()

        except FileExistsError:
            print(
                "You are adding a bill to an existing file named: " + file_name
            )

    def return_file_as_list(self):
        bills_file = open(file_name, "r", encoding="utf8")

        if bills_file.readable():
            file_list = bills_file.readlines()
            return file_list
        bills_file.close()

    def return_sum_all_bills(self):
        bills_file = open(file_name, "r", encoding="utf8")

        if bills_file.readable():
            file_line_list = bills_file.readlines()
            sum_all_bills = 0

            for line in file_line_list:
                line_js = ast.literal_eval(line)
                sum_all_bills += int(line_js["sum"])
            return sum_all_bills
        bills_file.close()

    def input_and_return_dict(self):
        global amount
        global category
        global which_store
        global date
        global descr
        amount = input("Podaj kwote: ")

        cat = sc.Shortcut("category")
        category = cat.use_shortcut(input("Podaj kategorie: "))
        w_s = sc.Shortcut("which_store")
        which_store = w_s.use_shortcut(input("gdzie zrobiono zakupy: "))

        date = sc.spec_cmd(input("Podaj date dd.MM.yyyy: "))
        descr_input = input("Opis: ")
        if descr_input == "":
            descr = "brak"
        else:
            descr = descr_input
        final_dict = {
            "sum": str(amount),
            "category": str(category),
            "which_store": str(which_store),
            "date": str(date),
            "descr": str(descr),
        }
        return final_dict

    def check_shortcuts(self, input, short, full):
        if input == short:
            return full

    def add_to_file(self, bill):
        global file_name
        global bills_list

        bills_file = open(file_name, "a+", encoding="utf8")

        if bills_file.writable():
            bills_file.write(f"{bill}\n")
        else:
            print("You can't write in this file")
        bills_file.close()

    def confirmation_page(self):
        global browser
        global file_name
        try:
            confirmation_message = browser.find_element(
                By.XPATH,
                "//div[@class="
                "'freebirdFormviewerViewResponseConfirmationMessage']",
            ).text
            if confirmation_message == "Twoja odpowied?? zosta??a zapisana.":
                print("-------\nUda??o si??!\n-------")
                print(
                    f"Kwota: {amount} PLN\n"
                    f"Kategoria: {category}\n"
                    f"Sklep: {which_store}\n"
                    f"Data: {date}\n"
                    f"Opis: {descr}\n"
                    f"-------\n"
                    f" * RACHUNEK ZOSTA?? DODANY DO GOOGLE FORM\n"
                    f"** RACHUNEK ZOSTA?? ZAPISANY DO PLIKU ->{file_name}"
                )
        except ConnectionError:
            print("b????d podczas wysylania")
        finally:
            browser.close()


new_bill = Bill()
new_bill.create_bills_file("all_bills_file")

while True:
    global file_name
    bill_as_dict = new_bill.input_and_return_dict()
    new_bill.add_to_file(bill_as_dict)
    print(
        f"Suma wszystkich pragon??w w ->"
        f" {file_name}:"
        f" {new_bill.return_sum_all_bills()} z??."
    )
    print("Wysy??anie do Google Form...")
    send_bill_to_google_sheet(amount, category, which_store, date, descr)
    new_bill.confirmation_page()
