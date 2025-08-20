import csv
import os

class EmployeeManager:
    def __init__(self):
        self.employees = {}
        self.data_file = './employees.csv'
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'x', newline='') as file:
                pass
        self._load_from_csv()        
    def _load_from_csv(self):
        with open(self.data_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ID = int(row['ID'])
                self.employees[ID] = {
                    'name': row['Name'],
                    'position': row['Position'],
                    'salary': float(row['Salary']),
                    'Email': row['Email']
                }
            file.close()
    def _save_to_csv(self):
        with open(self.data_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Position', 'Salary', 'Email'])
            for ID, employee in self.employees.items():
                writer.writerow([ID, employee['name'], employee['position'], 
                               employee['salary'], employee['Email']])
            file.close()
    def add_employee(self,ID, name, position, salary, Email):
        while True:
            try:
                ID = int(ID)
                break
            except ValueError:
                print("ID must be an integer, please try again.")
                ID = input("Enter ID: ")
        while True:
            try:
                salary = float(salary)
                break
            except ValueError:
                print("Salary must be a number, please try again.")
                salary = input("Enter salary: ")
        while '@' not in Email or '.' not in Email.split('@')[-1]:
            print("Email must be a valid email address, please try again.")
            Email = input("Enter a valid email: ")
        if ID in self.employees:
            print(f"Employee with ID {ID} already exists.")
            return -1
        else:
            employee = {
            'name': name,
            'position': position,
            'salary': salary,
            'Email': Email
            }
            self.employees[ID] = employee
            self._save_to_csv()
            return 0
    def List_employees(self):
        print("ID\tName\tPosition\tSalary\tEmail")
        for ID, employee in self.employees.items():
            print(f"{ID}\t{employee['name']}\t{employee['position']}\t{employee['salary']}\t{employee['Email']}")
    def Update_employee(self, ID, name=None, position=None, salary=None, Email=None):
        while True:
            try:
                ID = int(ID)
                break
            except ValueError:
                print("ID must be an integer, please try again.")
                ID = input("Enter ID: ")
        while True:
            try:
                if salary != '': 
                    salary = float(salary)
                break
            except ValueError:
                print("Salary must be a number, please try again.")
                salary = input("Enter salary: ")
            Email = input("Enter a valid email: ")
        if ID not in self.employees:
            print(f"Employee with ID {ID} does not exist, cannot update.")
            return -1
        if name != '':
            self.employees[ID]['name'] = name
        if position != '':
            self.employees[ID]['position'] = position
        if salary != '':
            self.employees[ID]['salary'] = salary
        if Email != '':
            while ('@' not in Email or '.' not in Email.split('@')[-1]):
                print("Email must be a valid email address, please try again.")
            self.employees[ID]['Email'] = Email
        self._save_to_csv()
        return 0
    def Delete_employee(self, ID):
        if int(ID) not in self.employees:
            print(f"Employee with ID {ID} does not exist, cannot delete.")
            return -1
        del self.employees[int(ID)]
        self._save_to_csv()
        return 0
    def Search_employee(self, ID):
        if int(ID) not in self.employees:
            print(f"Employee with ID {ID} does not exist.")
            return
        employee = self.employees[int(ID)]
        print(f"ID: {ID},\nName: {employee['name']},\nPosition: {employee['position']},\nSalary: {employee['salary']},\nEmail: {employee['Email']}")