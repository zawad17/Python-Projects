from time import *
import random as r


def mistake(maintest,usertest):
    error = 0
    for i in range(len(maintest)):
        try:
            if maintest[i]!= usertest[i]:
                error=error+1
        except:
            error=error+1
    return error
    
    
def speed_time(start,end,userinput):
    delay = end - start 
    roundtime = round(delay,2)
    speed = len(userinput)/roundtime
    return round(speed)
if __name__ =="__main__":
    
    while True:
        check = input("Want to start your journey? ").lower()
        if check =="yes":
            test = ["Typing speed also can be improved after checking it.","This is the best python typing test program.","I love python programming language."]
            test1 = r.choice(test)
            print("^^^^^^^^^^Typing Speed^^^^^^^^^^")
            print(test1)
            print()
            print()

            time1= time()
            testinput = input("Start typing: ")
            time2=time()

            print("Speed: ",speed_time(time1,time2,testinput),"w/sec")

            print("Error: ",mistake(test1,testinput) )
            
        elif check=="no":
            print("Thank you.")
            break
        else:
            print("Wrong input")    
