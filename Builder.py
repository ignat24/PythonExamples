from abc import ABC, abstractmethod


class Auto:
    def __init__(self):
        self.comfort = False
        self.premium = False
        self.sport = False
        self.options = []

    def __str__(self):
        string = ""
        if self.comfort:
            string += "Equipment comfort"
        if self.premium:
            string += "Equipment premium"
        if self.sport:
            string += "Equipment sport"
        if self.options:
            string += "\nOptions:"
            for option in self.options:
                string += str(option)
        return string


class BlackColor:
    def __str__(self):
        return "Black color"


class RedColor:
    def __str__(self):
        return "Red color"


class WhiteColor:
    def __str__(self):
        return "White color"


class CruiseControl:
    def __str__(self):
        return ", Cruise control"


class Display:
    def __str__(self):
        return ", Multimedia"


class ClimateControl:
    def __str__(self):
        return ", Climate control"


class Turbine:
    def __str__(self):
        return ", +50Hp"


class CarConfigBuilder(ABC):

    @abstractmethod
    def create_config(self):
        pass

    @abstractmethod
    def add_options(self):
        pass

    @abstractmethod
    def get_car(self):
        pass


class CarBuilderComfort(CarConfigBuilder):

    def __init__(self):
        self.car = Auto()

    def create_config(self):
        self.car.comfort = True

    def add_options(self):
        self.car.options.append(WhiteColor())
        self.car.options.append(CruiseControl())

    def get_car(self):
        return self.car


class CarBuilderPremium(CarConfigBuilder):

    def __init__(self):
        self.car = Auto()

    def create_config(self):
        self.car.premium = True

    def add_options(self):
        self.car.options.append(BlackColor())
        self.car.options.append(CruiseControl())
        self.car.options.append(Display())
        self.car.options.append(ClimateControl())

    def get_car(self):
        return self.car


class CarBuilderSport(CarConfigBuilder):

    def __init__(self):
        self.car = Auto()

    def create_config(self):
        self.car.sport = True

    def add_options(self):
        self.car.options.append(RedColor())
        self.car.options.append(Display())
        self.car.options.append(ClimateControl())
        self.car.options.append(Turbine())


    def get_car(self):
        return self.car



carComfort = CarBuilderComfort()
carComfort.create_config()
carComfort.add_options()
print(carComfort.get_car(),"\n")

carPremium = CarBuilderComfort()
carPremium.create_config()
carPremium.add_options()
print(carPremium.get_car(),"\n")

carSport = CarBuilderComfort()
carSport.create_config()
carSport.add_options()
print(carSport.get_car(),"\n")

print("With Director")


class Director:

    def create_comfort_car(self, builder):
        builder.create_config()
        builder.add_options()
        print(builder.get_car(),"\n")

    def create_premium_car(self, builder):
        builder.create_config()
        builder.add_options()
        print(builder.get_car(),"\n")

    def create_sport_car(self, builder):
        builder.create_config()
        builder.add_options()
        print(builder.get_car(),"\n")


manager = Director()
comfortCar = CarBuilderComfort()
premiumCar = CarBuilderPremium()
sportCar = CarBuilderSport()

manager.create_comfort_car(comfortCar)
manager.create_premium_car(premiumCar)
manager.create_sport_car(sportCar)




# class Builder(ABC):
#
#     def draw_line(self):
#         pass
#
#     def draw_rectangle(self):
#         pass
#
#     def draw_text(self):
#         pass
#
#     def draw_picture(self):
#         pass
#
#
# class Graphic(ABC):
#
#     def draw(self):
#         pass
#
#
# class DrawPicture:
#
#     def __init__(self, line, rectangle, text):
#         self.line = line
#         self.rectangle = rectangle
#         self.text = text
#
#     def draw_picture(self):
#         self.line.draw()
#         self.rectangle.draw()
#         self.text.draw()
#
#
#
#
# class Line(Graphic):
#
#     def draw(self):
#         print("- Line")
#
#
# class Rectangle(Graphic):
#
#     def draw(self):
#         print("- Rectangle")
#
#
# class Text(Graphic):
#
#     def draw(self):
#         print("- Text")
#
#
# class DrawPictureBuilder(Builder):
#
#     def draw_line(self):
#         return Line()
#
#     def draw_rectangle(self):
#         return Rectangle()
#
#     def draw_text(self):
#         return Text()
#
#     def create_picture(self):
#         line = self.draw_line()
#         rectangle = self.draw_rectangle()
#         text = self.draw_text()
#         return DrawPicture(line, rectangle, text)
#
#
# picture = DrawPictureBuilder()
# crPicture = picture.create_picture()
# crPicture.draw_picture()
#
#




# class Graphic:
#
#     def draw(self):
#         pass
#
#     def add(self, obj):
#         pass
#
#     def get_child(self, index):
#         pass
#
#
# class Line(Graphic):
#
#     def draw(self):
#         print("- Line")
#
#
# class Rectangle(Graphic):
#
#     def draw(self):
#         print("- Rectangle")
#
#
# class Text(Graphic):
#
#     def draw(self):
#         print("- Text")
#
#
# class Picture(Graphic):
#
#     def __init__(self):
#         self._children = []
#
#     def draw(self):
#         for obj in self._children:
#             obj.draw()
#
#     def add(self, obj):
#         if isinstance(obj, Graphic) and not obj in self._children:
#             self._children.append(obj)
#
#     def get_child(self, index):
#         return self._children[index]
#
#
#
#
# picture = Picture()
# picture.add(Line())
# picture.add(Rectangle())
# picture.add(Text())
# picture.draw()
#
#
# print("\n")
# line = picture.get_child(0)
# line.draw()
#
