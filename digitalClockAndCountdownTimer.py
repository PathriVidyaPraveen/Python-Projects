# Here are some additional tasks that you can try out.

# Can you create a display box around the digital_clock. We have created one such version - check out the code in the IDE
# Currently - you cannot exit the timer or the clock - it keeps going on for every.
# Can you update the code to accept a user input to exit the digital_clock project?
# Time: |16|41|12| is to be the required output
import time
import sys

def userChoice(choice):
    if choice == "1":
        digital_clock()
    elif choice == "2":
        seconds = int(input("Enter the number of seconds to countdown: "))
        countdown_timer(seconds)
    else:
        print("Invalid choice!")

def digital_clock():
    """Displays a digital clock."""
    while True:
        current_time_hour = time.strftime("%H", time.localtime())
        current_time_minute = time.strftime("%M", time.localtime())
        current_time_sec = time.strftime("%S", time.localtime())
        print("\rDigital Clock: " + '|' + current_time_hour + '|' + current_time_minute + '|' + current_time_sec + '|', end = '')
        time.sleep(1)
    
def countdown_timer(seconds):
    """Counts down from a given number of seconds."""
    print("Countdown Timer started!")
    while seconds > 0:
        print("\rTime remaining: " + str(seconds) + " seconds", end = '')
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")


if __name__ == '__main__':
    while True:
        choice = input("Choose an option (1:Digital Clock, 2:Countdown Timer): ")
        userChoice(choice)