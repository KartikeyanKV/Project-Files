from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

class AttendanceSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Face Recognition Attendance System")
        self.geometry("1000x700")
        self.configure(bg='black')

        # Centered Header
        self.header_frame = tk.Frame(self, bg='black')
        self.header_frame.pack(fill=tk.X, pady=10)

        self.title_label = tk.Label(self.header_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", bg='black', fg='red', font=('Arial', 28, 'bold'))
        self.title_label.pack(pady=20)
        
      

        # Main container
        self.container = tk.Frame(self, bg='black')
        self.container.pack(pady=20)

        # Grid for cards
        self.grid_frame = tk.Frame(self.container, bg='black')
        self.grid_frame.grid(row=0, column=0)

        # Create buttons with the respective images
        self.create_card("Student Details", "C:/Users/admin/Pictures/sp.jpg", "ad-C:/Users/admin/Pictures/sp.jpg", 0, 0)
        self.create_card("Face Recognition", "face.png", "ad-facerec.png", 0, 1)
        self.create_card("Attendance", "attendance.png", "ad-attendance.png", 0, 2)
        self.create_card("Chatbot", "chatbot.png", "ad-chatbot.png", 0, 3)
        self.create_card("Train Data", "train.png", "ad-traindata.png", 1, 0)
        self.create_card("Photos", "photos.png", "ad-photos.png", 1, 1)
        self.create_card("Developer", "developer.png", "ad-developer.png", 1, 2)
        self.create_card("Exit", "exit.png", "ad-exit.png", 1, 3)

    def create_card(self, title, img_path, ad_path, row, column):
        card_frame = tk.Frame(self.grid_frame, bg='black', borderwidth=2, relief=tk.RAISED)
        card_frame.grid(row=row, column=column, padx=20, pady=20, sticky="nsew")

        # Advertisement image (larger image above the button)
        try:
            ad_img = Image.open(ad_path)
            ad_img = ad_img.resize((150, 150), Image.ANTIALIAS)
            ad_photo = ImageTk.PhotoImage(ad_img)
            ad_label = tk.Label(card_frame, image=ad_photo, bg='black')
            ad_label.image = ad_photo  # keep a reference to avoid garbage collection
            ad_label.pack(pady=5)
        except Exception as e:
            print(f"Error loading advertisement image: {e}")

        # Main button image (icon for the button itself)
        try:
            img = Image.open(img_path)
            img = img.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(card_frame, image=photo, bg='black')
            img_label.image = photo  # keep a reference
            img_label.pack(pady=10)
        except Exception as e:
            print(f"Error loading main image: {e}")

        # Button below the image
        btn = tk.Button(card_frame, text=title, command=lambda: self.button_click(title), bg='#007bff', fg='white', font=('Arial', 16), padx=10, pady=5)
        btn.pack(pady=10)

        card_frame.grid_columnconfigure(0, weight=1)  # Ensure the card is centered in the grid

    def button_click(self, title):
        messagebox.showinfo("Button Clicked", f"You clicked on {title}")

if __name__ == "__main__":
    app = AttendanceSystem()
    app.mainloop()
