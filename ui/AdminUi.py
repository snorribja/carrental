from datetime import date
from models.employee import Employee
from services.employeeservice import EmployeeService

HEIMSETNINGAR = ["h", "H", "s", "S"]


class AdminUI(object):
    def __init__(self, username):
        self.__username = username
        self.__employee_service = EmployeeService()

    def print_header(self):
        '''Prentar haus fyrir Kerfisstjóra'''
        print("{:40s} {:>39}".format(
            "Kerfisstjóri - notandi: {}".format(self.__username), str(
                date.today())))
        print(("-"*80))

    def show_menu(self, texti, prompt):
        self.print_header()
        print(texti)

        choice = input(prompt)

        return choice

    def main_menu(self):
        '''Upphafssíða fyrir kerfisstjóra'''
        choice = ""
        while choice not in HEIMSETNINGAR:
            choice = self.show_menu(
                "\n\t1. Starfsmenn\n\t2. Nýr starfsmaður\n\t3. Bílayfirlit\n",
                "Veldu síðu: ")
            if choice == 1:
                choice = self.employee_menu
            # elif choice == 2:
                # choice =  # new employee
            elif choice == 3:
                choice = self.car_menu

    def car_menu(self):
        '''Bílayfirlit menu fyrir Kerfisstjóra'''
        choice = ""
        while choice not in HEIMSETNINGAR:
            choice = self.show_menu(
                "Bílayfirlit\n\t1. Allir bílar\n\t2. Lausir bílar\n\t3. Í útleigu\n\t\
4. Nýskrá bíl\n\t5. Afskrá bíl\n", "Veldu aðgerð: ")
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass

        return choice

    def print_employee_header(self):
        '''Prentar haus fyrir starfmannayfirlit'''
        print("{:<10s}| {:<10s}| {:<10s}| {:<10s}| {:<10s}| {:<20s}".format(
            "Notandi", "Lykilorð", "Hlutverk", "Nafn", "Sími", "Heimilisfang"))
        print("-"*80)

    def employee_menu(self):
        '''Yfirlit yfir alla starfsmenn fyrirtækis,
        Möguleiki á að eyða starfsmanni'''
        # choice = ""
        # while choice not in HEIMSETNINGAR:
        self.print_header()
        self.print_employee_header()

    def new_employee(self):
        '''Býr til nýjan starfsmann'''
        choice = ""
        while choice not in HEIMSETNINGAR:
            self.print_header()
            username = input("\tNotendanafn: ")
            password = input("\tLykilorð: ")
            name = input("\tNafn: ")
            address = input("\tHeimilisfang: ")
            phonenumber = input("\tSími: ")
            emp_type = input("\t(S)öludeild, (y)firmaður eða (k)erfisstjóri: ")
            if emp_type.lower() == "k":
                emp_type = "admin"
            elif emp_type.lower() == "y":
                emp_type = "yfirmadur"
            an_employee = Employee(username, password, name,
                                   address, phonenumber, emp_type)
            self.__employee_service.add_employee(an_employee)

    def quit(self):
        pass


def main():
    A1 = AdminUI("logigeir")
    A1.new_employee()


main()
