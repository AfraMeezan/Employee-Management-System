import os
import pickle

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        try:
            self.salary = float(salary)
        except ValueError:
            raise ValueError("Invalid salary input! Salary must be a number.")

    def yearly_salary(self):
        return self.salary * 12

    def display_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Monthly Salary: ₹{self.salary:.2f}")

class Manager(Employee):
    def __init__(self, emp_id, name, department, salary, team_size):
        super().__init__(emp_id, name, department, salary)
        self.team_size = team_size

    def bonus(self):
        if self.team_size > 5:
            return 0.10 * self.yearly_salary()
        else:
            return 0

    def display_details(self):
        super().display_details()
        print(f"Role: Manager, Team Size: {self.team_size}, Bonus: ₹{self.bonus():.2f}")

employees = []

def load_employees():
    global employees
    if os.path.exists("employees.txt"):
        with open("employees.txt", "rb") as f:
            employees = pickle.load(f)

def save_employees():
    with open("employees.txt", "wb") as f:
        pickle.dump(employees, f)

def add_employee():
    try:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")
        role = input("Is this employee a Manager? (yes/no): ").lower()
        if role == "yes":
            team_size = int(input("Enter team size: "))
            emp = Manager(emp_id, name, department, salary, team_size)
        else:
            emp = Employee(emp_id, name, department, salary)
        employees.append(emp)
        print(" Employee added successfully.\n")
    except ValueError as ve:
        print(" Error:", ve)

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    for emp in employees:
        if emp.emp_id == emp_id:
            emp.display_details()
            found = True
            break
    if not found:
        print("Employee not found!")

def display_summary():
    if not employees:
        print("No employee records found.")
        return
    sorted_employees = sorted(employees, key=lambda e: e.salary, reverse=True)
    print("\n--- Employee Summary Report (Sorted by Salary Descending) ---")
    for emp in sorted_employees:
        emp.display_details()
        print("-" * 50)

def menu():
    load_employees()
    while True:
        print("\n==== Employee Management System ====")
        print("1. Add Employee")
        print("2. Search Employee by ID")
        print("3. Display Summary Report")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            search_employee()
        elif choice == '3':
            display_summary()
        elif choice == '4':
            save_employees()
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
