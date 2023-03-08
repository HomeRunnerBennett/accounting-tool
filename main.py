import tkinter as tk
import sqlite3

conn = sqlite3.connect('accounting_system.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users(username text, password text, role text)''')
c.execute('''INSERT INTO users(username, password, role) VALUES('admin', 'admin1234', 'admin')''')

c.execute('''CREATE TABLE IF NOT EXISTS accounting_data(date text, description text, amount real, account_type text)''')

c.execute('''CREATE TABLE IF NOT EXISTS reports(report_type text, report_data text)''')

root = tk.Tk()
root.title("Accounting System")
root.geometry("1080x720")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Zoom In")
view_menu.add_command(label="Zoom Out")

report_menu = tk.Menu(menu_bar, tearoff=0)
report_menu.add_command(label="Statement of Comprehensive Income")
report_menu.add_command(label="Statement of Financial Position")
report_menu.add_command(label="Statement of Cashflow")
report_menu.add_command(label="Statement of Changes in Equity")

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="View", menu=view_menu)
menu_bar.add_cascade(label="Report", menu=report_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

user_label = tk.Label(root, text="User: admin")
user_label.pack()

options_frame = tk.Frame(root)
options_frame.pack(side=tk.LEFT, fill=tk.Y)

overviews_button = tk.Button(options_frame, text="Overviews")
overviews_button.pack(side=tk.TOP)

reports_button = tk.Button(options_frame, text="Reports")
reports_button.pack(side=tk.TOP)

accounts_button = tk.Button(options_frame, text="Accounts Payable and Receivable")
accounts_button.pack(side=tk.TOP)

budget_button = tk.Button(options_frame, text="Budget Vs Actual")
budget_button.pack(side=tk.TOP)

kpi_button = tk.Button(options_frame, text="Key Performance Indicators")
kpi_button.pack(side=tk.TOP)

content_frame = tk.Frame(root)
content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

def login():
    username = username_entry.get()
    password = password_entry.get()
    c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result is not None:
        role = result[0]
        show_feature(role)
    else:
        error_label.config(text="Invalid username or password")

def show_feature(role):
    global content_frame
    content_frame.destroy()
    content_frame = tk.Frame(root)
    content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    if role == "admin":
        show_reports()
    elif role == "accountant":
        show_overviews()

def show_feature(role):
    if role == "admin":
        show_reports()
    elif role == "accountant":
        show_overviews()

def show_reports():
    # code for showing reports here
    pass

    content_frame.destroy()
    content_frame = tk.Frame(root)
    content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    report_label = tk.Label(content_frame, text="Reports")
    report_label.pack()

def show_overviews():
    global content_frame
    content_frame.destroy()
    content_frame = tk.Frame(root)
    content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    overview_label = tk.Label(content_frame, text="Overviews")
    overview_label.pack()

login_frame = tk.Frame(root)
login_frame.pack(side=tk.TOP)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

error_label = tk.Label(login_frame, fg="red")
error_label.grid(row=3, column=0, columnspan=2)

# Start the GUI
root.mainloop()
# Close the database connection
conn.close()

# Implement the functions for the different input forms
def input_form_1():
    # Code for input form 1
    pass

def input_form_2():
    # Code for input form 2
    pass

def input_form_3():
    # Code for input form 3
    pass

# Create the input forms toolbar
input_forms_frame = tk.Frame(root)
input_forms_frame.pack(side=tk.LEFT, fill=tk.Y)

input_forms_label = tk.Label(input_forms_frame, text="Input Forms")
input_forms_label.pack()

input_form_1_button = tk.Button(input_forms_frame, text="Input Form 1", command=input_form_1)
input_form_1_button.pack(side=tk.TOP)

input_form_2_button = tk.Button(input_forms_frame, text="Input Form 2", command=input_form_2)
input_form_2_button.pack(side=tk.TOP)

input_form_3_button = tk.Button(input_forms_frame, text="Input Form 3", command=input_form_3)
input_form_3_button.pack(side=tk.TOP)

# Allow importing of Excel spreadsheets into the input forms
def import_spreadsheet():
    # Code for importing Excel spreadsheet
    pass
import_button = tk.Button(input_forms_frame, text="Import Spreadsheet", command=import_spreadsheet)
import_button.pack(side=tk.BOTTOM)
# Add the logout button
def logout():
    # Code for logging out
    pass

logout_button = tk.Button(root, text="Logout", command=logout)
logout_button.pack(side=tk.BOTTOM)

#Add the user name label
user_name = "John Doe" # Replace with actual user name
user_name_label = tk.Label(root, text="User: " + user_name)
user_name_label.pack(side=tk.TOP, anchor=tk.NE)

#Implement the functions for the different features
def overviews():
    # Code for displaying overviews
    pass

def reports():
    # Code for displaying reports
    pass

def accounts_payable_and_receivable():
    # Code for displaying accounts payable and receivable
    pass
def budget_vs_actual():
    # Code for displaying budget vs actual
    pass

def key_performance_indicators():
    # Code for displaying key performance indicators
    pass

#Create the features toolbar
features_frame = tk.Frame(root)
features_frame.pack(side=tk.LEFT, fill=tk.Y)

features_label = tk.Label(features_frame, text="Features")
features_label.pack()

overviews_button = tk.Button(features_frame, text="Overviews", command=overviews)
overviews_button.pack(side=tk.TOP)

reports_button = tk.Button(features_frame, text="Reports", command=reports)
reports_button.pack(side=tk.TOP)

accounts_payable_and_receivable_button = tk.Button(features_frame, text="Accounts Payable and Receivable", command=accounts_payable_and_receivable)
accounts_payable_and_receivable_button.pack(side=tk.TOP)

budget_vs_actual_button = tk.Button(features_frame, text="Budget vs Actual", command=budget_vs_actual)
budget_vs_actual_button.pack(side=tk.TOP)

key_performance_indicators_button = tk.Button(features_frame, text="Key Performance Indicators", command=key_performance_indicators)
key_performance_indicators_button.pack(side=tk.TOP)
