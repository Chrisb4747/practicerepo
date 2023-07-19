from datetime import datetime 

def time_function():
 closing_time = datetime.strptime("18:00", "%H:%M") #setting the format for the time 24hour (used from stackoverflow changed to suit my assignment)
 user_time    = datetime.strptime(input("Enter the current time (e.g, 17:00):"), "%H:%M")

 if user_time >= closing_time: #if closing time is 18:00 or later second argument will print
        print("The supermarket is now closed, please wait until tomorrow.")
 else: 
         print("The supermarket is open you may proceed to buying the ingredients!")

#time_function()