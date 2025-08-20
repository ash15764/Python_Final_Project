from EmployeeManager import EmployeeManager 

Manager = EmployeeManager()
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. List Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        ID = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")
        Email = input("Enter Employee Email: ")
        issue = Manager.add_employee(ID, name, position, salary, Email)
        if issue != -1:
            print("Employee added successfully.")
    elif choice == '2':
        Manager.List_employees()
    elif choice == '3':
        ID = input("Enter Employee ID to update: ")
        name = input("Enter new Employee Name (leave blank to keep current): ")
        position = input("Enter new Employee Position (leave blank to keep current): ")
        salary = input("Enter new Employee Salary (leave blank to keep current): ")
        Email = input("Enter new Employee Email (leave blank to keep current): ")
        issue = Manager.Update_employee(ID, name, position, salary, Email)
        if issue == -1:
            print("Update failed. Employee does not exist.")
        else:
            print("Employee updated successfully.")
    elif choice == '4':
        ID = input("Enter Employee ID to delete: ")
        issue = Manager.Delete_employee(ID)
        if issue == -1:
            print("Delete failed. Employee does not exist.")
        else:
            print("Employee deleted successfully.")
    elif choice == '5':
        ID = input("Enter Employee ID to search: ")
        Manager.Search_employee(ID)
    elif choice == '6':
        print("Exiting the Employee Management System.")
        break
    
    