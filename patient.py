from models import (Base, session, User, engine)
from sqlalchemy import insert, update, delete
from datetime import datetime
import random


def format_birthday(birthdays):
    birthdays = datetime.strptime(birthdays, '%m/%d/%y').date()
    return birthdays

def format_name(names):
    if names.isalpha():
        name2 = names.split(' ')
        name_format = []
        for name in name2:
            name = name.capitalize()
            name_format.append(name)
        name_format = ' '.join(name_format)
        return name_format
    else:
        while names.isalpha() == False:
            names = input('Please enter name using letters only: ')
        return format_name(names)



def enter_info(names, birthdays):
    patientid = random.randrange(1, 100000)

    while session.query(User).filter(User.patient_id == patientid):
        patientid = random.randrange(1, 100000)

    new_patient = User(ID = patientid, name = names, birthday = birthdays, patient_id = patientid)
    session.add(new_patient)
    session.commit()


def delete_patient(names, birthdays):
    for user in session.query(User).filter(User.name == names, User.birthday == birthdays):
        session.delete(user)
    session.commit()


def search_patient(names, birthdays):
    # names = format_name(names)
    # birthdays = format_birthday(birthdays)
    search_by_option = input('''What do you want to search by? 
                            \r1. Name
                            \r2. Birthday format: MM/DD/YY
                            \r3. Both
                            \r4. Update Information
                            \r''')
    if search_by_option == '1':
        names = f'%{names}%'
        search_results = session.query(User).filter(User.name.like(names)).all()
        for patient in search_results:
            # patient1 = list(patient)
            print(f'''Patient Name: {patient.name}  
                    \rDOB: {patient.birthday}\n''')
    elif search_by_option == '2':
        for patient in session.query(User).filter(User.birthday == birthdays):
            print(patient[0])
    else:
        for patient in session.query(User).filter(User.name == names, User.birthday == birthdays):
            print(f'Name: {patient[0]}')


def app():
    app_options = input('''Select an option below: 
                        \r1. Enter patient info
                        \r2. Search for Patient
                        \r3. Delete Patient 
                        \n''')

    name = input("What is the patient's name?: ")
    birthday = input("What is the patient's birthday? format: MM/DD/YY: ")

    birthday = format_birthday(birthday)
    name = format_name(name)

    if app_options == '1':
        enter_info(name, birthday)
    elif app_options == '2':
        search_patient(name, birthday)
    elif app_options == '3':
        delete_patient(name, birthday)
    else:
        print('Goodbye!')






Base.metadata.create_all(engine)
app()






