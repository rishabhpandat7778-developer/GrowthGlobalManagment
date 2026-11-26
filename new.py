import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
import io

user_data = {}

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=6, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    return img

def show_last_window():
    second.destroy()
    last = tk.Tk()
    last.title("Confirmation")
    last.attributes('-fullscreen', True)
    last.config(bg="#f0f8ff")

    tk.Label(last, text="🎉 Registration Successful!", font=("Helvetica", 26, "bold"), bg="#f0f8ff", fg="#2e8b57").pack(pady=40)

    data_text = "\n".join([f"{k}: {v}" for k, v in user_data.items()])
    img = generate_qr_code(data_text)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    img = Image.open(img_bytes)
    img_tk = ImageTk.PhotoImage(img)

    tk.Label(last, text="Here is your QR Code Membership ID", font=("Helvetica", 18), bg="#f0f8ff").pack(pady=10)
    tk.Label(last, image=img_tk, bg="#f0f8ff").pack(pady=20)

    def exit_app():
        last.destroy()

    tk.Button(last, text="Exit", command=exit_app, font=("Helvetica", 14), bg="#dc143c", fg="white").pack(pady=30)

    last.mainloop()

def open_form_window():
    global second, name_var, age_var, email_var, phone_var, gender_var, fitness_var

    second = tk.Tk()
    second.title("Membership Form")
    second.attributes('-fullscreen', True)
    second.config(bg="#eaf4f4")

    name_var = tk.StringVar()
    age_var = tk.StringVar()
    email_var = tk.StringVar()
    phone_var = tk.StringVar()
    gender_var = tk.StringVar()
    fitness_var = tk.StringVar()

    def create_field(label, variable):
        tk.Label(second, text=label, bg="#eaf4f4", font=("Helvetica", 16)).pack(pady=5)
        tk.Entry(second, textvariable=variable, font=("Helvetica", 14)).pack(pady=5)

    tk.Label(second, text="🏋️‍♂️ Membership Registration 🏋️‍♀️", font=("Helvetica", 30, "bold"), fg="white", bg="#ff6600").pack(pady=30)

    create_field("Full Name", name_var)
    create_field("Age", age_var)
    create_field("Email", email_var)
    create_field("Phone", phone_var)

    tk.Label(second, text="Gender", bg="#eaf4f4", font=("Helvetica", 16)).pack()
    tk.Radiobutton(second, text="Male", variable=gender_var, value="Male", bg="#eaf4f4", font=("Helvetica", 14)).pack()
    tk.Radiobutton(second, text="Female", variable=gender_var, value="Female", bg="#eaf4f4", font=("Helvetica", 14)).pack()

    tk.Label(second, text="Fitness Level", bg="#eaf4f4", font=("Helvetica", 16)).pack()
    tk.Radiobutton(second, text="Beginner", variable=fitness_var, value="Beginner", bg="#eaf4f4", font=("Helvetica", 14)).pack()
    tk.Radiobutton(second, text="Intermediate", variable=fitness_var, value="Intermediate", bg="#eaf4f4", font=("Helvetica", 14)).pack()
    tk.Radiobutton(second, text="Pro", variable=fitness_var, value="Pro", bg="#eaf4f4", font=("Helvetica", 14)).pack()

    def submit_form():
        name = name_var.get().strip()
        age = age_var.get().strip()
        email = email_var.get().strip()
        phone = phone_var.get().strip()
        gender = gender_var.get()
        fitness = fitness_var.get()

        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Invalid Name", "Full Name should contain only letters and spaces.")
            return
        if not age.isdigit() or int(age) < 18 and age=="":
            messagebox.showerror("Invalid Age", "Age must be a number and 18 or above and not be blank.")
            return
        if not phone.isdigit() or len(phone) != 10 and phone=="":
            messagebox.showerror("Invalid Phone", "Phone number must be exactly 10 digits and not be blank.")
            return
        if '@gmail.com' not in email and email=="":
            messagebox.showerror("Invalid Email", "Email must contain '@gmail' and not be blank.")
            return
        user_part = email.split('@')[0]
        if len(user_part) < 8 or not user_part.isalpha():
            messagebox.showerror("Invalid Email", "Email must have at least 8 alphabetic characters before '@'.")
            return
        if gender not in ["Male", "Female"]:
            messagebox.showerror("Missing Gender", "Please select a gender.")
            return
        if fitness not in ["Beginner", "Intermediate", "Pro"]:
            messagebox.showerror("Missing Fitness Level", "Please select a fitness level.")
            return

        user_data["Name"] = name
        user_data["Age"] = age
        user_data["Email"] = email
        user_data["Phone"] = phone
        user_data["Gender"] = gender
        user_data["Fitness Level"] = fitness

        show_last_window()

    tk.Button(second, text="Submit", command=submit_form, bg="#4caf50", fg="white", font=("Helvetica", 16)).pack(pady=30)

    tk.Button(second, text="Back", command=second.destroy, bg="#888", fg="white", font=("Helvetica", 14)).pack()

    second.mainloop()

def open_welcome_window():
    root = tk.Tk()
    root.title("Welcome to Gym")
    root.attributes('-fullscreen', True)
    root.config(bg="#d1e0e0")

        
    try:
        image = Image.open("image.jpg")
        image = image.resize((800, 400), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)
        tk.Label(root, image=image_tk, bg="#d1e0e0").pack(pady=30)
    except Exception as e:
        tk.Label(root, text="Image could not be loaded", font=("Helvetica", 14), fg="red", bg="#d1e0e0").pack(pady=20)

    tk.Label(root, text="Welcome to Our Fitness Club", font=("Helvetica", 28, "bold"), bg="#d1e0e0", fg="#333").pack(pady=20)
    tk.Button(root, text="Register Now", command=lambda: [root.destroy(), open_form_window()],
              font=("Helvetica", 16), bg="#2196f3", fg="white", padx=20, pady=10).pack(pady=40)

    root.mainloop()

open_welcome_window()
