# Task 1
class Employee:

    def __init__(self, firstname : str, lastname, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__salary = salary

    @classmethod
    def from_string(cls, string):
        splitstring = string.split("-")
        return cls(splitstring[0], splitstring[1],splitstring[2])

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def salary(self):
        return self.__salary

emp1 = Employee("Danil", "Ignatushkin", "1000")
emp2 = Employee.from_string("Nikita-Stratiy-2000")

print(emp1.firstname)
print(emp2.firstname)


# Task 2
class Pizza:
    _instances_count = 0

    def __init__(self, ingredientslist):
        self.ingredients = ingredientslist
        Pizza._instances_count +=1
        self.order_number = Pizza._instances_count

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])


# p = Pizza(["Cheese", "Tomato"])
# print(p.ingredients)
# print(p.order_number)
# p1 = Pizza.hawaiian()
# print(p1.ingredients)
# print(p1.order_number)

# Task 3
class Employee:

    # def __init__(self, fullname, salary=None, height=None, nationality=None, subordinates=None):
    #     fullname = fullname.split(" ")
    #     self.name = fullname[0]
    #     self.lastname = fullname[1]
    #     if salary:
    #         self.salary = salary
    #     if height:
    #         self.height = height
    #     if nationality:
    #         self.nationality = nationality
    #     if subordinates:
    #         self.subordinates = subordinates
    def __init__(self, fullname, **kwargs):
        self.name, self.lastname = fullname.split(" ")
        self.__dict__.update(kwargs)
        for k,v in kwargs.items():
            setattr(self, k, v)

# john = Employee("John Doe")
# mary = Employee("Mary Major", salary=120000)
#
# print(john.name)
# print(mary.lastname)
# print(mary.salary)

# Task 4
class Testpaper:

    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    tests_taken = "No tests taken"

    def take_test(self, classsubject, markscheme):
        pass_mark = classsubject.pass_mark.split("%")[0]
        subject = classsubject.subject
        count_question = len(markscheme)
        count = 0

        for i in range(count_question):
            if markscheme[i] == classsubject.markscheme[i]:
                count += 1
        score = count / count_question * 100
        stringscore = str(int(round(score, 0)))

        if score >= int(pass_mark):
            output = "Passed! (" + str(stringscore) + "%)"
        else:
            output = "Failed! (" + str(stringscore) + "%)"

        if self.tests_taken == "No tests taken":
            self.tests_taken = {subject: output}
        else:
            self.tests_taken[subject] = output


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")

student1 = Student()
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])



class Gallows:
    words = []
    game_over = False

    def play(self, word):
        if self.words:
            if word in self.words or word[0] != self.words[-1][-1]:
                self.words.clear()
                self.game_over = True
                return "game over"
            else:
                self.words.append(word)
                return self.words

        else:
            self.words.append(word)
            return self.words

    def restart(self):
        self.game_over = False
        self.words.clear()
        return "game restarted"

game = Gallows()
print(isinstance(game, Gallows))
game.play("apple")
game.play("ear")
game.play("apple")
print(game.words)

