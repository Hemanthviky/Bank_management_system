from connection import Conn
import random
import string
class Customer_Table:
    def Unique_account_no(self):
        while True:
            account_no = random.randint(1000000000, 9999999999)
            Conn.cursor.execute("SELECT * FROM customers WHERE customer_account_number = ?", (account_no,))
            existing_data = Conn.cursor.fetchone()
            if not existing_data:
                return account_no
    def Unique_ifsc_code(self):
        while True:
            ifsc_code = ''.join(random.choices(string.ascii_uppercase, k=4)) + \
                        str(random.randint(0, 9999)).zfill(4)
            Conn.cursor.execute("SELECT * FROM customers WHERE customer_ifsc_code = ?", (ifsc_code,))
            existing_data = Conn.cursor.fetchone()
            if not existing_data:
                return ifsc_code
    def Sign_up(self):
        data = {
            "customer_first_name": input("First Name: "),
            "customer_last_name": input("Last Name: "),
            "customer_user_name": input("User Name: "),
            "customer_password": input("Password: "),
            "customer_dob": input("Date (YYYY-MM-DD): "),
            "customer_phone_no": int(input("Phone Number: ")),
            "customer_email_id": input("Email ID: "),
            "customer_pancard_id": input("Pancard: "),
            "customer_aadhar_no": int(input("Aadhar Number: ")),
            "customer_occupasion": input("Occupation: "),
            "customer_nominee_name": input("Nominee Name: "),
            "customer_account_type": input("Account Type (Savings/Current): ").upper(),
            "customer_branch": input("Branch: "),
            "customer_address": input("Address: "),
            "customer_account_number": self.Unique_account_no(),
            "customer_ifsc_code": self.Unique_ifsc_code(),
            "customer_current_balance": 0
        }

        sql = """INSERT INTO customers (customer_first_name, customer_last_name, customer_user_name, customer_password,
                    customer_dob, customer_phone_no, customer_email_id, customer_pancard_id, customer_aadhar_no,
                    customer_occupasion, customer_nominee_name, customer_account_type, customer_branch, customer_address,
                    customer_account_number, customer_ifsc_code, customer_current_balance)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

        Conn.cursor.execute(sql, data['customer_first_name'],data['customer_last_name'],data['customer_user_name'],
                            data['customer_password'],data['customer_dob'],data['customer_phone_no'],
                            data['customer_email_id'],data['customer_pancard_id'],data['customer_aadhar_no'],
                            data['customer_occupasion'],data['customer_nominee_name'],data['customer_account_type'],
                            data['customer_branch'],data['customer_address'],data['customer_account_number'],
                            data['customer_ifsc_code'],data['customer_current_balance'])
        Conn.connection.commit()
        print(f"{data['customer_user_name']} has successfully created a bank account")
    def verify_customer(self, customer_user_name, customer_password):
        sql = """SELECT customer_user_name,customer_password FROM customers 
                 WHERE customer_user_name = ? AND customer_password = ?"""
        Conn.cursor.execute(sql, customer_user_name, customer_password)
        customer_data = Conn.cursor.fetchone()
        return customer_data is not None
class Employee_Table:
    def Sign_up(self):
        data = {
            'employee_first_name': input("First Name:"),
            'employee_last_name': input("Last Name:"),
            'employee_user_name': input("User Name:"),
            'employee_password': input("Password:"),
            'employee_dob': input("Date (YYYY-MM-DD): "),
            'employee_join_date': input("JOIN date (YYYY-MM-DD): "),
            'employee_phone_no': int(input("Phone Number:")),
            'employee_email_id': input("Email Id"),
            'employee_desigination': input("Disigination:"),
            'employee_address': input("Address:"),
            'employee_branch': input("Branch:")
        }

        sql = """INSERT INTO employee (employee_first_name, employee_last_name, employee_user_name,
                              employee_password, employee_dob, employee_join_date, employee_phone_no,
                              employee_email_id, employee_desigination, employee_address, employee_branch)
                              VALUES (?,?,?,?,?,?,?,?,?,?,?)"""

        Conn.cursor.execute(sql, data['employee_first_name'],data['employee_last_name'],
                            data['employee_user_name'],data['employee_password'],data['employee_dob'],
                            data['employee_join_date'],data['employee_phone_no'],data['employee_email_id'],
                            data['employee_desigination'],data['employee_address'],data['employee_branch'])
        Conn.connection.commit()
        print(f"{data['employee_user_name']} Successfully Joined the Bank as {data['employee_desigination']} !!!")
    def verify_employee(self, employee_user_name, employee_password):
        sql = """SELECT employee_user_name,employee_password FROM employee 
                 WHERE employee_user_name = ? AND employee_password = ?"""
        Conn.cursor.execute(sql,employee_user_name, employee_password)
        employee_data = Conn.cursor.fetchone()
        return employee_data is not None
class Transactions_Table:
    def online_transaction(self):
        data = {
            "customer_id": int(input("Enter your customer ID: ")),
            "customer_user_name": input("Enter the customer user name: "),
            "customer_account_number": int(input("Enter the account number: ")),
            "transfer_amount": int(input("Enter the transfer amount: ")),
            "ifsc_code": input("Enter the IFSC code: "),
            "account_number": int(input("Enter the the account number: ")),
            "transactions_date": input("Enter the date(YYYY-MM-DD)"),
            "branch": input("Enter the branch")
        }
        sql = """ INSERT INTO transactions(customer_id,customer_user_name ,customer_account_number,
                   transfer_amount ,ifsc_code ,account_number ,transactions_date,branch)
                   VALUES (?,?,?,?,?,?,?,?)"""
        Conn.cursor.execute(sql,data['customer_id'],data['customer_user_name'],data['customer_account_number'],
                            data['transfer_amount'],data['ifsc_code'],data['account_number'],data['transactions_date'],
                            data['branch'])
        sql_1 = """UPDATE customers SET customer_current_balance = customer_current_balance - ? WHERE customer_id = ?"""
        Conn.cursor.execute(sql_1,data['transfer_amount'],data['customer_account_number'])
        sql_2 = """UPDATE customers SET customer_current_balance = customer_current_balance + ? 
                WHERE customer_account_number = ?"""
        Conn.cursor.execute(sql_2, data['transfer_amount'], data['account_number'])
        Conn.connection.commit()

class Deposit_Table:
    def deposit_(self):
        data = {
            "employee_id": int(input("Enter employee ID: ")),
            "employee_user_name": input("Enter employee user name: "),
            "customer_id": int(input("Enter customer Id: ")),
            "customer_user_name": input("Enter the Customer user name: "),
            "customer_account_number": int(input("Enter the customer account number: ")),
            "deposit_amount": int(input("Enter the deposit amount: ")),
            "date": input("Enter current date(YYYY-MM-DD): "),
            "branch": input("Enter the Branch: ")
        }

        sql = """ INSERT INTO deposit_(employee_id,employee_user_name,customer_id,customer_user_name,
                  customer_account_number,deposit_amount,date,branch)
                  VALUES (?,?,?,?,?,?,?,?)"""

        sql_1 = """UPDATE customers SET customer_current_balance = customer_current_balance + ? 
                   WHERE customer_id = ?"""

        Conn.cursor.execute(sql, data['employee_id'],data['employee_user_name'],data['customer_id'],
                            data['customer_user_name'],data['customer_account_number'],
                            data['deposit_amount'],data['date'],data['branch'])

        Conn.cursor.execute(sql_1, data['deposit_amount'],data['customer_id'])
        Conn.connection.commit()
class Admin:
    def verify_admin(self, admin_name, admin_password):
        sql = "SELECT * FROM admin WHERE admin_name = ? AND admin_password = ?"
        Conn.cursor.execute(sql, admin_name, admin_password)
        admin_data = Conn.cursor.fetchone()
        return admin_data is not None
class Salary_Table:
    def salary(self):
        data = {
            'employee_id': int(input("Employee ID")),
            'employee_designation': input("Desigination:"),
            'employee_salary': input("Salary amount:")
        }

        sql = """ INSERT INTO salary(employee_id,employee_designation,employee_salary)
                   VALUES(?,?,?)"""

        Conn.cursor.execute(sql, data['employee_id'],data['employee_designation'],data['employee_salary'])

        Conn.connection.commit()
class Loan_Table:
    def add_loan(self):
        data = {
            'customer_id': int(input("Enter the customer Id: ")),
            'customer_first_name': input("Enter the Customer first name: "),
            'customer_last_name': input("Enter the Customer last name: "),
            'loan_type': input("Enter loan type Housing/Car/Bike/Personal : "),
            'loan_amount': int(input("Enter the Loan Amount: ")),
            'loan_date': input("Enter the date (YYYY-MM-DD): "),
            'loan_amount_paid': 0.0,
            'loan_balance_amount': int(input("Loan Balance Amount"))
        }

        sql = """INSERT INTO loan(customer_id,customer_first_name,
                 customer_last_name,loan_type,loan_amount,loan_date,
                 loan_amount_paid,loan_balance_amount)
                 VALUES(?,?,?,?,?,?,?,?)"""

        sql_1 = """UPDATE customers SET customer_current_balance = customer_current_balance + ?
                    WHERE customer_id = ?"""

        Conn.cursor.execute(sql,data['customer_id'],data['customer_last_name'],
                            data['customer_last_name'],data['loan_type'],data['loan_amount'],data['loan_date'],
                            data['loan_amount_paid'],data['loan_balance_amount'])

        Conn.cursor.execute(sql_1,data['loan_amount'],data['customer_id'])

        Conn.connection.commit()

        print(
            f"{data['loan_type']} loan has been successfully confirmed and {data['loan_amount']} "
            f"has been added to your account")
    def pay_loan(self):
        data = {
            "pay_amount": int(input("Enter the Pay Amount: ")),
            "id": int(input("Enter the customer_id: "))
        }

        sql = """UPDATE loan SET loan_amount_paid = loan_amount_paid - ?
                  WHERE customer_id = ?"""

        sql_1 = """UPDATE customers SET customer_current_balance = customer_current_balance - ?
                    WHERE customer_id = ?"""

        Conn.cursor.execute(sql,data['pay_amount'],data['id'])

        Conn.cursor.execute(sql_1,data['pay_amount'],data['id'])

        Conn.connection.commit()

        print(f"{data['pay_amount']} has be paid")
