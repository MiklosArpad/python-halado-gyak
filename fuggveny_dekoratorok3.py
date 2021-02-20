

# function decorators - függvény dekorátorok 3. rész

def validate_form(func):
    def wrapper(password, email):
        if len(password) < 6:
            return ""