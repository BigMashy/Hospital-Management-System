from Main import main
from Doctor import Doctor
from Patient import Patient

class Admin:
    
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')
    def get_admin():
        
        admin = Admin('admin','123','B1 1AB')
        return admin
    #def get_admin(cls):
     #  admin = cls('admin', '123', 'B1 1AB')
      # return [admin]
    def login(self):
        print("-----Login-----")
        u = input('Enter the username: ')
        p = input('Enter the password: ')

        # Call the main function to get the list of objects
        
        admins = Admin.get_admin()
        for admin in admins:
            if u == admin.get_username() and p == admin.get_password():
                print("Access Granted!")
                return u
            print("Access Denied")

        print("Access Denied")
        
        # check if the username and password match the registered ones
        #To
        

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        fn=input("Doctor first name: ")
        ln=input("Doctor surname: ")
        spec=input("Speciality: ")
        self.__fn
        self.__ln
        self.__spec
        return fn,ln,spec
        
        #ToDo2
        

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op=input("Choice: ")
        


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            fn = input("Doctor first name: ")
            ln = input("Doctor surname: ")
            spec = input("Speciality: ")
            self.__main=self.__fn,self.__ln,self.__spec
            return fn, ln, spec
            # check if the name is already registered
            
            for doctor in main:
                if self.__fn == Doctor.get_first_name() and self.__ln == Doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    break # save time and end the loop

            
            else:
                doctors.append(self.__main)
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print(doctors)
            

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if self.find_index(index, doctors):
                        doctor = doctors[index]

              
                        print(f"Current details for doctor {index + 1}: {doctor.get_full_name()} | {doctor.get_speciality()}")

                        print('Choose the field to be updated:')
                        print(' 1 First name')
                        print(' 2 Surname')
                        print(' 3 Speciality')

                        op = input('Input: ')

              # Update the selected field
                        if op == '1':
                            new_first_name = input("Enter new first name: ")
                            Doctor.set_first_name(new_first_name)
                        elif op == '2':
                            new_surname = input("Enter new surname: ")
                            Doctor.set_surname(new_surname)
                        elif op == '3':
                            new_speciality = input("Enter new speciality: ")
                            Doctor.set_speciality(new_speciality)
                        else:
                            print("Invalid operation.")

                        print('Doctor details updated successfully.')

                    else:
                          print("Invalid doctor ID.")

                
                        

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase
            
            op.lower()
            if op == "1":
                new_first_name=input("Set First Name: ")
                new_first_name=self.__first_name
                print("New Doctor First Name: ")
            elif op == "2": 
                new_surname=input("Set Surname: ")
                new_surname=self.__surname
                print("New Doctor Surname: ")
            elif op == "3":
                new_speciality=input("Set Speciality: ")
                new_speciality=self.__speciality
                print("New Doctor Speciality: ")
            

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            if doctor_index in doctors:
                doctor_index.remove()


           
            print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        
    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                assigned_doctor = doctors[doctor_index]
                patients[patient_index].assign_doctor(assigned_doctor)
                assigned_doctor.add_patient(patients[patient_index])                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def get_discharged_patient():
        discharged_patients = []
        return discharged_patients
    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        while True:
            print("-----Discharge Patient-----")

       
            op = input('Do you want to discharge a patient(Y/N):').lower()
            discharged_patients = Patient.get_discharged_patient()
            if op == 'yes' or op == 'y':
                f=input("Patient first name: ")
                l=input("Patient last name: ")
                if f and l in patients:
                    patients.remove(Patient(f, l))
                    discharged_patients.append(Patient(f, l))
                else:
                    print("Patient not found")

            elif op == 'no' or op == 'n':
                break

            # unexpected entry
            else:
                print('Please answer by yes or no.')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)
        

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            print("Update Username: ")
            newuser=input("New Username: ")
            self.__username=newuser
            print("Username updated successfully. ")
            

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print("Password Update Successful")
        elif op == 3:
            new_address = input("Enter New Address")
            self.__address = new_address
            print("Address Update Successful")

        else:
            print("Invalid operation.")

