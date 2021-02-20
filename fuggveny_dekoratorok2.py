# function decorators - függvény dekorátorok 2. rész


def validate_email(func):
    def wrapper(email, password):
        if '@' not in email:
            return "Not valid email"
        return func(email, password)

    return wrapper


def validate_password(func):
    def wrapper(email, password):
        if len(password) < 6:
            return "Weak password, at least 6 characters"
        return func(email, password)

    return wrapper


# itt lehet több dekorátort is magadni mint kettő

@validate_email
@validate_password
def form(email, password):
    return "Your password is strong and you have a valid email"


print(form("zazi", "1234567"))
print(form("zazi@mail.hu", "1234567"))
print(form("zazi@mail.hu", "123"))
