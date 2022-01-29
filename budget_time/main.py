from datetime import date
import ast
today = date.today()
today_date = today.strftime("%d.%m.%Y")


class bill:
    file_name = "all_bill_file.txt"
    bills_list = []

    def create_bills_file(self, name):
        global file_name
        file_name = name + ".txt"

        try:
            with open(file_name, 'x', encoding='utf8') as f:
                f.write("")
                f.close()
#'Created: '+ today_date + '\nAll bills: \n'

        except FileExistsError:
            print('You are adding a bill to an existing file named: '+ file_name)


    def read_list_from_file(self):
        bills_file = open(file_name,'r', encoding='utf8')
        if bills_file.readable():
            file_text = bills_file.readlines()
            selected_js = ast.literal_eval(file_text[1])
            print(type(selected_js))
            print(selected_js['sum'])
            for sum in sums


    def input_and_return_dictionary(self):
        sum = input('Podaj kwote: ')
        category = input('Podaj kategorie: ')
        which_store = input('gdzie zrobiono zakupy: ')
        date = input('Podaj date dd.MM.yyyy: ')
        final_dict = {'sum': str(sum), 'category': str(category), 'which_store': str(which_store), 'date': str(date)}
        return final_dict


    def add_to_file_as_list(self, bill):
        global file_name
        global bills_list

        bills_file = open(file_name, 'a+', encoding='utf8')

        if bills_file.writable():
            bills_file.write(f'{bill}\n')
        else:
            print("You can't write in this file")
        bills_file.close()


new_bill = bill()
new_bill.create_bills_file("all_bills6")
new_bill.read_list_from_file()
new_bill.add_to_file_as_list(new_bill.input_and_return_dictionary())
