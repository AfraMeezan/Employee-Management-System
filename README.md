 Employee Management System

A simple Python-based command-line application for managing employee records, including managers, storing data using `pickle` in a binary file format.

Features

* Add new employees or managers
* View a summary report of all employees sorted by salary
* Search employees by ID
* Persistent data storage using `pickle`
* Inheritance used for Manager class

File Structure

```
employee_management_system/
│
├── employees.txt         # Binary file storing employee data
├── employee_system.py    # Main Python script
└── README.md             # Project documentation
```

Requirements

* Python 3.x

How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/employee-management-system.git
   cd employee-management-system
   ```

2. Run the program:

   ```bash
   python employee_system.py
   ```

Functional Overview

1. Add Employee

* Input ID, Name, Department, and Salary
* Option to add as a Manager with team size
* Validates salary input
* Adds to the in-memory list and persists on exit

2. Search Employee

* Searches employee by Employee ID
* Displays details if found, otherwise shows an error

 3. Display Summary Report

* Displays all employees sorted by salary in descending order

 4. Exit

* Saves all current data to `employees.txt` file using `pickle`

Class Overview

 `Employee`

* Attributes: `emp_id`, `name`, `department`, `salary`
* Methods:

  * `yearly_salary()` – Calculates annual salary
  * `display_details()` – Prints employee details

 `Manager (inherits Employee)`

* Additional Attribute: `team_size`
* Additional Method:

  * `bonus()` – 10% yearly bonus if managing more than 5 team members

 Data Storage

* Data is saved in a binary file (`employees.txt`) using the `pickle` module for persistence.

