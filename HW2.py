from threading import Thread, Lock
import random
import time

def measure_function_time(function):
    def inner(*agrs, **kwargs):
        start = time.time()
        result = function(*agrs, **kwargs)
        end = time.time()
        print(f"Time: {end - start}s")
        return result
    return inner
    
class Number1:
    def __init__(self):
        self.__number = float()
        self.lock = Lock()
    
    def get_number(self):
        return self.__number
    
    def set_number(self, value):
        self.lock.acquire()
        try:
            self.__number = value
        finally:
            self.lock.release()
    
    def increase_number(self, value):
        self.lock.acquire()
        try:
            self.__number += value
        finally:
            self.lock.release()

class Number2:
    def __init__(self):
        self.__number = float()
        self.lock = Lock()
    
    def get_number(self):
        return self.__number
    
    def set_number(self, value):
        self.lock.acquire()
        try:
            self.__number = value
        finally:
            self.lock.release()
    
    def increase_number(self, value):
        self.lock.acquire()
        try:
            self.__number += value
        finally:
            self.lock.release()

def increase1(number1, number2):
    for _ in range(random.randint(10000, 20000)):
        number1.increase_number(random.random())
        number2.increase_number(random.random())

def increase2(number1, number2):
    for _ in range(random.randint(10000, 20000)):
        number2.increase_number(random.random())
        number1.increase_number(random.random())

@measure_function_time
def main():
    number1 = Number1()
    number2 = Number2()
    number_of_threads = random.randint(0, 5) + 5
    print(f"Starts {number_of_threads*2} threads")
    thread_pool = []
    for _ in range(number_of_threads):
        thread_pool.append(Thread(target = increase1, args = (number1, number2)))
        thread_pool.append(Thread(target = increase2, args = (number1, number2)))
    for thread in thread_pool:
        thread.start()
    for thread in thread_pool:
        thread.join()
    print(f"Number in first class = {number1.get_number()}")
    print(f"Number in second class = {number2.get_number()}")

if __name__ == "__main__":
    main()
