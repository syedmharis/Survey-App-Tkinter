import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter import PhotoImage
import statistics

#Main class
class SculptureForm(tk.Tk):

    def __init__(self):
        super().__init__()

        self.data = []
        #Adds title to app
        self.title("Sculpture Survey")

        #Adds Heading to the app
        self.heading = ttk.Label(self, text="Sculpture Viewer Survey", font=("Arial", 20))
        self.heading.grid(row=0, column=0, columnspan=2, pady=20, ipadx=50)
        self.heading.config(anchor="center")
        
        # Shows the sculpture image
        self.image = PhotoImage(file="sculpture.png") 
        self.heading = ttk.Label(self, image=self.image)
        self.heading.grid(row=1, column=0, columnspan=2, pady=20)
        
        #Ask for name
        self.name_label = ttk.Label(self, text="Name :")
        self.name_entry = ttk.Entry(self)

        #Ask for age 
        self.age_label = ttk.Label(self, text="Age :")
        self.age_entry = ttk.Entry(self)

        #Selection for sex
        self.sex_label = ttk.Label(self,text="Choose Your Sex")
        self.sex_var = tk.StringVar()
        self.sex_male = ttk.Radiobutton(self, text="Male", variable=self.sex_var, value="Male")
        self.sex_female = ttk.Radiobutton(self, text="Female", variable=self.sex_var, value="Female")
        self.sex_other = ttk.Radiobutton(self, text="Others", variable=self.sex_var, value="Others")


        #Selection for ethnicity
        self.ethnicity_label = ttk.Label(self, text="Choose your Ethinicity :")
        self.ethnicity_var = tk.StringVar()
        self.ethnicity_white = ttk.Radiobutton(self, text="White", variable=self.ethnicity_var, value="White")
        self.ethnicity_black = ttk.Radiobutton(self, text="Black", variable=self.ethnicity_var, value="Black")
        self.ethnicity_chinese = ttk.Radiobutton(self, text="Chinese", variable=self.ethnicity_var, value="Chinese")
        self.ethnicity_asian = ttk.Radiobutton(self, text="Asian", variable=self.ethnicity_var, value="Asian")
        self.ethnicity_other = ttk.Radiobutton(self, text="Other", variable=self.ethnicity_var, value="Other")

        #Selection for dstatus
        self.dstatus_label = ttk.Label(self,text="Disabled Status")
        self.dstatus_var = tk.StringVar()
        self.dtatus_notdisabled = ttk.Radiobutton(self, text="Not Disabled", variable=self.dstatus_var, value="Not Disabled")
        self.dstatus_disabled = ttk.Radiobutton(self, text="Disabled", variable=self.dstatus_var, value="Disabled")

        #Selection for dstatus
        self.reaction_label = ttk.Label(self, text="Reaction to Sculpture :")
        self.reaction_var = tk.StringVar()
        self.reaction_enjoyed = ttk.Radiobutton(self, text="I enjoyed the Sculpture", variable=self.reaction_var, value="enjoyed")
        self.reaction_curious = ttk.Radiobutton(self, text="I am curious how it works ", variable=self.reaction_var, value="curious")
        self.reaction_knowmore = ttk.Radiobutton(self, text="I want to know more", variable=self.reaction_var, value="knowmore")

        #Submit Buttons
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_form)
        self.submit_button_view = ttk.Button(self, text="View Entries", command=self.view_form)

        #Setting display grid in tkinter app
        self.name_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")
        self.name_entry.grid(row=3, column=1, padx=5, pady=5)

        self.age_label.grid(row=4, column=0, padx=5, pady=5, sticky="W")
        self.age_entry.grid(row=4, column=1, padx=5, pady=5)

        self.sex_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="W")
        self.sex_male.grid(row=6, column=0, padx=5, pady=5, sticky="W")
        self.sex_female.grid(row=6, column=1, padx=5, pady=5, sticky="W")
        self.sex_other.grid(row=6, column=2, padx=5, pady=5, sticky="W")

        self.ethnicity_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="W")
        self.ethnicity_white.grid(row=8, column=0, padx=5, pady=5, sticky="W")
        self.ethnicity_black.grid(row=8, column=1, padx=5, pady=5, sticky="W")
        self.ethnicity_chinese.grid(row=8, column=2, padx=5, pady=5, sticky="W")
        self.ethnicity_asian.grid(row=8, column=3, padx=5, pady=5, sticky="W")
        self.ethnicity_other.grid(row=8, column=4, padx=5, pady=5, sticky="W")

        self.dstatus_label.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="W")
        self.dtatus_notdisabled.grid(row=10, column=0, padx=5, pady=5, sticky="W")
        self.dstatus_disabled.grid(row=10, column=1, padx=5, pady=5, sticky="W")

        self.reaction_label.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="W")
        self.reaction_enjoyed.grid(row=12, column=0, padx=5, pady=5, sticky="W")
        self.reaction_curious.grid(row=12, column=1, padx=5, pady=5, sticky="W")
        self.reaction_knowmore.grid(row=12, column=2, padx=5, pady=5, sticky="W")

        self.submit_button.grid(row=13, column=0, padx=20, pady=10)
        self.submit_button_view.grid(row=13, column=1, padx=20, pady=10)

    #Checks password for the host view form    
    def check_password(self, entered_password):
        if entered_password == 'manchester':
            self.create_treeview()
        else:
            messagebox.showerror("Incorrect Password", "Please enter the correct password.")

    # For the Host to View Data Submitted.
    def view_form(self):

        self.view_entries = tk.Toplevel(self)
        self.view_entries.geometry("800x400")
        self.view_entries.title("View Entries")

        #Ask for password
        password_label = ttk.Label(self.view_entries, text="Enter Password: (manchester) ")
        password_entry = ttk.Entry(self.view_entries, show='*')
        password_label.pack()
        password_entry.pack()

        #Submits the entered password and Calls the check Pass Method.
        password_submit_button = ttk.Button(self.view_entries, text="Submit", command=lambda: self.check_password(password_entry.get()))
        password_submit_button.pack()

    #Creates a view if host is allowed to enter
    def create_treeview(self):

        self.tree = ttk.Treeview(self.view_entries, columns=("Name", "Age", "Sex", "Ethnicity", "Disabled Status", "Reaction"))
        self.tree.heading("#0", text="S.No")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Sex", text="Sex")
        self.tree.heading("Ethnicity", text="Ethnicity")
        self.tree.heading("Disabled Status", text="Disabled Status")
        self.tree.heading("Reaction", text="Reaction")
        self.tree.column("#0", minwidth=0, width=50, stretch=tk.NO)
        self.tree.column("Name", minwidth=0, width=100, stretch=tk.NO)
        self.tree.column("Age", minwidth=0, width=100, stretch=tk.NO)
        self.tree.column("Sex", minwidth=0, width=100, stretch=tk.NO)
        self.tree.column("Ethnicity", minwidth=0, width=100, stretch=tk.NO)
        self.tree.column("Disabled Status", minwidth=0, width=100, stretch=tk.NO)
        self.tree.column("Reaction", minwidth=0, width=100, stretch=tk.NO)
        self.tree.pack()

        # Collect data for statistics
        ages = [entry['age'] for entry in self.data]
        females = [entry for entry in self.data if entry['sex'] == 'Female']
        males = [entry for entry in self.data if entry['sex'] == 'Male']
        
        # Calculate statistics
        
        female_count = len(females)
        male_count = len(males)

        #Error checks because stats are derived from 2 values
        if female_count >= 2:
            average_age = statistics.mean(ages)
            age_stdev = statistics.stdev(ages)
            statistics_label = ttk.Label(self.view_entries, text=f" Average age : {average_age}\n Female count : {female_count}\n Male count : {male_count}\n Age standard deviation : {age_stdev}")
            statistics_label.pack()

        # Display statistics
        else :
            statistics_label = ttk.Label(self.view_entries, text=f" For Statistical Values you need atleast 2 entries.\n Female count : {female_count}\n Male count : {male_count}")
            statistics_label.pack()

        i = 1
        for entry in self.data:
            self.tree.insert('', 'end', text=i, values=(entry['name'], entry['age'], entry['sex'], entry['ethnicity'], entry['dstatus'], entry['reaction']))
            i += 1

    #Submits and saves the values entered by viewer into data    
    def submit_form(self):

        name = self.name_entry.get()
        age = self.age_entry.get()
        sex = self.sex_var.get()
        ethnicity = self.ethnicity_var.get()
        dstatus = self.dstatus_var.get()
        reaction = self.reaction_var.get()

        # Here error checking for the form fields
        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for your age.")
            return
        
        if name == '' or age == '' or sex == '' or ethnicity == '' or dstatus == '' or reaction == '':
            messagebox.showerror("Error", "Please fill all fields!")

        else:
            self.data.append({
                'name': name,
                'age': age,
                'sex': sex,
                'ethnicity': ethnicity,
                'dstatus': dstatus,
                'reaction': reaction
            })
            
            messagebox.showinfo("Success", "Your data has been saved successfully.")

            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.sex_var.set(None)
            self.ethnicity_var.set(None)
            self.dstatus_var.set(None)
            self.reaction_var.set(None) 
       


if __name__ == "__main__":
    form = SculptureForm()
    form.mainloop()
