# Global list to store employee dictionaries
employees = []

def add_employee(emp_id, name, department, designation):
    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "designation": designation
    }
    employees.append(employee)
    print(f"✔️ Successfully added Employee: {name} (ID: {emp_id})")

def display_all_employees():
    print("\n=============================================")
    print("         EMPLOYEE MANAGEMENT SYSTEM          ")
    print("=============================================")
    
    if not employees:
        print("No records found.")
        print("=============================================")
        return

    for emp in employees:
        print(f"ID:          {emp['id']}")
        print(f"Name:        {emp['name']}")
        print(f"Department:  {emp['department']}")
        print(f"Designation: {emp['designation']}")
        print("---------------------------------------------")
    print(f"Total Employees: {len(employees)}")
    print("=============================================\n")
if __name__ == "__main__":
    add_employee(101, "Hilal", "Engineering", "Python Developer Intern")
    add_employee(102, "Salman", "HR", "Talent Acquisition Specialist")
    add_employee(103, "Rahul", "Marketing", "SEO Analyst")

    display_all_employees()
    input("Press Enter to close this window...")
