import ast
dictionary = {}
file_name = f"shortcut_dict.txt"

def print_dictionary_from_file():
    global dictionary

    try:
        dict_file = open(file_name, 'rt')
        file = dict_file.read()


        if len(str(file)) == 0:
            print('plik nie zawiera tekstu')

        elif file.count("{") == 0:
            print('plil nie zawiera słownika')

        else:
            dictionary = ast.literal_eval(file)

    except:
        #create fille if nescesery
        dict_file = open(file_name, 'a+')
        dict_file.write(str(dictionary))
        print('utworzono plik dictionary')


    print(dictionary)



def append_dictionary_in_file():

    dict_file = open(file_name, 'rt')
    global dictionary

    if dict_file.readable():
        file = dict_file.read()
        if len(file) > 0:
            dictionary = ast.literal_eval(file)
    short = input("short: ")
    long = input("long: ")

    dictionary[short] = long

    try:
        dict_file = open('shortcut_dict.txt', 'wt')
        dict_file.write(str(dictionary))
        dict_file.close()

    except:
        print("Unable to write to file")


print_dictionary_from_file()

while True:
    append_dictionary_in_file()
    print(dictionary)