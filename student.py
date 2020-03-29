from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text = "Sistema de Gestión Escolar", bd = 10, relief = GROOVE, font =("arial", 40, "bold"), 
        bg = "black", fg = "gray")
        title.pack(side = TOP, fill = X)

#============ Management Frame =====================
        Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "gray")
        Manage_Frame.place(x = 20, y = 100, width = 450, height = 600)

        m_title = Label(Manage_Frame, text = "Gestor Estudiantil", bg = "gray",fg = "black",font =("arial", 30, "bold"))
        m_title.grid(row = 0, columnspan = 2, pady = 10)

        #============ Role =====================

        lbl_role = Label(Manage_Frame, text = "Clave Única",bg = "gray", fg="black", font =("arial", 15, "bold"))
        lbl_role.grid(row=1, column=0, pady=10, padx=20, sticky = "w")

        txt_role = Entry(Manage_Frame, font=("arial", 15, "bold"), bd = 5, relief = GROOVE)
        txt_role.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        #============ Name =====================

        lbl_name = Label(Manage_Frame, text="Nombre", bg="gray",fg="black", font=("arial", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        #============ Email =====================

        lbl_Email = Label(Manage_Frame, text="Email", bg="gray",fg="black", font=("arial", 15, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        #============ Gender =====================

        lbl_Gender = Label(Manage_Frame, text="Género", bg="gray",fg="black", font=("arial", 15, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, font=("arial", 14, "bold"), state='readonly')
        combo_gender['values'] = ("Masculino","Femenino", "Otro")
        combo_gender.grid(row=4, column=1, padx=34, pady=10)

        #============ Contact =====================

        lbl_Contact = Label(Manage_Frame, text="Contacto",bg="gray", fg="black", font=("arial", 15, "bold"))
        lbl_Contact.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        #============ Date of Birth =====================
        lbl_DOB = Label(Manage_Frame, text="Fecha Nacimiento",bg="gray", fg="black", font=("arial", 15, "bold"))
        lbl_DOB.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        #============ Address =====================
        lbl_Address = Label(Manage_Frame, text="Dirección", bg="gray",fg="black", font=("arial", 15, "bold"))
        lbl_Address.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_Address = Text(Manage_Frame, width = 28, height = 4, font = ("", 10))
        txt_Address.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        #============ Button Frame =====================
        Button_Frame = Frame(Manage_Frame, bd = 4, relief = RIDGE, bg = "gray")
        Button_Frame.place(x = 10, y = 500, width = 430)

        Addbutton = Button(Button_Frame, text = "Agregar", width = 7).grid(row = 0, column = 0, padx = 10, pady = 10)
        Updatebutton = Button(Button_Frame, text = "Actualizar", width = 7).grid(row = 0, column = 1, padx = 10, pady = 10)
        Deletebutton = Button(Button_Frame, text = "Borrar", width = 7).grid(row = 0, column = 2, padx = 10, pady = 10)
        Clearbutton = Button(Button_Frame, text = "Limpiar", width = 7).grid(row=0, column=3, padx=10, pady=10)

#============ Detail Frame =====================
        Detail_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "gray")
        Detail_Frame.place(x = 500, y = 100, width = 720, height = 600)

        lbl_Search = Label(Detail_Frame, text="Buscar",bg="gray", fg="white", font=("arial", 15, "bold"))
        lbl_Search.grid(row = 0, column = 0, pady = 10, padx = 20, sticky = "w")

        combo_Search = ttk.Combobox(Detail_Frame, width = 10, font=("arial", 14, "bold"), state='readonly')
        combo_Search['values'] = ("Clave única", "Nombre", "Contacto")
        combo_Search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search = Entry(Detail_Frame, width =  20, font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbutton = Button(Detail_Frame, text="Buscar", width=10, pady = 5).grid(row=0, column=3, padx=10, pady=10)
        Showallbutton = Button(Detail_Frame, text="Mostrar", width=10, pady = 5).grid(row=0, column=4, padx=10, pady=10)

#============ Table Frame =====================

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="gray")
        Table_Frame.place(x=10, y=70, width=696, height=524)

        Scroll_x = Scrollbar(Table_Frame, orient = HORIZONTAL)
        Scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        Student_table = ttk.Treeview(Table_Frame, columns = ("CU","Nombre","Email", "Género", "Contacto","Nacimiento", "Dirección"), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)
        Scroll_x.pack(side = BOTTOM, fill = X)
        Scroll_x.config(command = Student_table.xview)
        Scroll_y.pack(side = RIGHT, fill = Y)
        Scroll_y.config(command=Student_table.yview)
        Student_table.heading("CU", text = "CU No.")
        Student_table.heading("Nombre", text = "Nombre")
        Student_table.heading("Email", text = "Email")
        Student_table.heading("Género", text = "Género")
        Student_table.heading("Contacto", text = "Contacto")
        Student_table.heading("Nacimiento", text = "Nacimiento")
        Student_table.heading("Dirección", text = "Dirección")
        Student_table['show'] = 'headings'
        Student_table.column("CU", width=100)
        Student_table.column("Nombre", width=100)
        Student_table.column("Email", width=100)
        Student_table.column("Género", width=100)
        Student_table.column("Contacto", width=100)
        Student_table.column("Nacimiento", width=100)
        Student_table.column("Dirección", width=100)
        Student_table.pack()
        

root = Tk()
ob = Student(root)
root.mainloop()

