from datetime import date
from models.customer import Customer
from models.order import Order
from models.car import Car
from models.employee import Employee
from services.carservice import CarService
from services.customerservice import CustomerService
from services.employeeservice import EmployeeService
from services.orderservice import OrderService
from ui.AdminUi import AdminUI
HOMECOMMANDS = ["h", "H", "s", "S"]


class SalesmanUI(object):
    """Klasi sem sér um viðmót Sölumanns og ferðir þar um"""

    def __init__(self):
        self.__employee_service = EmployeeService()

    def main(self):
        pass
        # a_customer = Employee("gunnarboss", "abc1234",
        #                       "Gunnar Pall")
        # self.__employee_service.add_employee(a_customer)
        # yesno = input("remove?")
        # if yesno == "y":
        #     self.__employee_service.remove_employee("gunnarboss")
        # username = input("username: ")
        # numer = input("skrifaðu 2: ")
        # nytt_nafn = input("skrifaðu nýja nafnið: ")
        # self.__employee_service.change_employee(username, numer, nytt_nafn)
        # username = ("username: ")
        # self.__employee_service.remove_employee(username)
        # atli = self.__employee_service.get_employees()
        # print(atli)

        # bjarki = self.__employee_service.change_employee("jonjones", "", "")
        # gunnar = bjarki.__repr__(1)
        # print(gunnar)


a1 = AdminUI("jonj")

a1.main_menu()
