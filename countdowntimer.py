import time 
num = input("Enter the value in seconds:")

def countdown(seconds):
    while seconds >0 :
     min = int(seconds/60)
     sec = int(seconds%60)

     timer = f'{min}:{sec}'

     print(timer)
     time.sleep(1)
     
     seconds-=1
    print("Times up")

countdown(int(num))