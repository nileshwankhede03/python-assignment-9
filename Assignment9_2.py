#2. Write a Python program using multiprocessing. Process to square a list of numbers using multiple processes.

import multiprocessing

def Fun(no):
    return no * no

def main():
    
    Data = list()

    print("Enter the size of List : ")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    Result = []

    p = multiprocessing.Pool()
    Result = p.map(Fun,Data)

    print("output is : ",Result)

if __name__ == "__main__":
    main()