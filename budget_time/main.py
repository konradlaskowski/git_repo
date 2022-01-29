from datetime import date
today = date.today()
today_date = today.strftime("%d.%m.%Y")


class bill:
    file_name = "all_bill_file.txt"

    def create_bills_file(self, name):

        global file_name
        file_name = name + ".txt"

        try:
            with open(file_name, 'x', encoding='utf8') as f:
                f.write('Created: '+ today_date + '\nAll bills: \n')
                f.close()

        except FileExistsError:
            print('You add a bill to an existing file named: '+ file_name)


    def read_list_from_file(self):
        bills_file = open(file_name,'r')
        print(bills_file.read())


    def input_and_return_dictionary(self):
        sum = input('Podaj kwote: ')
        category = input('Podaj kategorie: ')
        which_store = input('gdzie zrobiono zakupy: ')
        date = input('Podaj date dd.MM.yyyy: ')
        return {'sum':sum, 'category':category, 'which_store':which_store, 'date':date}


    def add_to_file_as_list(self, bill):
        global file_name
        bills_file = open(file_name, 'a+', encoding='utf8')


        if bills_file.writable():
            bills_file.write(f'Rachunek: {bill} \n')
        else:
            print("You can't write in this file")
        bills_file.close()




new_bill = bill()
new_bill.create_bills_file("all_bills")
dict_bill = new_bill.input_and_return_dictionary()
new_bill.add_to_file_as_list(dict_bill)
