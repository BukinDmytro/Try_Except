#1

class InvalidUsernameError(Exception):
    def __init__(self,username):
        self.username = username

#InvalidSpaceError
#NameIsAlreadyTakenError ДОРОБИТИ ПРИДУМАТИ !!!!!

def register_user(username):
    if len(username) <= 5:
        raise InvalidUsernameError(username)
    else:
        print("Ви успішно зареєструвались !")

#приклад використання

try:
    username = input("Введіть ім'я користувача: ")
    register_user(username)
except InvalidUsernameError:
    print("Недостатньо символів у Вашому імені користувача ! Спробуйте щось інше ")


#2

class InvalidPasswordLength(Exception):
    def __init__(self,password):
        self.password = password

#InvalidSpaceError
#NameIsAlreadyTakenError ДОРОБИТИ ПРИДУМАТИ !!!!!

def register_password(password):
    if len(password) <= 5:
        raise InvalidPasswordLength(password)
    else:
        print("Пароль надійний !")

#приклад використання

try:
    password = input("Введіть пароль : ")
    register_password(password)
except InvalidPasswordLength:
    print("Недостатньо символів у Вашому паролі ! Спробуйте щось інше ")

#3

class InvalidFileFormatError(Exception):
    def __init__(self , filename):
        self.filename = filename

def read_file(filename):
    if ".txt" not in filename:
        raise InvalidFileFormatError(filename)
    else:
        print("Допустимий формат файлу")

try:
    filename = input("Введіть назву файлу з його форматом ( наприклад .txt ):")
    read_file(filename)
except InvalidFileFormatError:
    print("Недопустимий формат файлу !")



