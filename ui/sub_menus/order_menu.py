from models.order import Order
from models.customer import Customer
from services.orderservice import OrderService
from services.customerservice import CustomerService
from ui.sub_menus.customer_menu import CustomerUI
from ui.ui_standard_functions import UIStandard
HOMECOMMANDS = ["h", "H", "s", "S"]


class OrderUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self, name, a_type):
        self.__name = name
        self.__order_service = OrderService()
        self.__customer_service = CustomerService()
        self.__customer_menu = CustomerUI(name, a_type)
        self.__uistandard = UIStandard(name, a_type)

    def order_menu(self):
        """Prentar pantana viðmót tekur við inputi"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder þangað til ég næ að
            # lata while loopuna virka betur
            choice = self.__uistandard.show_menu(
                "Pantanir\n\t1. Yfirlit pantana\n\t2. Ný pöntun\n", "Veldu aðgerð: ")
            if choice == "1":
                choice = self.order_list_menu()
            elif choice == "2":
                choice = self.new_order_menu()
        return choice

    def order_list_menu(self):
        """Prentar innra pantana viðmót og tekur við input"""
        choice = ""
        while choice not in HOMECOMMANDS:  # Placeholder
            choice = self.__uistandard.show_menu(
                """Pantanir - Yfirlit pantana\n\tSækjaupplýsingar út frá:
\t1. Kennitölu\n\t2. Pöntunarnúmeri\n\t3. Allar Pantanir\n""", "Veldu aðgerð: ")
            if choice == "1":  # TODO Þurfum að geta tengt viðskiptavin við pöntun
                pass
            if choice == "2":  # TODO Þurfum að gefa pöntunarnúmer
                pass
            if choice == "3":
                self.all_orders()
        return choice

    def all_orders(self):
        self.__uistandard.print_header()
        print(" {:11}| {:5}| {:25}| {:11}| {:10}| {:6}| {:10}".format(
            "Dagsetning", "Pöntunarnúmer", "Nafn", "Kennitala",
            "Tegund", "Bílnúmer", "Staða"))
        print("\t", "-"*100)
        string = self.__order_service.show_orders()
        print(string)
        # Sæki drasl1

    def new_order_menu(self):
        self.__uistandard.print_header()
        print("Pantanir - Ný pöntun\n\tTímabil\n\t--------")
        begin_date = input("\tUpphafsdagsetning: ")
        end_date = input("\tSkiladagsetning: ")
        print("\n\tFlokkar\n\t-------\n\t(J)eppi\n\t(F)ólksbíll\n\t(S)endibíll\n")
        type_of_car = input("\tFlokkur: ")
        insurance_price = 100  # Hér þarf að sækja verð
        insurance = input(
            "\tViðbótartrygging (verð {} á dag) (J)á/(N)ei: ".format(
                insurance_price))
        if insurance == "j" or insurance == "J":
            insurance = True
        else:
            insurance = False
        format(insurance_price)
        discount = input("\tAfsláttur(0-20%): ")
        total_price = 10000  # hér þarð að nota aðra klasa
        ssn = input("\tKennitala viðskiptavinar: ")
        # if setning til að athuga hvort manneskjan sé til. Ef svo er
        # þá prentast út upplýsingar um hana, annars er sótt fall til
        # að gera nýjan viðskiptavin
        customer = self.__customer_service.find_customer(ssn)
        if customer:
            customer_name = customer.get_name()
        else:
            print(
                "Viðskiptavinur ekki skráður í kerfið. Vinsamlegast skráðu nauðsynlegar upplýsingar.")
            self.__uistandard.print_header  # Héðan og
            print("Viðskiptavinir - Nýr viðskiptavinur\n")
            ssn = input("\tKennitala: ")
            name = input("\tNafn: ")
            phone_number = input("\tSími: ")
            credit_card_number = input("\tKreditkort: ")
            a_customer = Customer(ssn, name, phone_number, credit_card_number)
            self.__customer_service.make_customer(a_customer)
            new_customer = self.__customer_service.find_customer(ssn)
            print("{:>20}{:>30}{:>20}".format("Kennitala", "Nafn", "Sími"))
            # hingað er fall sem að er alveg eins og í customer ui en er ekki hægt að vísa beint í því að
            print(new_customer)
            # þegar ég bý til viðskiptavininn í repoinu sem að customer ui vísar í verður hann ekki til hér.
            # Vanar eitthvað sniðugt workaround hér
            customer = self.__customer_service.find_customer(ssn)
            customer_name = customer.get_name()

        print("\n\tViðskiptavinur: {}".format(customer_name))
        payment = input("\tGreiðslumáti: (D)ebit, (K)redit, (P)eningar: ")
        order = Order(begin_date, end_date, type_of_car, insurance)
        self.__order_service.make_order(order)

        # kallar á föll og býr til klasa
        print("---------------------\nPöntun Staðfest\n")
        return "h"
