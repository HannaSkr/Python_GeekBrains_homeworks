
def new_surname():
    while True:
        last_name = input('Введите фамилию: ')
        if last_name.isalpha():                
            return last_name.capitalize()
        else:
            print('некорректный ввод. попробуйте еще раз')   

    
def new_name():  
    while True:
        first_name = input('Введите имя: ')
        if first_name.isalpha():                
            return first_name.capitalize()
        else:                
            print('некорректный ввод. попробуйте еще раз')   
 
 
def new_number():    
    while True:
        phone_number = (input('Введите +<код> и номер телефона без пробелов: '))
        if phone_number[0] == "+" and phone_number[1:].isdigit() and len(phone_number) <= 13:
            return phone_number
        else:
            print("некорретно введен номер. попробуйте еще раз")


def ask_user():
    last_name = new_surname()
    first_name = new_name()
    phone_number = new_number()
    return last_name, first_name, phone_number


def add_to_book(data_file):
    data = ' '.join(ask_user())
    with open(data_file, 'a', encoding='utf-8') as file:
        file.write(f'{data}\n')


def read_file(data_file):
    with open(data_file, 'r', encoding='utf-8') as file:     
        list_contacts = []
        for line in file.readlines():               
            list_contacts.append(line.split())
    return list_contacts


def read_file_dic(data_file):
    with open(data_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['фамилия', 'имя', 'номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts


def search_contact(list_contacts):
    param, what = ask_search()
    param_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        try:  
            if contact[param_dict.get(param)] == what:
                found_contacts.append(contact)
        except KeyError:
            print('такого поля для поиска нет')
            break
    if len(found_contacts) == 0:
            print('по вашему запросу ничего не найдено')
    else:
        print_contacts(found_contacts)


def ask_search():
    try:
        print('По какому полю выполнить поиск?')
        search_param = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
        what = None
        if search_param == '1':
            what = input('Введите фамилию для поиска: ')
        elif search_param == '2':
            what = input('Введите имя для поиска: ')
        elif search_param == '3':
            what = input('Введите номер для поиска: ')
    except IndexError:
        print("некорректный ввод!")
    return search_param, what


def searching(list_contacts: list):
    param, what = ask_search()
    result = []
    for contact in list_contacts:
        try:
            if contact[int(param) - 1] == what:
                result.append(contact)
        except IndexError:
            print('некорректный ввод!')
            break
    if len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print('по вашему запросу найдено: ')
        for i in range(len(result)):
            print(f'{i + 1} - {result[i]}')               
        numer = int(input('данные какого контакта вы хотите отредактировать? '))
        return result[numer - 1]
    else:
        print('по вашему запросу ничего не найдено')
       

def correct_contact(data_file):
    list_contacts = read_file(data_file)
    num = searching(list_contacts)
    try:
        list_contacts.remove(num)    
        print('Данные какого поля будут изменены?')
        search_param = input('1 - фамилия\n2 - имя\n3 - номер телефона\n')
        if search_param == '1':
            num[0] = new_surname()
        elif search_param == '2':
            num[1] = new_name()
        elif search_param == '3':
            num[2] = new_number()
        list_contacts.append(num)
        print('контакт успешно изменен')
    except ValueError:
        print('попробуйте еще раз')
    with open(data_file, 'w', encoding='utf-8') as file:
        for contact in list_contacts:
            line = ' '.join(contact) + '\n'
            file.write(line)


def import_contacts(addition_to_book, book):
    try:
        with open(addition_to_book, 'r', encoding='utf-8') as new_contacts, open(book, 'a', encoding='utf-8') as file:
            additional_contacts = new_contacts.readlines()
            file.writelines(addition_to_book)
    except FileNotFoundError:
        print(f' файл {addition_to_book} не найден')


def show_all(data_file):
    lists_contacts = sorted(read_file_dic(data_file), key=lambda x: x['фамилия'])
    print_contacts(lists_contacts)
    return lists_contacts


def delete_contact(data_file):
    list_contacts = read_file(data_file)
    contact_exclude = searching(list_contacts)
    try:
        list_contacts.remove(contact_exclude)
        with open(data_file, 'w', encoding='utf-8') as file:
            for contact in list_contacts:
                line = ' '.join(contact) + '\n'
                file.write(line)
        print('контакт успешно удален')
    except ValueError:
        print("попробуйте еще раз")
    
    
def print_contacts(list_contacts: list):
    for contact in list_contacts:
        for key, value in contact.items():
            print(f'{key}: {value:10}', end = '\t')
        print()

def main_menu(book):
    while True:
        print('выберите, что вы хотите сделать\n')
        choice = (input('Введите "1" если хотите добавить новый контакт\n' + \
                            'Введите "2" если хотите найти контакт\n' + \
                            'Введите "3" если хотите корректировать данные контакта \n' + \
                            'Введите "4" если хотите удалить контакт\n' + \
                            'Введите "5" если хотите просмотреть всю адресную книгу\n' + \
                            'Введите "6" если хотите импортировать адресную книгу\n' + \
                            'Введите "0" если хотите выйти из справочника\n' + \
                            'сделайте свой выбор: '))
        if choice == '1':
            add_to_book(book)
        elif choice == '2':
            list_contacts = read_file_dic(book)
            search_contact(list_contacts)
        elif choice == '3':
            correct_contact(book)
        elif choice == '4':
            delete_contact(book)
        elif choice == '5':   
            show_all(book)
        elif choice == '6':
            addition = input('введите имя файла для импорта контактов: ')
            import_contacts(addition, book)
        elif choice == '0':      
            print('До свидания')
            break
        else:
            print("некорректный ввод! попробуйте еще раз: ")  
    

if __name__ == '__main__':
    file = 'Book.txt'
    main_menu(file)
    