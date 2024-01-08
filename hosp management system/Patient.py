class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        self.__first_name=first_name
        self.__surname=surname
        self.__age=age
        self.__mobile=mobile
        self.__postcode=postcode
        self.__symptoms= 'None'
        self.__doctor = 'None'
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        full_name=self.__first_name,self.__surname
        return full_name


    def get_doctor(self,doctor) :
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        return self.__symptoms

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
