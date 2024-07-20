import tkinter
from tkinter import messagebox
from tkinter import filedialog

def change_theme(theme):
    text_fild["bg"]=view_colors[theme]["text_bg"]
    text_fild["fg"]=view_colors[theme]["text_fg"]
    text_fild["insertbackground"]=view_colors[theme]["cursor"]
    text_fild["selectbackground"]=view_colors[theme]["select_bg"]

def change_font(view_fonts):
    current_size = text_fild.cget("font").split(" ")[-1]
    text_fild.config(font=(fonts[font_name]["font"], current_size))

def change_size(size):
    current_font = text_fild.cget("font").split(" ")[0]
    text_fild.config(font=(current_font, size))

def notepad_exit():
    if messagebox.askokcancel("Выход из приложения", "Вы действительно хотите выйти из приложения?"):
        screen.destroy()

def open_file():
    file_path = filedialog.askopenfilename(title="Выбор файла", filetype=(("Текстовые документы (*.txt)","*.txt"), ("Все файлы", "*.*")))    
    if file_path:
        text_fild.delete("1.0", tkinter.END)
        text_fild.insert("1.0", open(file_path, encoding="utf-8").read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetype=(("Текстовые документы (*.txt)","*.txt"), ("Все файлы", "*.*")))
    f = open(file_path,"w",encoding="utf-8")
    text = text_fild.get("1.0", tkinter.END)
    f.write(text)
    f.close()

screen = tkinter.Tk()
screen.title("Редактор")
screen.geometry(f"700x800+600+100")
screen.configure(bg="white")
screen.protocol("WM_DELETE_WINDOW", notepad_exit)

frame = tkinter.Frame(screen)
frame.pack(fill="both", expand=True)

menu_frame = tkinter.Menu(screen)

file_menu = tkinter.Menu(menu_frame, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
screen.config(menu=file_menu)

view_menu = tkinter.Menu(menu_frame, tearoff=0)
view_menu_sub = tkinter.Menu(view_menu, tearoff=0)
font_menu_sub = tkinter.Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label="Темная", command=lambda:change_theme("dark"))
view_menu_sub.add_command(label="Светлая", command=lambda:change_theme("light"))
view_menu_sub.add_command(label="Серая", command=lambda:change_theme("grey"))
view_menu.add_cascade(label="Тема", menu=view_menu_sub)

font_menu_sub.add_command(label="Arial", command=lambda:change_font("Arial"))
font_menu_sub.add_command(label="Times New Roman", command=lambda:change_font("Times New Roman"))
font_menu_sub.add_command(label="Comic Sans MS", command=lambda:change_font("CSMS"))
font_menu_sub.add_command(label="Calibri", command=lambda:change_font("Calibri"))
view_menu.add_cascade(label="Шрифт", menu=font_menu_sub)
screen.config(menu=view_menu)

font_size = tkinter.Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Размер", menu=font_size)
font_size.add_command(label="8", command=lambda:change_size(8))
font_size.add_command(label="10", command=lambda:change_size(10))
font_size.add_command(label="12", command=lambda:change_size(12))
font_size.add_command(label="14", command=lambda:change_size(14))
font_size.add_command(label="16", command=lambda:change_size(16))
font_size.add_command(label="20", command=lambda:change_size(20))


menu_frame.add_cascade(label="Файл", menu=file_menu)
menu_frame.add_cascade(label="Вид", menu=view_menu)
screen.config(menu=menu_frame)

view_colors = {
    "dark": {
        "text_bg":"black", "text_fg":"white", "cursor":"white", "select_bg": "grey"
    }, 
    "light": {
        "text_bg":"white", "text_fg":"black", "cursor":"black", "select_bg": "blue"
    },
    "grey":{
        "text_bg":"dark grey", "text_fg":"white", "cursor":"white", "select_bg": "grey"
    }
}

fonts = {
    "Arial":{
        "font":"Arial"
    },
    "CSMS":{
        "font":"Comic Sans MS"
    },
    "Times New Roman":{
        "font":"Times New Roman"
    },
    "Calibri":{
        "font": "Calibri"
    }
}

sizes_change = {
    "8":{
        "font": 8
    },
    "10":{
        "font": 10
    },
    "12":{
        "font": 12
    },
    "14":{
        "font": 14
    },
    "16":{
        "font": 16
    },
    "20":{
        "font": 20
    }
}
text_fild = tkinter.Text(frame, padx=10, pady=10, wrap="word",spacing3=10, font="Arial 12")
text_fild.pack(side="left", fill="both", expand=True)

scroll = tkinter.Scrollbar(frame, command=text_fild.yview)
scroll.pack(side="right",fill="y")
text_fild.config(yscrollcommand=scroll.set)

screen.mainloop()