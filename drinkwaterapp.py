import tkinter as tk
from tkinter import messagebox
from plyer import notification
from playsound import playsound
import time
import threading
#global flag to control reminder lopp
reminder_running=False

def start_reminder():
    global reminder_running
    try:
        minutes=int(entry.get())
        interval=minutes*60

    except ValueError:
        messagebox.showerror('invalid input','please enter a valid number.')
        return
    if reminder_running:
        messagebox.showinfo('already running','the reminder is already running.')
        return

    reminder_running=True

    def remind_loop():
        while reminder_running:
            playsound('C:/python/its-time-to-drink-water.mp3')
            notification.notify(
                title='drink water reminder',
                message='time to drink water',
                timeout=15
            )
            for _ in range(interval):
                if not reminder_running:
                    break
                time.sleep(1)

            

    #run in background thread so gui doesnt frezze
    threading.Thread(target=remind_loop,daemon=True).start()
    messagebox.showinfo('started',f'reminder set every {minutes} minute(s).')

def stop_reminder():
    global reminder_running
    if reminder_running:
        reminder_running=False
        messagebox.showinfo('stopped','the reminder has been stopped .')
    else:
        messagebox.showinfo('not running','no reminder is currently running.')
        

root=tk.Tk()
root.title('water reminder')
root.geometry('300x200')

label=tk.Label(root,text='remind me every (mintues)',font=('Arial',12))
label.pack(pady=20)

entry=tk.Entry(root,font=('Arial',12))
entry.pack(pady=10)

start_button=tk.Button(root,text='start reminder',font=('Arial',12),command=start_reminder)
start_button.pack(pady=10)

stop_button=tk.Button(root,text='stop reminder',font=('Arial',12),command=stop_reminder)
stop_button.pack(pady=10)

root.mainloop()


                
