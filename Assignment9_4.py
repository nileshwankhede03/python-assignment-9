# 4. Create a Python program that Compare execution time of summing numbers from 1 to 10 million using normal function, threading, and multiprocessing.
import time
import threading
import multiprocessing

def Addition():
    sum = 0
    for i in range(1,10000000):
        sum = sum + i
    
    print(sum)

def main():
    start_time1 = time.time()
    Addition()
    end_time1 = time.time()
    print("Total execution time of normal function : ",end_time1 - start_time1)


    start_time2 = time.time()
    Thread1 = threading.Thread(target = Addition)
    Thread1.start()
    Thread1.join()
    end_time2 = time.time()
    print("Total execution time of Thread is : ",end_time2 - start_time2)


    start_time3 = time.time()
    Process1 = multiprocessing.Process(target = Addition)
    Process1.start()
    Process1.join()
    end_time3 = time.time()
    print("Total execution time of using Multi-Processing is : ",end_time2 - start_time2)

    print("Exit of main ")

if __name__ == "__main__":
    main()