from Database import Customer_Table
from Database import Employee_Table
from Database import Loan_Table
from Database import Deposit_Table
from Database import Transactions_Table
from Database import Admin
from Database import Salary_Table
from View import View_Admin
from View import View_Customer
from View import View_Employee


def main():
    customer_table = Customer_Table()
    employee_table = Employee_Table()
    loan_table = Loan_Table()
    deposit_table = Deposit_Table()
    transaction_table = Transactions_Table()
    admin = Admin()
    salary_table = Salary_Table()
    view_admin = View_Admin()
    view_customer = View_Customer()
    view_employee = View_Employee()
    while True:
        print("Enter the Choice")
        print("1. Admin Options")
        print("2. Employee Options")
        print("3. Customer Options")
        print("4. Exit")
        choice = int(input("Enter the choice number: "))
        if choice == 1:
            print("\nAdmin Page!")
            admin_name = input("Enter admin name: ")
            admin_password = input("Enter admin password: ")
            if admin.verify_admin(admin_name, admin_password):
                print(f"\n1"
                      f"Welcome {admin_name}")
                print("Admin login successful.")
                while True:
                    print("Enter the Choices")
                    print("1. ADD Salary To customers")
                    print("2. Display customer details")
                    print("3. Display Employee details")
                    print("4. Online Transaction History")
                    print("5. Exit")
                    admin_choice = int(input("Enter the Choice Number:"))
                    if admin_choice == 1:
                        salary_table.salary()
                    elif admin_choice == 2:
                        view_admin.display_customer_details()
                    elif admin_choice == 3:
                        view_admin.display_employee_details()
                    elif admin_choice == 4:
                        customer_id = int(input("Enter the customer_id to check then online transaction history "))
                        view_admin.online_transactions_history(customer_id)
                    elif admin_choice == 5:
                        break
                    else:
                        print("\nInvalid choice number.")
            else:
                print("\nInvalid admin_name or admin_password.")


        elif choice == 2:
            print("\nEmployee Page!")
            print("1. Login")
            print("2. SignUp")
            employee_choice = int(input("\nEnter the choice:"))
            if employee_choice == 1:
                employee_user_name = input("Enter employee user name: ")
                employee_password = input("Enter employee password: ")
                if employee_table.verify_employee(employee_user_name, employee_password):
                    print("\nEmployee login successful.")
                    while True:
                        print("1. Employee details")
                        print("2. Deposit Money")
                        print("3. Check Salary")
                        print("4. ADD Loan")
                        print("5. Check online Transactions")
                        print("6. Exit")
                        employee_choice1 = int(input("\nEnter the choice: "))
                        if employee_choice1 == 1:
                            print(f"{employee_user_name} details:\n")
                            view_employee.display_employee_details()
                        elif employee_choice1 == 2:
                            deposit_table.deposit_()
                        elif employee_choice1 == 3:
                            employee_id = int(input("Enter the Employee ID: "))
                            view_employee.display_salary(employee_id)
                        elif employee_choice1 == 4:
                            loan_table.add_loan()
                        elif employee_choice1 == 5:
                            customer_user_name = input("\nEnter the customer user name")
                            view_employee.online_transactions_history(customer_user_name)
                        elif employee_choice1 == 6:
                            break
                        else:
                            print("\nInvalid choice number")

            elif employee_choice == 2:
                print("Employee Sign Up!\n")
                employee_table.Sign_up()
            else:
                print("\nInvalid choice number")


        elif choice == 3:
            print("\nCustomer Page!")
            print("1. Login")
            print("2. SignUp")
            customer_choice = int(input("\nEnter the choice: "))
            if customer_choice == 1:
                customer_id = int(input("Enter the ID: "))
                customer_user_name = input("Enter Customer user  name: ")
                customer_password = input("Enter Customer password: ")
                if customer_table.verify_customer(customer_user_name, customer_password):
                    print(f"\nWelcome {customer_user_name}")
                    while True:
                        print("1. Display Your details")
                        print("2. Check the Balance")
                        print("3. Online Transaction")
                        print("4. Deposit History")
                        print("5. Online Transaction History")
                        print("6. Pay Loan amount")
                        print("7. To check the Loan_balance")
                        print("8. Exit")
                        customer_choice1 = int(input("\nEnter the choice:"))
                        if customer_choice1 == 1:
                            print(f'{customer_user_name} details')
                            view_customer.Display_customer(customer_user_name)
                        elif customer_choice1 == 2:
                            view_customer.Balance_check(customer_user_name)
                        elif customer_choice1 == 3:
                            transaction_table.online_transaction()
                        elif customer_choice1 == 4:
                            view_customer.deposit_history(customer_user_name)
                        elif customer_choice1 == 5:
                            view_customer.online_transactions_history(customer_user_name)
                        elif customer_choice1 == 6:
                            loan_table.pay_loan()
                        elif customer_choice1 == 7:
                            view_customer.loan_balance_check(customer_id)
                        elif customer_choice1 == 8:
                            break
                        else:
                            print("Invalid choice number")

            elif customer_choice == 2:
                customer_table.Sign_up()
            else:
                print("Invalid Choice")

        elif choice == 4:
            break
        else:
            print("Invalid Choice")
            main()
main()
