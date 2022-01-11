import tkinter as tk
from tkinter.filedialog import askopenfilename

from PIL import ImageTk, Image


window = tk.Tk()
window.geometry('900x675')
window.title('GAN GUI')
window.configure(bg='#4a7a8c')

# set up frames
frame = tk.Frame(window)
frame.pack()
frame.configure(bg='#4a7a8c')

leftframe = tk.Frame(window)
leftframe.pack(side='left', pady=1)
leftframe.configure(bg='#4a7a8c')

label = tk.Label(frame, text = "GAN GUI",font=('Helvetica bold', 11), width=40, height=2, bg='#4a7a8c')
label.pack(pady=30)

path = None
# # functions
def clicked():
    file_name.insert(string="button was clicked!")
    file_name.insert()

def open_files():
    selected_path = askopenfilename(title="Select a file", filetypes=(("Picture files", "*.png;*.bmp;*.jpg"),
                                               ("All files", "*.*") ))
    global path
    path = selected_path
    file_name.configure(text='File chosen: {}'.format(path))
    pass

def load_and_display():
    img = ImageTk.PhotoImage(Image.open(path).resize((350, 300)))
    label_img.configure(image=img)
    label_img.image = img
    pass


# #Create an Empty Label to Read the name of the File
file_name = tk.Label(frame,text='Choose a file...', borderwidth=3, relief='sunken', width=50, height=2)
file_name.pack(pady=5, padx=20, side='left')

# # buttons
# #Create a button for opening files
file_button = tk.Button(frame, text="Open...",command=open_files, width=10, height=2, bg='black', fg='white')
file_button.pack(pady=5, side='left')

bt = tk.Button(leftframe, command = load_and_display,width=20, height=2, 
                 text = 'Load Image', bg='yellow', fg='red')
bt.pack( padx=10, pady=20)

bt2 = tk.Button(leftframe, command = clicked,width=20, height=2, text = 'Run GFP-GAN',  bg='green', fg='white')
bt2.pack(padx=10, pady=20)

bt3 = tk.Button(leftframe, command = clicked,width=20, height=2, text = 'Run RealESRGAN', bg='blue', fg='white')
bt3.pack( padx=10, pady=20)

bt4 = tk.Button(leftframe, command = clicked,width=20, height=2, text = 'Save Image (.PNG)', bg='black', fg='red')
bt4.pack( padx=10, pady=20)

# # bt5 = tk.Button(window, text = 'Quit !', command = window.destroy, width=20, height=1, bg='red', fg='white', widt)
# # bt5.grid(row = 30, column = 9, padx=5, pady=10)

# # Create image box
img = ImageTk.PhotoImage(Image.open('E:/Projects/Freelancing/GFPGAN-prototype/main/assets/BramwelOchieng Headshot.jpg').resize((350, 300)))

label_img = tk.Label(window, image=img)
label_img.pack(padx=5, pady=20, side='left')

label_img2 = tk.Label(window, image=img)
label_img2.pack(padx=5, pady=20, side='left')



window.mainloop()