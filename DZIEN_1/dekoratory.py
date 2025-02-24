import time

def pomiar_czasu(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        delta = endtime-starttime
        print(f"czas wykonania funkcji: {delta} s")
    return wrapper

def sleep(func):
    def wrapper():
        time.sleep(3)
        return func()
    return wrapper

@pomiar_czasu
@sleep
def big_list():
    sum([i**5 for i in range(10_000_000)])

big_list()

def repeat(n):
    def wrapper(func):
        def inner(*args):
            for i in range(n):
                func(*args)
        return inner
    return wrapper

@repeat(7)
def calc(c,d):
    print(f"wynik -> {c*d**2}")

calc(2,3)
