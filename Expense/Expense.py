import tkinter as tk

import mysql
from tkcalendar import DateEntry
from tkinter import ttk
import mysql.connector as db


def launch():
    register = tk.Tk()
    register.title("Personal Expense Tracker")
    register.geometry('900x600')
    register.state('zoomed')

    def submit_expense():
        date = dateEntry.get()
        name = NameEntry.get()
        category = selection
        amount = expenseEntry.get()
        values = [date, name, category, amount]
        print(values)
        tree_table.insert('', 'end', values=values)
        try:
            connectionObj = db.connect(
            host="localhost",
            user="root",
            passwd="ammuz$123",
            database="expensemanager"
            )
            curr = connectionObj.cursor()
            queryExpense = '''
                INSERT INTO expense(Date,Payee,Type,Expense) VALUES (%s, %s,%s,%s)
                '''
            params = (date, name, category, amount)
            curr.execute(queryExpense, params)
            connectionObj.commit()
        except Exception as e:
            print(e)
        else:
            curr.close()
            connectionObj.close()


    dateLabel = tk.Label(register, text="Date", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
    dateLabel.grid(row=0, column=0, padx=6, pady=6)

    dateEntry = DateEntry(register, width=12, font=('arial', 15, 'bold'), date_pattern='YYYY-MM-DD')
    dateEntry.grid(row=0, column=1, padx=5, pady=5)
    print(dateEntry.get())

    Name = tk.StringVar()
    Name.set("Rajeev")
    nameLabel = tk.Label(register, text="Name", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
    nameLabel.grid(row=1, column=0, padx=6, pady=6)

    NameEntry = tk.Entry(register, textvariable=Name, font=('arial', 15, 'bold'), width=14)
    NameEntry.grid(row=1, column=1, padx=6, pady=6)
    print(NameEntry.get())

    typeLabel = tk.Label(register, text="Type", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white", width=12)
    typeLabel.grid(row=2, column=0, padx=6, pady=6)
    # Dropdown menu options
    options = [
        "Grocery",
        "OnlineShopping",
        "Recharge",
        "Entertainment",
        "Shopping",
        "Bills",
    ]

    variable = tk.StringVar(register)
    variable.set(options[0])  # default value

    typeOption = tk.OptionMenu(register, variable, *options)
    typeOption.grid(row=2, column=1, padx=6, pady=6)
    typeOption.config(font=('arial', 15, 'bold'), width=13)
    selection = variable.get()
    print(selection)
    Expense = tk.IntVar()
    expenseLabel = tk.Label(register, text="Expense", font=('arial', 15, 'bold'), bg="DodgerBlue2", fg="white",
                            width=12)
    expenseLabel.grid(row=4, column=0, padx=6, pady=6)

    expenseEntry = tk.Entry(register, textvariable=Expense, font=('arial', 15, 'bold'), width=12)
    expenseEntry.grid(row=4, column=1, padx=7, pady=7)

    buttonAdd = tk.Button(register, command=submit_expense, text="Submit",
                          font=('arial', 15, 'bold'), bg="black",
                          fg="white", width=12)
    buttonAdd.grid(row=5, column=1, padx=6, pady=6)

    # saved expenses--------------
    tree_list = ['Date', 'Name', 'Type', 'Expense']
    s = ttk.Style()
    s.theme_use(themename="clam")
    tree_table = ttk.Treeview(register, column=tree_list, show='headings', height=7)
    tree_table.column("# 2", anchor='center', stretch='n')
    for c in tree_list:
        tree_table.heading(c, text=c.title())
    tree_table.grid(row=7, column=0, padx=6, pady=6, columnspan=3)
    register.mainloop()



