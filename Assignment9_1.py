import threading , time

def Display1(number):
    for i in range(1,number + 1):
        print("Display 1 from Thread 1 : ",i)
        time.sleep(1.0)
        

def Display2(number):
    for i in range(1,number + 1):
        print("Display 2 from Thread 2 : ",i) 
        time.sleep(1.0)

def Display3(number):
    for i in range(1,number + 1):
        print("Display 3 from Thread 3 : ",i) 
        time.sleep(1.0)

def main(): 
    Thread1 = threading.Thread(target = Display1 , args = (5,))
    Thread2 = threading.Thread(target = Display2 , args = (5,))
    Thread3 = threading.Thread(target = Display3 , args = (5,))

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

    print("Exit of main ")

if __name__ == "__main__":
    main()
