from models.customer import Customer
from services.customerservice import CustomerService
from ui.ui_standard_functions import UIStandard
import time
HOMECOMMANDS = ["h", "H", "s", "S"]


class CustomerUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, a_type):
        self.__name = name
        self.__customer_service = CustomerService()
        self.__uistandard = UIStandard(name, a_type)

    def customer_menu(self):
        """Prentar viðskiptavinaviðmót sölumanns og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:
            choice = self.__uistandard.show_menu(
                """Viðskiptavinir\n\t1. Leita eftir kennitölu
    \t2. Fá yfirlit yfir alla viðskiptavini\n\t3. Nýr viðskipavinur""", "Veldu aðgerð")
            if choice == "1":
                ssn = input("Kennitala: ")
                customer = self.__customer_service.find_customer(ssn)
                # returnar None ef að hann finnst ekki
                if customer:
                    self.find_customer(ssn, customer)
                else:
                    print("Enginn viðskiptavinur skráður á þessa kennitölu")
                    time.sleep(2)

            if choice == "2":
                choice = self.get_customer_list()
            if choice == "3":
                self.new_customer_menu()
        return choice

    def find_customer(self, ssn, customer):
        self.__uistandard.print_header()
        print("Viðskiptavinir - Nánari upplýsingar\n")
        print("{:>20}{:>30}{:>20}".format("Kennitala", "Nafn", "Sími"))
        print(customer)
        # self.__order_service.showorders(customer)
        # þetta vantar alveg inn
        choice = input("\t1. Breyta\n\t2. Eyða\n\tVeldu aðgerð: ")
        if choice == "1":
            self.change_menu(ssn)
        elif choice == "2":
            self.__customer_service.remove_customer(ssn)
            print("Viðskiptavini hefur verið eytt")
            time.sleep(2)
        else:
            print("Aðgerð ekki í boði")
            time.sleep(2)

    def change_menu(self, ssn):
        what_to_change = input("1. Breyta nafni"
                               "\n2. Breyta símanúmer"
                               "\n3. Breyta kredikortanúmeri"
                               "\nVeldu aðgerð: ")
        if what_to_change == "1":
            new_name = input("Nýtt nafn: ")
            self.__customer_service.change_name(ssn, new_name)
            print("Nafni viðskiptavinar hefur verið breytt")
            time.sleep(2)
        if what_to_change == "2":
            new_phone_number = input("Nýja símanúmerið: ")
            self.__customer_service.change_phone_number(ssn, new_phone_number)
            print("Símanúmeri viðskiptavinar hefur verið breytt")
            time.sleep(2)
        if what_to_change == "3":
            new_card_number = input("Nýja kortanúmerið: ")
            self.__customer_service.change_card(ssn, new_card_number)
            print("Kreditkortanúmeri viðskiptavinar hefur verið breytt")
            time.sleep(2)

    def get_customer_list(self):
        """Prentar ut lista yfir alla viðskiptavini með grunnupplýsingum"""
        self.__uistandard.print_header()
        print("Viðskiptavinir - Allir Viðskiptavinir")
        print("{:>20}{:>30}{:>20}".format("Kennitala", "Nafn", "Sími"))
        print("-"*70)
        string = self.__customer_service.get_list()
        print(string)
        choice = input("B - tilbaka, H - Heim, S - Útskrá: ")
        if choice in HOMECOMMANDS:
            return choice
        else:
            return None

    def new_customer_menu(self):
        """biður um nauðsynlegar upplýsingar og býr til viðskiptavin"""
        self.__uistandard.print_header
        print("Viðskiptavinir - Nýr viðskiptavinur\n")
        ssn = input("\tKennitala: ")
        name = input("\tNafn: ")
        phone_number = input("\tSími: ")
        credit_card_number = input("\tKreditkort: ")
        a_customer = Customer(ssn, name, phone_number, credit_card_number)
        self.__customer_service.make_customer(a_customer)
        new_customer = self.__customer_service.find_customer(ssn)
        print("{:>20}{:>30}{:>20}".format("Kennitala", "Nafn", "Sími"))
        print(new_customer)
        time.sleep(2)

    def save_program(self):
        self.__customer_service.save_program()
