#CountDownTimer

import time

# time.sleep(3) # this is an example on how sleep work in the time function, it works as a timer that delays when the the print statement will be seen
# print("times up")

the_timer = int(input("Enter the time in seconds: "))

#for counter in range(the_timer, 0, -1):
#    seconds = counter % 60
#    minutes =  int(counter / 60) % 60
#    hours = int(counter / 3600) % 24
#    days = int(counter / 86400)  # 1 day = 86400 seconds
#    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}") # the variable counter behavs like a counter and printing it makes it visible 
#    time.sleep(1)

while the_timer > 0:
    seconds = counter % 60
    minutes =  int(counter / 60) % 60
    hours = int(counter / 3600) % 24
    days = int(counter / 86400)  # 1 day = 86400 seconds


print("Wake up!")