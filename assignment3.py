import pymongo
from bson import ObjectId
from datetime import datetime

try:
    connection = pymongo.MongoClient("localhost", 27017)
    database = connection["myDB"]
    Expense = database['myExpense']
except Exception as err:
    print("Connection error:", err)

class PersonalExpenseTracker:
    def first_option(self):
        print("""\nPersonal Expense Tracker
************************************************
1. Add New Expense
2. View All Expenses
3. View Total Expenses
4. Delete an Expense
5. Exit
              """)
        try:
            option = int(input("Please select your option from 1 to 5: "))
            options = {
                1: self.Add_New_Expense,
                2: self.View_All_Expense,
                3: self.View_Total_Expense,
                4: self.Delete_an_Expense,
                5: exit
            }
            options.get(option, lambda: print("Invalid input, please enter the number from 1 to 5"))()
        except ValueError:
            print("Invalid input, please enter the number from 1 to 5")

    def get_expense_details(self):
        description = input("Enter description of expense: ")
        try:
            amount = float(input("Enter the expense amount: "))
            if amount < 0:
                print("Invalid amount, please enter a positive number.")
                return None, None, None
        except ValueError:
            print("Please enter a valid number for amount.")
            return None, None, None

        try:
            date_input = input("Enter Date (YYYY-MM-DD): ")
            date = datetime.strptime(date_input, "%Y-%m-%d")
            return description, amount, date
        except ValueError:
            print("Invalid Date Format, please enter again.")
            return None, None, None

    def Add_New_Expense(self):
        description, amount, date = self.get_expense_details()
        if description and amount is not None and date:
            expense_form = {'Description': description, 'Amount': amount, 'Date': date}
            try:
                Expense.insert_one(expense_form)
                print("Expense added successfully.")
            except Exception as arr:
                print("Something went wrong:", arr)

    def View_All_Expense(self):
        try:
            data = Expense.find()
            for expense in data:
                expense['_id'] = str(expense['_id'])
                print(", ".join(f"{key}: {value}" for key, value in expense.items()))
        except Exception as err:
            print("Error viewing expenses:", err)

    def View_Total_Expense(self):
        try:
            total = sum(expense['Amount'] for expense in Expense.find({}, {'Amount': 1}))
            print("Total Expenses:", total)
        except Exception as err:
            print("Error calculating total expenses:", err)

    def Delete_an_Expense(self):
        delete_id = input("Please enter the ID of the expense to delete: ")
        try:
            object_id = ObjectId(delete_id)
            result = Expense.delete_one({'_id': object_id})
            if result.deleted_count:
                print("Delete is successful.")
            else:
                print("ID not found. Please enter a valid ID.")
        except Exception as err:
            print("Error deleting expense:", err)

if __name__ == "__main__":
    personal_expense_tracker = PersonalExpenseTracker()
    while True:
        personal_expense_tracker.first_option()
