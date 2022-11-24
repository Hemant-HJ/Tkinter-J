import query
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as sql
import json

def load():
    with open('variable.json', mode = 'r') as file:
        return json.load(file)

file_data = load()

if file_data['started'] == False:
    
    def config():
        def write():
            try:
                connection = sql.connect(
                    user = username.get(),
                    password = password.get(),
                    host = host.get()
                )
                cursor = connection.cursor(buffered = True)

                for que in query.queries:
                    cursor.execute(que)
                    connection.commit()
                
                changed_data = {
                    'username': username.get(),
                    'password': password.get(),
                    'host': host.get(),
                    'started': True
                }
                with open('variable.json', mode = 'w') as file:
                    file_data.update(changed_data)
                    json.dump(file_data, file, indent = 4)

                messagebox.showinfo(title = 'Success', message = 'Databases have been created.\nPlease restart the application.')

                droot.destroy()
            except sql.Error as e:
                print(e)
        droot = Tk()

        username = StringVar()
        password = StringVar()
        host = StringVar()
        droot.title('Configuration')
        droot.geometry('300x200')
        droot.resizable(False, False)
        dframe = ttk.Frame(droot)
        dframe.pack()

        l_config = ttk.Label(dframe, text = 'Configuration', font = 'bold', anchor = CENTER).pack()

        l_username = ttk.Label(dframe, text = 'Username').pack()
        e_username = ttk.Entry(dframe, textvariable = username).pack()

        l_pass = ttk.Label(dframe, text = 'Password').pack()
        e_pass = ttk.Entry(dframe, textvariable = password, show = '*').pack()

        l_host = ttk.Label(dframe, text = 'Host').pack()
        e_host = ttk.Entry(dframe, textvariable = host).pack()

        confirm = ttk.Button(dframe, text = 'Confirm', command = write).pack()
        droot.mainloop()
    config()
else:
    connection = sql.connect(
        user = file_data['username'], 
        password = file_data['password'],
        host = file_data['host'],
        database = 's109154_qew'
    )

    if connection.is_connected():
        print('Successfully Connected.')
    else:
        print('Connection Error.')

    cursor = connection.cursor(buffered = True)

    root = Tk()
    root.resizable(False, False)
    root.geometry('600x500')
    root.title('Hospital Management')
    f_style = ttk.Style(root).configure('Frame.TFrame', background = 'black')
    

    def buttons():
        frame = ttk.Frame(root, style = 'Frame.TFrame').pack()
        b_style = ttk.Style(root).theme_use('classic')    
        l_style = ttk.Style(root).configure('TLabel', font = ('Helvetica', 30))
        bu_style = ttk.Style(root).configure('TButton', font = ('Helvetica', 13), foreground = 'black', background = 'lightblue')
        cl_style = ttk.Style(root).configure('Close.TButton', font = ('Helvetica', 13), background = 'red')
    
        l_main = ttk.Label(frame, text = 'Hostpital Management', anchor = CENTER).pack()

        doctor_l = ttk.Label(frame, text = 'Doctors List', font = 'bold')
        doctor_l.place(x = 100, y = 100)
        doctor_b = ttk.Button(frame, text = 'Doctors', command = doctor).place(x = 400, y = 100)

        service_l = ttk.Label(frame, text = 'Service List', font = 'bold')
        service_l.place(x = 100, y = 140)
        service_b = ttk.Button(frame, text = 'Services', command = services).place(x = 400, y = 140)

        regis_l = ttk.Label(frame, text = 'Register', font = 'bold')
        regis_l.place(x = 100, y = 180)
        regis_b = ttk.Button(frame, text = 'Register', command = register).place(x = 400, y = 180)

        appo_l = ttk.Label(frame, text = 'Appointment', font = 'bold')
        appo_l.place(x = 100, y = 220)
        appo_b = ttk.Button(frame, text = 'Appointment', command = appointment).place(x = 400, y = 220)

        modify_l = ttk.Label(frame, text = 'Modify', font = 'bold')
        modify_l.place(x = 100, y = 260)
        modify_b = ttk.Button(frame, text = 'Modify', command = modify).place(x = 400, y = 260)

        view_l = ttk.Label(frame, text = 'View', font = 'bold')
        view_l.place(x = 100, y = 300)
        view_b = ttk.Button(frame, text = 'View', command = view).place(x = 400, y = 300)

        close_b = ttk.Button(frame, text = 'Close', command = root.destroy, style = 'Close.TButton').place(x = 500, y = 400)

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
            messagebox.showinfo(title = 'Success', message = 'User Successfully Registed.')
            reg_level.destroy()

        reg_level = Toplevel()
        reg_level.resizable(False, False)
        reg_level.geometry('400x300')
        reg_level.title('Registration')

        b_style = ttk.Style(reg_level).theme_use('classic')    
        l_style = ttk.Style(reg_level).configure('TLabel', font = ('Helvetica Bold', 15))
        bu_style = ttk.Style(reg_level).configure('TButton', font = ('Helvetica', 13), foreground = 'black', background = 'lightblue')
        cl_style = ttk.Style(reg_level).configure('Ok.TButton', font = ('Helvetica', 13), background = 'green')

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

        b_confirm = ttk.Button(reg_frame, text = 'Confirm', command = confirm, style = 'Ok.TButton').pack()

    def appointment():
        def confirm():
            data = [int(adhar_var.get()), name_var.get(), doctor_var.get()]
            insert_query = query.insert_app

            cursor.execute(insert_query, data)
            connection.commit()
            messagebox.showinfo(title = 'Success', message = 'Appoinment Added.')
            app_level.destroy()

        app_level = Toplevel()
        app_level.geometry('300x200')
        app_level.title('Appointment')
        app_level.resizable(False, False)

        b_style = ttk.Style(app_level).theme_use('classic')    
        l_style = ttk.Style(app_level).configure('TLabel', font = ('Helvetica Bold', 15))
        bu_style = ttk.Style(app_level).configure('TButton', font = ('Helvetica', 13), foreground = 'black', background = 'lightblue')
        cl_style = ttk.Style(app_level).configure('Ok.TButton', font = ('Helvetica', 13), background = 'green')

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
        c_doctor['values'] = doctor_name
        c_doctor.pack()

        b_confirm = ttk.Button(app_frame, text = 'Confirm', command = confirm, style = 'Ok.TButton').pack()

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
            messagebox.showinfo(title = 'Success', message = 'Patient Successfully Varified.')
            mod_level.destroy()

        mod_level = Toplevel()
        mod_level.resizable(False, False)
        mod_level.geometry('300x200')
        mod_level.title('Modify')

        b_style = ttk.Style(mod_level).theme_use('classic')    
        l_style = ttk.Style(mod_level).configure('TLabel', font = ('Helvetica Bold', 15))
        bu_style = ttk.Style(mod_level).configure('TButton', font = ('Helvetica', 13), foreground = 'black', background = 'lightblue')
        cl_style = ttk.Style(mod_level).configure('Ok.TButton', font = ('Helvetica', 13), background = 'green')

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

        b_confirm = ttk.Button(mod_frame, text = 'Confirm', command = confirm, style = 'Ok.TButton').pack()

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