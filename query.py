drop_database = 'Drop database if exists hospital;'
create_database =  'Create database hospital;'
use_database = 'Use hospital;'

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
    Sex char(1) Not Null,
    Contact Bitint(10) Not Null,
    Address Varchar(50)
);
"""
appointment_table = """
Create table if not exists appointment (
    adhar_no Bitint Not Null Primary Key,
    patient_name Varchar(20) Not Null,
    doctor_name varchar(20) Not Null,
    date timestamp,
    appointment_no int 
);
"""
insert_into_doctor = """
Insert into doctor values
"""
queries = [drop_database, create_database, use_database, doctor_table, patient_table, appointment_table, insert_into_doctor]