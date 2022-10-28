import query
from tkinter import *
from tkinter import ttk
import mysql.connector as sql
import datetime
import json

root = Tk()

def load():
    with open('variable.json', mode = 'r') as file:
        return json.load(file)

file_data = load()

connection = False
username = StringVar()
password = StringVar()
host = StringVar()

def write():
    try:
        connection = sql.connect(
            user = username.get(),
            password = password.get(),
            host = host.get()
        )
        changed_data = {
            'username': username.get(),
            'password': password.get(),
            'host': host.get()
        }
        with open('variable.json', mode = 'w') as file:
            file_data.update(changed_data)
            json.dump(file_data, file, indent = 4)
    except sql.Error as e:
        print(e)

if file_data['started'] == False:
    frame = ttk.Frame(root)
    frame.pack()

    l_username = ttk.Label(frame, text = 'Username').pack()
    e_username = ttk.Entry(frame, textvariable = username).pack()

    l_pass = ttk.Label(frame, text = 'Password').pack()
    e_pass = ttk.Entry(frame, textvariable = password).pack()

    l_host = ttk.Label(frame, text = 'Host').pack()
    e_host = ttk.Entry(frame, textvariable = host).pack()

    confirm = ttk.Button(frame, text = 'Confirm', command = write).pack()
    root.mainloop()

else:
    connection = sql.connect(
        user = file_data['username'], 
        password = file_data['password'],
        host = file_data['host'],
        database = 'hospital'
    )

if connection.is_connected():
    print('Successfully Connected.')
else:
    print('Connection Error.')

cursor = connection.cursor(buffered = True)

for que in query.queries:
    cursor.execute(que)
connection.commit()

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
    appo_b = ttk.Button(frame, text = 'Appointment', command = appointment).place(x = 400, y = 220)

    modify_l = ttk.Label(frame, text = 'Click here to modify a existing data.', font = 'bold')
    modify_l.place(x = 100, y = 260)
    modify_b = ttk.Button(frame, text = 'Modify', command = modify).place(x = 400, y = 260)

    view_l = ttk.Label(frame, text = 'Click here to view all data.', font = 'bold')
    view_l.place(x = 100, y = 300)
    view_b = ttk.Button(frame, text = 'View', command = view).place(x = 400, y = 300)

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

    service = query.service

    for service in service:
        tree.insert('', END, values = service)

    tree.grid(row = 0, column = 0, sticky = 'nsew')

def register():
    def confirm():
        data = [int(adhar_var.get()), name_var.get(), sex_var.get(), int(contact_var.get()), address_var.get()]
        insert_query = query.insert_patient

        cursor.execute(insert_query, data)
        connection.commit()
        reg_level.destroy()

    reg_level = Toplevel()
    reg_level.resizable(False, False)
    reg_level.geometry('400x300')
    reg_level.title('Registration')
    reg_frame = ttk.Frame(reg_level)
    reg_frame.pack()

    adhar_var = StringVar()
    name_var = StringVar()
    sex_var = StringVar()
    contact_var = StringVar()
    address_var = StringVar()

    l_adhar = ttk.Label(reg_frame, text = 'Adhar No').pack() # place(x = 40, y = 20)
    e_adhar = ttk.Entry(reg_frame, textvariable = adhar_var).pack() # place(x = 60, y = 20)

    l_name = ttk.Label(reg_frame, text = 'Name').pack() # place(x = 40, y = 60)
    e_name = ttk.Entry(reg_frame, textvariable = name_var).pack() # place(x = 60, y = 60)

    l_sex = ttk.Label(reg_frame, text = 'Sex').pack() # place(x = 40, y = 100)
    c_sex = ttk.Combobox(reg_frame, textvariable = sex_var)
    c_sex['state'] = 'readonly'
    c_sex['values'] = ['male', 'female']
    c_sex.pack()

    l_contact = ttk.Label(reg_frame, text = 'Contact').pack()
    e_contact = ttk.Entry(reg_frame, textvariable = contact_var).pack()

    l_address = ttk.Label(reg_frame, text = 'Address').pack()
    e_address = ttk.Entry(reg_frame, textvariable = address_var).pack()

    b_confirm = ttk.Button(reg_frame, text = 'Confirm', command = confirm).pack()

def appointment():
    def confirm():
        data = [int(adhar_var.get()), name_var.get(), doctor_var.get(), datetime.datetime.now()]
        insert_query = query.insert_app

        cursor.execute(insert_query, data)
        connection.commit()
        app_level.destroy()

    app_level = Toplevel()
    app_level.geometry('300x200')
    app_level.title('Appointment')
    app_level.resizable(False, False)
    app_frame = ttk.Frame(app_level)
    app_frame.pack()

    adhar_var = StringVar()
    name_var = StringVar()
    doctor_var = StringVar()

    l_adhar = ttk.Label(app_frame, text = 'Adhar No').pack() # place(x = 40, y = 20)
    e_adhar = ttk.Entry(app_frame, textvariable = adhar_var).pack() # place(x = 60, y = 20)

    l_name = ttk.Label(app_frame, text = 'Name').pack() # place(x = 40, y = 60)
    e_name = ttk.Entry(app_frame, textvariable = name_var).pack() # place(x = 60, y = 60)

    l_doctor = ttk.Label(app_frame, text = 'doctor').pack() # place(x = 40, y = 100)
    c_doctor = ttk.Combobox(app_frame, textvariable = doctor_var)
    c_doctor['state'] = 'readonly'
    cursor.execute('Select name from doctor;')
    doctor_name = []
    for tup in cursor.fetchall():
        doctor_name.append(tup[0])
    doctor_name = ['abc', 'adaf', 'asdf', 'asdfasdf', 'asdfadf']
    c_doctor['values'] = doctor_name
    c_doctor.pack()

    b_confirm = ttk.Button(app_frame, text = 'Confirm', command = confirm).pack()

def modify():
    def confirm():
        changed_data = changed_var.get()
        if field_var.get().lower() in ('adhar_no', 'contact'):
            change_data = int(changed_var.get())
        data = [changed_data]
        mod_query = f"""
        Update patient
        set {field_var.get()} = %s
        where adhar_no = {int(adhar_var.get())}        
        """
        cursor.execute(mod_query, data)
        connection.commit()
        mod_level.destroy()

    mod_level = Toplevel()
    mod_level.resizable(False, False)
    mod_level.geometry('300x200')
    mod_level.title('Modify')
    mod_frame = ttk.Frame(mod_level)
    mod_frame.pack()

    adhar_var = StringVar()
    field_var = StringVar()
    changed_var = StringVar()

    l_adhar = ttk.Label(mod_frame, text = 'Adhar No').pack() # place(x = 40, y = 20)
    e_adhar = ttk.Entry(mod_frame, textvariable = adhar_var).pack() # place(x = 60, y = 20)

    l_field = ttk.Label(mod_frame, text = 'The Field you want to change.', font = 'bold').pack()
    c_field = ttk.Combobox(mod_frame, textvariable = field_var)
    c_field['state'] = 'readonly'
    c_field['values'] = ['Adhar_No', 'Name', 'Sex', 'Contact', 'Address']
    c_field.pack()

    l_ch_field = ttk.Label(mod_frame, text = 'New Value').pack()
    e_ch_field = ttk.Entry(mod_frame, textvariable = changed_var).pack()

    b_confirm = ttk.Button(mod_frame, text = 'Confirm', command = confirm).pack()

def view():
    view_level = Toplevel()
    view_level.resizable(False, False)
    view_level.title('Details')

    pati_f = ttk.Frame(view_level)
    app_f = ttk.Frame(view_level)

    pati_f.grid(row = 0, column = 0)
    app_f.grid(row = 1, column = 0)

    l_pati = ttk.Label(pati_f, text = 'Patients').pack()
    l_app = ttk.Label(app_f, text = 'Appointments').pack()

    columns = ('adhar_no', 'name', 'sex', 'contact', 'address')
    t_pati = ttk.Treeview(pati_f, columns = columns, show = 'headings')
    t_pati.heading('adhar_no', text = 'Adhar No')
    t_pati.heading('name', text = 'Name')
    t_pati.heading('sex', text = 'Sex')
    t_pati.heading('contact', text = 'Contact')
    t_pati.heading('address', text = 'Address')

    cursor.execute('Select * from patient;')
    for entry in cursor.fetchall():
        print(entry)
        t_pati.insert('', END, values = entry)

    t_pati.pack()

    colums = ('adhar_no', 'pname', 'dname', 'date', 'apno')
    t_app = ttk.Treeview(app_f, columns = colums, show = 'headings')
    t_app.heading('adhar_no', text = 'Adhar No')
    t_app.heading('pname', text = 'Patient Name')
    t_app.heading('dname', text = 'Doctor Name')
    t_app.heading('date', text = 'Date')
    t_app.heading('apno', text = 'Appointment No')

    cursor.execute('Select adhar_no, patient_name, doctor_name, DATE(date), appointment_no from appointment;')
    for entry in cursor.fetchall():
        t_app.insert('', END, values = entry)

    t_app.pack()

buttons()

root.mainloop()