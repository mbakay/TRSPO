import random
import threading as th
from unittest import result

def step(n):
    if n % 2 == 1:
        return 3 * n + 1
    else:
        return n / 2

def loop(queue, mutex, results):
    with mutex:
        if(len(queue) == 0):
            return
        value = queue.pop(0)
    while True:
        n = value
        while n != 1:
            n = step(n)
            results[value - 1].append(n)
        with mutex:
            if(len(queue) == 0):
                break
            value = queue.pop(0)

def list_to_str(list):
    str_list = []
    for element in list:
        str_list.append(str(element))
    return str_list

def main():
    amount_of_threads = 10
    N = random.randint(100000, 200000)
    results = []
    for i in range(N):
        results.append([ i + 1])
    queue = list(range(1,N+1))
    threadpool = []
    mutex =  th.Lock()
    for _ in range(amount_of_threads):
        threadpool.append(th.Thread(target = loop, args = (queue, mutex, results)))
    for thread in threadpool:
        thread.start()
    for thread in threadpool:
        thread.join()
    with open("file.txt",'w') as f:
        for result in results:
            f.write(', '.join(list_to_str(result)) + '\n')

if __name__ == "__main__":
    main()
