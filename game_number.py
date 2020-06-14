import abc
from random import randrange

# Реализация фабричного метода


class IShare(abc.ABC):

    abc.abstractmethod

    def get_perimeter(self):
        pass

    abc.abstractmethod

    def get_area(self):
        pass

    abc.abstractmethod

    def get_description(self):
        pass


class Circle(IShare):
    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def get_perimeter(self):
        return 2 * self.__class__.PI * self.__radius

    def get_area(self):
        return self.__class__.PI * self.__radius ** 2

    def get_description(self):
        return f'Я окружность с радиусом {self.__radius}'


class Rectangle(IShare):
    PI = 3.14

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    width = property(get_width)

    @property
    def height(self):
        return self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_area(self):
        return self.width * self.__height

    def get_description(self):
        return f'Я прямоугольник с высотой {self.__height} и шириной {self.width}'


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def get_description(self):
        return f'Я квадрат со строной {self.width}'


class Game:
    QUESTION_COUNT = 2

    def __init__(self):
        raise Exception('Нельзя создать экземпляр класса')

    @staticmethod
    # рандомный выбор фигуры
    def __get_share():
        type = randrange(3)
        if type == 0:
            return Circle(randrange(1, 10))
        if type == 1:
            return Rectangle(randrange(1, 10), randrange(1, 10))
        if type == 2:
            return Square(randrange(1, 10))

    @staticmethod
    # string - что считаем и answer - ответ
    def __calculate(string, answer):  
        while True:
            guess = input(f'Укажите {string} : ').strip()
            if not guess.replace('.', '', 1).isdigit():
                print('Введите число!')
                continue
            break
        if float(guess) == answer:
            print('Вы дали правильный ответ')
        else:
            print(f'Ошибка! Правильный ответ {answer}!')

    @classmethod
    def __run(cls):
        # получаем сгенереированный вопрос
        share = cls.__get_share()
        if isinstance(share, IShare):
            print(share.get_description())
            cls.__calculate('площадь', share.get_area())
            cls.__calculate('периметр', share.get_perimeter())
        else:
            raise TypeError('Неизвестная фигура!')

    @classmethod
    # вход в игру
    def play(cls):
        print(
            f'Привет! Мы геометрические фигуры и у нас есть {cls.QUESTION_COUNT} вопроса.')
        while True:
            is_game_over = input('Играем? Y/N:').strip()
            if is_game_over.upper() == 'N':
                break
            cls.__run()
        print('Спасибо за участие!')


Game.play()
