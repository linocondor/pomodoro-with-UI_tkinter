from tkinter import *
import math
from playsound import playsound

#-----------------------SOUNDS

boxing_bell = "boxing-bell-start.mp3" 
campana = "campana.mp3" 


#-----------------------VARIABLES
study_time = NONE
number_of_sessions = NONE
break_time = NONE
counter_sessions = 1

BLACK = "#1A1A1B"
LIGHTBLUE = "#94F3E4"
DARKBLUE = "#37AA9C"
GREY = "#333F44"
FONTNAME = "Helvetica"



#----------------------------------------
##Functions
#take data from user
def get_timer_data():
    global study_time
    global number_of_sessions
    global break_time

    study_time = int(study_time_input.get()) * 60
    number_of_sessions = int(number_of_sessions_input.get()) * 2
    break_time  = int(break_time_input.get()) *60
    
    print(study_time, break_time)

    start_countdown()


def start_countdown():
    
    global number_of_sessions
    global counter_sessions

    #print(number_of_sessions)
    #print(counter_sessions)


    if number_of_sessions <= 0:
        window.after_cancel(timer)
        pomodoro_time_label.config(text="00:00")
        counter_sessions = 1
        print(counter_sessions)


    else:
        if counter_sessions % 2 == 0:
            playsound(campana)
            count_down(break_time)

        else:
            playsound(campana)
            count_down(study_time)


    number_of_sessions -= 1
    counter_sessions += 1

    


#Reset function
def button_reset():
    window.after_cancel(timer)
    
    pomodoro_time_label.config(text="00:00")
    
    global counter_sessions
    counter_sessions = 1



#timer function
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    pomodoro_time_label.config(text=f"{count_min}:{count_sec}")

    #canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        playsound(boxing_bell)
        start_countdown()        
        

    

#-----------------------------------------



window = Tk()
window.config(padx=20, pady=20, bg=BLACK)

#Label - Title Pomodoro Timer
pomodoro_title_label = Label(text="Pomodoro Timer", font=(FONTNAME, 30, "bold"), bg=BLACK, fg=DARKBLUE)
pomodoro_title_label.grid(column=1, row=0)

#Label - Time
pomodoro_time_label = Label(text="00:00", font=(FONTNAME, 30, "bold"), 
bg=BLACK, fg=LIGHTBLUE)
pomodoro_time_label.grid(column=1, row=1)

#Label - Title study time
study_time_label = Label(text="Study Time (min)", font=(FONTNAME, 20, "bold"), bg=BLACK, fg=DARKBLUE)
study_time_label.grid(column=0, row=2)

#Label - Title study time
study_time_label = Label(text="Number of Session", font=(FONTNAME, 20, "bold"), bg=BLACK, fg=DARKBLUE)
study_time_label.grid(column=1, row=2)

#Label - Title study time
study_time_label = Label(text="Break Time (min)", font=(FONTNAME, 20, "bold"), bg=BLACK, fg=DARKBLUE)
study_time_label.grid(column=2, row=2)

#Input - Study time
study_time_input = Entry(width=10, font=(FONTNAME, 10, "bold"), bg=BLACK, fg=LIGHTBLUE)
study_time_input.grid(column=0, row=3)

#Input - Number of sessions
number_of_sessions_input = Entry(width=10, font=(FONTNAME, 10, "bold"), bg=BLACK, fg=LIGHTBLUE)
number_of_sessions_input.grid(column=1, row=3)

#Input - Break Time
break_time_input = Entry(width=10, font=(FONTNAME, 10, "bold"), bg=BLACK, fg=LIGHTBLUE)
break_time_input.grid(column=2, row=3)

#Button - Start Button
start_button = Button(text="Start", command=get_timer_data, font=(FONTNAME, 10, "bold"), bg=BLACK, fg=LIGHTBLUE)
start_button.grid(column=0 ,row=4, pady=10)

#Button - Reset Button
start_button = Button(text="Reset", command= button_reset, font=(FONTNAME, 10, "bold"), bg=BLACK, fg=LIGHTBLUE)
start_button.grid(column=2 ,row=4, pady=10)







window.mainloop()