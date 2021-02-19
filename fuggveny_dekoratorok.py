
# function decorators - függvény dekoratőrök 1. rész

def valide_div(func):
    def wrapper(value1, value2):
        if value2 == 0:
            return "Can you not divide by Zero"
        return func(value1, value2)
    return wrapper

@valide_div                 # ezzel tudom eltüntetni a Phyton hibaüzenetét, csak az általa írt stringet adja vissza
                            #  hát ezt  -return "Can you not divide by Zero"-
def divide(value1, value2):
    return value1 / value2

print(divide(11, 0))
print(divide(11, 1))
print(divide(11, 2))
print(divide(11, 3))
print(divide(11, 4))


def validate_form(func):
    def wrapper(password, email):
        if len(password) < 6:
            return "Weak password, at least 6 characters"
        if "@" not in email:
            return "Not valid email"
        return func(password, email)
    return wrapper

@validate_form          # ez a parancs nélkül kiirja a rossz variációt is

def form(password, email):
    return "Your password is strong, you have a valid email"

print(form("01234", "zazi"))
print(form("0123456", "zai@hotmail.ho"))
print(form("0123456", "zazi"))