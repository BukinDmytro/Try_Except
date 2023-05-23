#1
'''
class InvalidUrlError(Exception):
    def __init__(self,url):
        self.url = url
def fetch_data_from_url(url):
        if url != "https://www.youtube.com/watch?v=Gs_uBw0CJNk":
            raise InvalidUrlError("Invalid URL:" + url)
        elif "/" not in url:
            raise InvalidUrlError("Something was typed uncorrectly (")
        else:
            print("URL was typed correctly")

try:
    fetch_data_from_url("https://www.youtube.com/watch?v=Gs_uBw0CJNK")
except InvalidUrlError as e:
    print("Error:" , e)
'''
#2

class UserNotFoundError(Exception):
    pass

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            raise UserNotFoundError(f"User '{username}' wasn't found ((")



database = UserDatabase()


user1 = User("dimon", "bukindima222@gmail.com")
user2 = User("vasya", "justvasya222@gmail.com")
database.add_user(user1)
database.add_user(user2)


try:
    user = database.get_user("dimon")
    print(f"Username: {user.username}, Email: {user.email}")
except UserNotFoundError as e:
    print(e)


#3
class TemperatureConverter:
    def celsius_to_fahrenheit(celsius):
        if celsius < -273.15:
            raise ValueError("Absolute 0 ((")
        else:
            return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(fahrenheit):
        if fahrenheit < -459.67:
            raise ValueError("Absolute zero (")
        else:
            return (fahrenheit - 32) * 5/9



converter = TemperatureConverter()


try:
    celsius = 20
    fahrenheit = converter.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")
except ValueError as e:
    print(e)

try:
    fahrenheit = 20
    celsius = converter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius}°C")
except ValueError as e:
    print(e)















