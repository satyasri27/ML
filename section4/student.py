"""Student Record Manager (Self Evaluation)

Objective:
Build a small console application to practice Python fundamentals using a real-world scenario.
What you will build:
A menu-driven program to manage student records.
What to do:
Create a console menu that runs in a loop until the user exits.
Your program should support
Add a student record with name and marks
View all student records
Search a student by name
Update a student’s marks
Delete a student record
Save records to a file
Load records automatically when the program starts
Handle invalid inputs gracefully
Rules:
Use Python only
Use a class-based approach
Use a list or dictionary for storage
Use file handling for persistence"""

HISTORY_FILE = "student.txt"
class Student:
    def __init__(self):
         self.history = self.load_history()
    def load_history(self):
        data = {}
        try:
            with open(HISTORY_FILE,"r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        name, marks = line.split(",")
                        data[name] = int(marks)            
        except FileNotFoundError:
            pass
        return data
    def save_history(self):
        with open(HISTORY_FILE, "w") as file:
            for name, marks in self.history.items():
                file.write(f"{name},{marks}\n")
    def add_student(self):
        name = input("enter name: ")
        try:
            marks = int(input("enter marks: "))
        except ValueError:
            print("eneter valid numbers")
            return
        self.history[name] = marks
        self.save_history()
        print("sudent added successfully")
    def view_students(self):
        if not self.history:
            print("no records found")
        else:
            for name, marks in self.history.items():
                print(name, marks)
    def search_student(self):
        name = input("enter student name: ")
        if name in self.history:
            print(f"{name}, {self.history[name]}")
        else:
            print("student not found")
    def update_marks(self):
        name = input("enter student name: ")
        if name in self.history:
            new_marks = int(input("give new marks: "))
            self.history[name] = new_marks
            self.save_history()
            print(f"sucessfully update the marks for the student {name}")
        else:
            print("student not found")
    def delete_student(self):
        name = input("enter the student name: ")
        if name in self.history:
            del self.history[name]
            self.save_history()
            print(f"student named {name} is deleted")
        else:
            print("student not found")

def main():
    manager = Student()
    while True:
        print("\n student manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("enter choice: ")
        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_marks()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            manager.save_history()
            print("GoodBye, History saved")
            break
        else:
            print("invalid choice, try again")

if __name__ =="__main__":
    main()





