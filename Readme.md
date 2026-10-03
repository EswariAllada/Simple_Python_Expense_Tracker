#  Expense Tracker

A simple Python-based Expense Tracker that allows users to add, view, calculate, and delete expenses. The project stores expense data permanently using JSON and displays expenses in a clean Pandas DataFrame.

##  Features

* ➕ Add new expenses
* 📋 View all expenses using Pandas DataFrame
* 💰 Calculate total expenses
* 🗑️ Delete expenses
* 💾 Store expenses permanently using JSON
* 🔄 Load previously saved expenses when the program starts
* 🐍 Built completely with Python

##  Technologies Used

* **Python**
* **JSON** – for permanent data storage
* **Pandas** – for displaying and working with expense data

##  Project Structure

expense_tracker/
│
├── main.py
├── expenses.json
├── README.md


> `expenses.json` is created/updated automatically when expenses are added or deleted.

## ⚙️ How It Works

When the application starts, it checks for an existing `expenses.json` file.

Start Program
     ↓
Load existing expenses
     ↓
Display Menu
     ↓
Add / View / Total / Delete
     ↓
Update expenses.json

### 1. Add Expense

The user enters:

* Date
* Category
* Description
* Amount

The expense is stored as a Python dictionary and added to the expenses list.

### 2. View Expenses

The stored expenses are converted into a Pandas DataFrame.


### 3. Total Expenses

The application calculates the total amount spent by adding the amount of each expense.

### 4. Delete Expense

The user selects an expense number, and the corresponding expense is removed from the list.

The updated data is then saved back to `expenses.json`.

##  Data Persistence

The project uses JSON to make expense data persistent.
Unlike a normal Python list, which disappears when the program closes, the JSON file keeps the data stored.

##  Learning Outcomes

Through this project, I practiced:

* Python fundamentals
* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions
* File handling
* JSON data storage
* CRUD operations
* Pandas DataFrames
* Basic project organization

##  Future Improvements

Possible future enhancements include:

* 📊 Expense visualization using charts
* 🔎 Search and filter expenses
* 📅 Monthly expense summaries
* 📤 Export expenses to CSV
* 🗄️ SQLite database integration
* 🌐 Convert the application into a web application
* 📱 Add a graphical user interface

##  Author

**Eswari**

B.Tech – Computer Science & Engineering (AI & ML)


