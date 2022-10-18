import query
from tkinter import *
from tkinter import ttk
import mysql.connector as sql

connection = sql.connect(

)

if connection.is_connected():
    print('Successfully Connected.')
else:
    print('Connection Error.')

cursor = connection.cursor(buffered = True)

# for que in query.queries:
#     cursor.execute(que)
# connection.commit()

root = Tk()
root.resizable(False, False)
root.geometry('600x500')
root.title('Hospital Management')

def buttons():
    frame = ttk.Frame(root).pack()
    doctor_l = ttk.Label(frame, text = 'Click to get a view of all the doctors.', font = 'bold')
    doctor_l.place(x = 100, y = 100)
    doctor_b = ttk.Button(frame, text = 'Doctors').place(x = 400, y = 100)

    service_l = ttk.Label(frame, text = 'Click to get all available servies.', font = 'bold')
    service_l.place(x = 100, y = 140)
    service_b = ttk.Button(frame, text = 'Services').place(x = 400, y = 140)

    regis_l = ttk.Label(frame, text = 'Click here to get registered.', font = 'bold')
    regis_l.place(x = 100, y = 180)
    regis_b = ttk.Button(frame, text = 'Register').place(x = 400, y = 180)

    appo_l = ttk.Label(frame, text = 'Click here to fix an appointment.', font = 'bold')
    appo_l.place(x = 100, y = 220)
    appo_b = ttk.Button(frame, text = 'Appointment').place(x = 400, y = 220)

    modify_l = ttk.Label(frame, text = 'Click here to modify a existing data.', font = 'bold')
    modify_l.place(x = 100, y = 260)
    modify_b = ttk.Button(frame, text = 'Modify').place(x = 400, y = 260)

    view_l = ttk.Label(frame, text = 'Click here to view all data.', font = 'bold')
    view_l.place(x = 100, y = 300)
    view_b = ttk.Button(frame, text = 'View').place(x = 400, y = 300)

    close_b = ttk.Button(frame, text = 'Close', command = root.destroy).place(x = 500, y = 400)

def doctor():
    pass

def services():
    pass

def register():
    pass

def appointment():
    pass

def modify():
    pass

def view():
    pass

buttons()

root.mainloop()