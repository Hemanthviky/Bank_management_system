from connection import Conn
from tabulate import tabulate

class View_Customer:

    def Display_customer(self, customer_user_name):
        sql = "SELECT * FROM customers where customer_user_name= ?"
        Conn.cursor.execute(sql,customer_user_name)
        customer_data = Conn.cursor.fetchall()
        rows = ['customer_id', 'customer_first_name', 'customer_last_name', 'customer_user_name', 'customer_password',
                'customer_dob', 'customer_phone_no', 'customer_email_id', 'customer_pancard_id', 'customer_aadhar_no',
                'customer_occupasion', 'customer_nominee_name', 'customer_account_type', 'customer_branch',
                'customer_address', 'customer_account_number', 'customer_ifsc_code', 'customer_current_balance']
        print(tabulate(customer_data, rows, tablefmt="rounded_outline"))

    def Balance_check(self, customer_user_name):
        sql = "SELECT customer_id,customer_current_balance FROM customers WHERE customer_user_name = ?"
        Conn.cursor.execute(sql, customer_user_name)
        rows = ['customer_id', 'customer_current_balance']
        balance = Conn.cursor.fetchall()
        print(tabulate(balance, rows, tablefmt='rounded_outline'))

    def loan_balance_check(self, customer_user_id):
        sql = "SELECT loan_id,loan_balance_amount,loan_type FROM loan WHERE customer_id = ?"
        Conn.cursor.execute(sql, customer_user_id)
        rows = ['Loan_id', 'Loan_type', 'Loan_Balance']
        balance = Conn.cursor.fetchall()
        print(tabulate(balance, rows, tablefmt='rounded_outline'))

    def online_transactions_history(self, customer_user_name):
        sql = "SELECT * FROM transactions where customer_user_name= ?"
        Conn.cursor.execute(sql, (customer_user_name,))
        online_transactions_history = Conn.cursor.fetchall()
        rows = ['transaction_is', 'customer_id', 'customer_user_name', 'customer_account_number',
                'transfer_amount', 'ifsc_code', 'account_number', 'transactions_date', 'branch']
        print(tabulate(online_transactions_history, rows, tablefmt="rounded_outline"))

    def deposit_history(self, customer_user_name):
        sql = "SELECT * FROM deposit_ where customer_user_name= ?"
        Conn.cursor.execute(sql, customer_user_name)
        deposit_history = Conn.cursor.fetchall()
        rows = ['employee_id', 'employee_user_name', 'customer_id', 'customer_user_name',
                'customer_account_number', 'deposit_amount', 'date', 'branch']
        print(tabulate(deposit_history, rows, tablefmt="rounded_outline"))

class View_Employee:

    def display_employee_details(self):
        Conn.cursor.execute("SELECT * FROM employee")
        employee_data = Conn.cursor.fetchall()
        rows = ['employee_id', 'employee_first_name', 'employee_last_name', 'employee_user_name',
                'employee_password', 'employee_dob', 'employee_join_date', 'employee_phone_no',
                'employee_email_id', 'employee_desigination', 'employee_address', 'employee_branch']
        print(tabulate(employee_data, rows, tablefmt="rounded_outline"))

    def online_transactions_history(self, customer_user_name):
        sql = "SELECT * FROM transactions where customer_user_name= ?"
        Conn.cursor.execute(sql, (customer_user_name,))
        online_transactions_history = Conn.cursor.fetchall()
        rows = ['transaction_is', 'customer_id', 'customer_user_name', 'customer_account_number',
                'transfer_amount', 'ifsc_code', 'account_number', 'transactions_date', 'branch']
        print(tabulate(online_transactions_history, rows, tablefmt="rounded_outline"))

    def display_salary(self, employee_id):
        sql = "SELECT * FROM salary WHERE employee_id = ?"
        Conn.cursor.execute(sql, (employee_id,))
        display_salary = Conn.cursor.fetchall()
        rows = ['employee_id', 'employee_designation', 'employee_salary']
        print(tabulate(display_salary, rows, tablefmt='rounded_outline'))

class View_Admin:

    def display_customer_details(self):
        Conn.cursor.execute("SELECT * FROM customers")
        customer_data = Conn.cursor.fetchall()
        rows = ['customer_id', 'customer_first_name', 'customer_last_name', 'customer_user_name', 'customer_password',
                'customer_dob', 'customer_phone_no', 'customer_email_id', 'customer_pancard_id', 'customer_aadhar_no',
                'customer_occupasion', 'customer_nominee_name', 'customer_account_type', 'customer_branch',
                'customer_address',
                'customer_account_number', 'customer_ifsc_code', 'customer_current_balance']
        print(tabulate(customer_data, rows, tablefmt="rounded_outline"))

    def display_employee_details(self):
        Conn.cursor.execute("SELECT * FROM employee")
        employee_data = Conn.cursor.fetchall()
        rows = ['employee_id', 'employee_first_name', 'employee_last_name', 'employee_user_name',
                'employee_password', 'employee_dob', 'employee_join_date', 'employee_phone_no',
                'employee_email_id', 'employee_desigination', 'employee_address', 'employee_branch']
        print(tabulate(employee_data, rows, tablefmt="rounded_outline"))

    def online_transactions_history(self, customer_id):
        sql = "SELECT * FROM transactions where customer_id= ?"
        Conn.cursor.execute(sql, (customer_id,))
        online_transactions_history = Conn.cursor.fetchall()
        rows = ['transaction_is', 'customer_id', 'customer_user_name', 'customer_account_number',
                'transfer_amount', 'ifsc_code', 'account_number', 'transactions_date', 'branch']
        print(tabulate(online_transactions_history, rows, tablefmt="rounded_outline"))
