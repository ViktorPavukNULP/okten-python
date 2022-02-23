# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def print(self):
        pass

# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable

class Book(Printable):

    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)


class Magazine(Printable):

    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(self.name)


# 3) Створити свій кастомний Exception

class NonBookMagazineException(Exception):
    pass

# 4) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine інакше кидати свою кастомну помилку
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

class Main:
    def __init__(self):
        self.printable_list = []

    def add(self, element):
        if isinstance(element, Book) or isinstance(element, Magazine):
            self.printable_list.append(element)
        else:
            raise NonBookMagazineException

    def show_all_magazines(self):
        for el in self.printable_list:
            if isinstance(el, Magazine):
                el.print()

    def show_all_books(self):
        for el in self.printable_list:
            if isinstance(el, Book):
                el.print()


# 5)всі методи класу Main запускати в try except, приклад:
main = Main()
try:
    main.add(Magazine('Magazine1'))
    main.add(Book('Book1'))
    main.add(Magazine('Magazine3'))
    main.add(Magazine('Magazine2'))
    main.add(Book('Book2'))
    main.show_all_magazines()
    print('-' * 40)
    main.show_all_books()
except NonBookMagazineException:
    print('Це не журнал або книжка')
except Exception as err:
    print(err)

try:
    main.add('Book1')
except NonBookMagazineException:
    print('Це не журнал або книжка')
except Exception as err:
    print(err)
