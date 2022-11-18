drop_database = 'Drop database if exists hospital;'
create_database =  'Create database hospital;'
use_database = 'hospital;'

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
('Dr.Kumar','Physician',20),
('Dr.K Sanjeev','Pediatrecian',22),
('Dr.Sharma','Orthopaedic surgeon',24),
('Dr.Shikha','Gynaecologist',27),
('Dr.Khan','Neurologist',26),
('Dr.Verma','cardiologist',29),
('Dr.Sia','Opthalmalogist',25),
('Dr.Karan','Dermatologist',32),
('Dr.Singh','physician',35)
"""
queries = [use_database,doctor_table, patient_table, appointment_table, insert_into_doctor]

service = [
    (1,'X-ray',12),
    (2,'CT Scan',11),
    (3,'Blood Collection',13),
    (4,'MRI',14),
    (5,'Dialysis',15),
    (6,'ECG',16),
    (7,'Chemist',17),
    (8,'Ultrasound',19),
    (9,'Lab',10)
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
