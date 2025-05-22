# 3. Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a list.
import multiprocessing

def Factorial(number):
    iFact = 1
    for i in range(1,number+1):
        iFact = iFact * i

    return iFact

def main():
    
    Data = []

    print("Enter the size of List : ")
    size = int(input())

    print("Enter the elements in a List : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    p = multiprocessing.Pool()

    Result = []

    Result = p.map(Factorial,Data)

    print("Output is : ",Result)

if __name__ == "__main__":
    main()