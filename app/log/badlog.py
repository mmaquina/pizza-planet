# https://www.freecodecamp.org/news/python-decorators-explained-with-examples/


from datetime import datetime

def log_this(func):

    def wrapper_func():
        print(f'{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}: {func.__name__} is being called')
        to_return = func()
        print(f'{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}: {func.__name__} returned')
        return to_return

    return wrapper_func