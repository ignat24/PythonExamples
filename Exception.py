import re
import cmath

def valid_email(email):
    patternnumber = r"[0-9]"
    patternsimbols = r"[%&$#!()_-]"
    try:
        splitemail = email.split("@")
        if len(splitemail)>2:
            raise ValueError
        if re.search(patternsimbols, email) or re.search(patternnumber, email):
            raise ValueError
        return "Email is valid"


    except ValueError:
        return "Email is not valid!"


# valid_email("trafik@ukr.tel.com")          #output:   "Email is valid"
#
# valid_email("trafik@ukr_tel.com")        #output:   "Email is not valid"
#
# valid_email("tra@fik@ukr.com")           #output:   "Email is not valid"
#
# valid_email("ownsite@our.c0m")

class MyError(ValueError):

    def __init__(self, number):
        print("You input negative number:" + str(number) + ".", end=" ")


def check_positive(number):
    try:
        intnumber = int(number)
        if intnumber < 0:
            raise MyError(str(number))
        else:
            return "You input positive number: " + str(number)
    except MyError as mr:
        return "Try again."
    except ValueError:
        return "Error type: ValueError!"



# print(check_positive(24))      #output:    "You input positive number: 24"
#
# print(check_positive(-19))     #output:     "You input negative number: -19. Try again."
#
# print(check_positive ("38"))    #output:    "You input positive number: 38"
#
# print(check_positive ("abc"))

def divide(numerator, denominator):
    try:
        if denominator == 0:
            string = "Oops, " + str(numerator) + " / " + str(denominator) + " division by zero is error!!!"
            raise ZeroDivisionError(string)
        result = numerator / denominator
        return "Result is " + str(result)


    except ZeroDivisionError as error:
        return error
    except:
        return "Value Error! You did not enter a number!"

# divide(5,0)
# divide

def check_odd_even(number):
    try:
        if number % 2 != 0:
            return "Entered number is even"
        else:return "Entered number is odd"
    except:
        return "You entered incorrect data. Please try again."

# def ToSmallNumberGroupError(number):
#     try:
#         number = int(number)
#         if number < 10:
#             string = "We obtain error: Number of your group can't be less than 10"
#             raise ValueError(string)
#         return "Number of your group " + str(number) + " is valid"
#     except ValueError as vl:
#         return vl
#     except:
#         return "You entered incorrect data. Please try again."
class NumberError(Exception):
    pass

def day_of_week(day):
    week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday" }
    errorday ="There is no such day of the week! Please try again."
    try:
        day = int(day)
        if 0 < day < 7:
            return week[day]
        else:
            raise NumberError(errorday)

    except NumberError as vr:
        return vr

    except:
        return "You did not enter a number! Please try again."


class ZeroDivision(Exception):
    massage = "Zero Division Error"


def solve_complexx(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a == 0 or b == 0 or c == 0:
            raise ZeroDivision
        d = b ** 2 - 4 * a * c
        x1 = "x1=" + str((-b + cmath.sqrt(d)) / (2 * a))
        x2 = "x2=" + str((-b - cmath.sqrt(d)) / (2 * a))
        return "The solution are "+x1 + " and " + x2

    except ZeroDivision:
        return "Zero Division Error"

    except:
        return "Could not convert string to float"

# print(solve_complexx(1,5,6))


class ToSmallNumberGroupError(Exception):
    pass


def check_number_group(number):
    try:
        floatnumber = float(number)
        if floatnumber < 10:
            raise ToSmallNumberGroupError()
        return f"Number of your group {number} is valid"
    except ToSmallNumberGroupError:
        return "We obtain error: Number of your group can't be less than 10 "
    except:
        return "You entered incorrect data. Please try again."

print(check_number_group(75))



