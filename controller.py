import view
import data
import write_down
import removal 
import out_data 
import out_search 


def book():
        while True:
            print('Список команд: \n 1 - добавить контакт \n 2 - удалить контакт \n 3 - посмотреть список контактов \n 4 - найти номер по имени \n 5 - завершить работу \n')
            command = int(input('Введите номер команды: '))
            if command == 1:
                a = view.name1()
                b = view.surname1()
                c = view.telefon1()
                d = view.description1()
                data.id(a,b,c,d)
                book_new = data.get_id()
                write_down.save_phone_number(book_new)
                print('Контакт Сохранен \n')
            elif command == 2:
                x = view.contact_search()
                removal.del_phone_number(x)
                print('Контакт удалетн \n')
            elif command == 3:
                print('Телефонная книга: \n')
                out_data.look_phone_book()
            elif command == 4:
                x = view.contact_search()
                print('Данные по запросу: \n')
                out_search.search_view_number(x)
            elif command == 5:
                print('работа завершена')
                break
            else:
                print('ошибка')