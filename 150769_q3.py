class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated for {self.name} to {self.salary}")

    def __str__(self):
        return f"{self.name} (ID: {self.employee_id}, Salary: {self.salary})"


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} has been added to {self.department_name} department.")

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for {self.department_name}: {total}")
        return total

    def display_all_employees(self):
        if self.employees:
            print(f"Employees in {self.department_name}:")
            for emp in self.employees:
                emp.display_details()
        else:
            print(f"No employees in {self.department_name} department.")


def main():
    dept_name = input("Enter the department name: ")
    department = Department(dept_name)

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Update Employee Salary")
        print("3. Display All Employees")
        print("4. Show Total Salary Expenditure")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            salary = float(input("Enter salary: "))
            emp = Employee(name, emp_id, salary)
            department.add_employee(emp)

        elif choice == '2':
            emp_id = input("Enter employee ID to update salary: ")
            found = False
            for emp in department.employees:
                if emp.employee_id == emp_id:
                    new_salary = float(input("Enter new salary: "))
                    emp.update_salary(new_salary)
                    found = True
                    break
            if not found:
                print("Employee not found.")

        elif choice == '3':
            department.display_all_employees()

        elif choice == '4':
            department.total_salary_expenditure()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
