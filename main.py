import query
from tkinter import *
from tkinter import ttk
import mysql.connector as sql

connection = sql.connect(
    user = 'u109154_SvCGUADgcx', 
    password = '=oE+Xthivc+B^nGH2O82Ckwo',
    host = '51.161.33.34', 
    database = 's109154_qew'
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
    doctor_b = ttk.Button(frame, text = 'Doctors', command = doctor).place(x = 400, y = 100)

    service_l = ttk.Label(frame, text = 'Click to get all available servies.', font = 'bold')
    service_l.place(x = 100, y = 140)
    service_b = ttk.Button(frame, text = 'Services', command = services).place(x = 400, y = 140)

    regis_l = ttk.Label(frame, text = 'Click here to get registered.', font = 'bold')
    regis_l.place(x = 100, y = 180)
    regis_b = ttk.Button(frame, text = 'Register', command = register).place(x = 400, y = 180)

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
    doctor_level = Toplevel()
    doctor_level.resizable(False, False)
    doctor_level.title('Doctors Available')
    doctor_frame = ttk.Frame(doctor_level)
    doctor_frame.pack()

    select_q = 'Select * from doctor'
    cursor.execute(select_q)

    columns = ('name', 'specialization', 'room_no')
    tree = ttk.Treeview(doctor_frame, columns = columns, show = 'headings')
    tree.heading('name', text = 'Name')
    tree.heading('specialization', text = 'Specialization')
    tree.heading('room_no', text = 'Room No')

    for doc in cursor.fetchall():
        tree.insert('', END, values = doc)

    tree.grid(row = 0, column = 0, sticky = 'nsew')

def services():
    service_level = Toplevel()
    service_level.resizable(False, False)
    service_level.title('Services Available')
    service_frame = ttk.Frame(service_level)
    service_frame.pack()

    columns = ('s_no', 'service', 'room_no')
    tree = ttk.Treeview(service_frame, columns = columns, show = 'headings')
    tree.heading('s_no', text = 'S No.')
    tree.heading('service', text = 'Service')
    tree.heading('room_no', text = 'Room No')

    service = []

    for service in service:
        tree.insert('', END, values = service)

    tree.grid(row = 0, column = 0, sticky = 'nsew')

def register():
    reg_level = Toplevel()
    reg_level.resizable(False, False)
    reg_level.geometry('300x200')
    reg_level.title('Registration')
    reg_frame = ttk.Frame(reg_level)
    reg_frame.pack()

    adhar_var = StringVar()
    name_var = StringVar()
    sex_var = StringVar()
    contact_var = StringVar()
    address_var = StringVar()

    l_adhar = ttk.Label(reg_frame, text = 'Adhar No').place(x = 40, y = 20)
    e_adhar = ttk.Entry(reg_frame, textvariable = address_var).place(x = 60, y = 20)

    l_name = ttk.Label(reg_frame, text = 'Name').place(x = 40, y = 60)
    e_name = ttk.Entry(reg_frame, textvariable = name_var).place(x = 60, y = 60)

    l_sex = ttk.Label(reg_frame, text = 'Sex').place(x = 40, y = 100)
    c_sex = ttk.Combobox(reg_frame)

def appointment():
    pass

def modify():
    pass

def view():
    pass

buttons()

root.mainloop()