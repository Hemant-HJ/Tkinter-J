drop_database = 'Drop database if exists hospital;'
create_database =  'Create database hospital;'
use_database = 'Use s109166_ddd;'

doctor_table = """
Create table if not exists doctor (
    name varchar(20) Not Null,
    specialization varchar(30) Not Null,
    Room_no Int
);
"""
patient_table = """
Create table if not exists patient (
    adhar_no Bigint Not Null Primary key,
    Name varchar(20) Not Null,
    Sex varchar(6) Not Null,
    Contact Bigint(10) Not Null,
    Address Varchar(50)
);
"""
appointment_table = """
Create table if not exists appointment (
    adhar_no Bigint Not Null ,
    patient_name Varchar(20) Not Null,
    doctor_name varchar(20) Not Null,
    date timestamp,
    appointment_no int AUTO_INCREMENT  Primary Key
);
"""
insert_into_doctor = """
Insert into doctor values
('asfa','asfasf',12),
('asfa','asdf',1),
('wer','azcv',4)
"""
queries = [drop_database, create_database, use_database, doctor_table, patient_table, appointment_table, insert_into_doctor]

service = [
    (1,'adfgadfg',12),
    (2,'asdfadf',1),
    (3,'fasdfasdf',123)
]

insert_patient = """
Insert into patient
values (%s, %s, %s, %s, %s)
"""

insert_app = """
Insert into appointment (adhar_no, patient_name, doctor_name, date)
values (%s, %s, %s, %s)
"""
modify_pa = """
Update patient
set %s = %s
where adhar_no = %s;
"""