# Python_Final_Project
A project to manage the employees in a company

## The Project contain two main files :~

# Employees Manager 👷:~

the class responsible for creating, editing, deleting or even searching an employee in the manager or the csv file

- the Manager uses a dictionary with the ID as the index to the employee, while the rest of the information are  inserted in another smaller dictionary

- The manager class includes two variables :-
  1. `Employees` : the main dictionnary containing all the employees' informations  `[ID🪪, Name, Position, Salary💲, E-mail]`
  2. `Data_File` : the main directory of the csv file 📁 to implement all the data of the employees

       **The csv file is created always in the directory `./employees.csv`**


- The manager Class involves the following functions :-
  1. `_load_from_csv` : load the csv file at the creation of the manager.
  2. `_save_to_csv` : save all data to the csv file after every modification.
  3. `add_employee` : add an employee to the manager data and update the csv accordingly.
  4. `List_employees` : print all the employees in the manager database with all their informations.
  5. `Update` : Edit one or more of the fields of the employee (Except the ID) and update the csv accordingly.
  6. `Delete_employee` : Delete an employee from the manager database and update the csv accordingly.
  7. `Search_employee` : Find a specific employee and list its attributes (ID is used for the searching operation.


     **ID is always assumed to be an integer**

     

# UI :~

the main UI & options the user deal with in order to work with the manager, the csv file is updated accordingly after each action.
- To Start the Project :~
1. Copy or Pull the code files on a IDE (integrated development environment) software
2. Select the file `UI.py`
3. Run the file using the icon ▶️
4. Enjoy !! 
