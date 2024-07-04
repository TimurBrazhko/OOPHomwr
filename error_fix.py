# git принципы ООП 4 штуки 1.Наследование 2. Полиморфизм -> (все внутренности род класса)
# Инкапсуляция, Абстракция

# супер класс/ родительский класс

class Books:

    price = 350

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} \nАвтор: {self.author}\n"

book1=Books("Преступление и наказание", 'Достоевский')
print(book1)

book2=Books('этоМИр', 'beka')
print(book2)

# Дочерний класс
class Manga(Books):
    #полиморфизм
    price = 600

    def __init__(self, title, author, image='default.jpg'):
        # Books.__init__(self, title, author)
        super().__init__(title, author)
        self.image = image

    def reverse(self):
        print('читай справа налево')

    def __str__(self):
        return f'{super().__str__()}\n{self.image}'

manga1=Manga('berzerk', 'miyra')
print(manga1)

# DRY

class Anime(Manga):
    def __init__(self, title, author, drive_image):
        super().__init__(title, author)
        self.drive_image = drive_image


anime_1 = Anime('Naruto', 'kisimoto','24')
print(anime_1)
