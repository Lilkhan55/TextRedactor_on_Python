import tkinter
from tkinter import messagebox, filedialog
import tkinter.font

format_states = {
    "Bold": False,
    "Italic": False,
    "Underline": False
}

def change_theme(theme):
    text_fild["bg"] = view_colors[theme]["text_bg"]
    text_fild["fg"] = view_colors[theme]["text_fg"]
    text_fild["insertbackground"] = view_colors[theme]["cursor"]
    text_fild["selectbackground"] = view_colors[theme]["select_bg"]

def change_font(view_font):
    current_font = tkinter.font.Font(font=text_fild["font"])
    current_font.config(family=fonts[view_font]["style_font"])
    text_fild.config(font=current_font)

def change_size(size):
    current_font = tkinter.font.Font(font=text_fild["font"])
    current_font.config(size=size)
    text_fild.config(font=current_font)

def change_format(format):
    current_font = tkinter.font.Font(font=text_fild["font"])
    if format == "Bold":
        if format_states["Bold"]:
            current_font.config(weight="normal")
            format_states["Bold"] = False
        else:
            current_font.config(weight="bold")
            format_states["Bold"] = True

    elif format == "Italic":
        if format_states["Italic"]:
            current_font.config(slant="roman")
            format_states["Italic"] = False
        else:
            current_font.config(slant="italic")
            format_states["Italic"] = True

    elif format == "Underline":
        if format_states["Underline"]:
            current_font.config(underline=0)
            format_states["Underline"] = False
        else:
            current_font.config(underline=1)
            format_states["Underline"] = True

    text_fild.config(font=current_font)

def change_position(position):
    start, end = text_fild.index("sel.first"), text_fild.index("sel.last")
    
    if start == end:
        line_index = text_fild.index("insert").split(".")[0]
        start = f"{line_index}.0"
        end = f"{line_index}.end"
    
    text_fild.tag_remove("align", "1.0", "end")
    
    text_fild.tag_configure("align", justify=position)
    text_fild.tag_add("align", start, end)

def notepad_exit():
    if messagebox.askokcancel("Выход из приложения", "Вы действительно хотите выйти из приложения?"):
        screen.destroy()

def open_file():
    file_path = filedialog.askopenfilename(title="Выбор файла", filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))    
    if file_path:
        text_fild.delete("1.0", tkinter.END)
        text_fild.insert("1.0", open(file_path, encoding="windows-1251", errors="ignore").read())

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    if file_path:
        with open(file_path, "w", encoding="windows-1251") as f:
            text = text_fild.get("1.0", tkinter.END)
            f.write(text)

screen = tkinter.Tk()
screen.title("Редактор")
screen.geometry("700x800+600+100")
screen.configure(bg="white")
screen.protocol("WM_DELETE_WINDOW", notepad_exit)

frame = tkinter.Frame(screen)
frame.pack(fill="both", expand=True)

menu_frame = tkinter.Menu(screen)

file_menu = tkinter.Menu(menu_frame, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
menu_frame.add_cascade(label="Файл", menu=file_menu)

view_menu = tkinter.Menu(menu_frame, tearoff=0)

view_menu_sub = tkinter.Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label="Темная", command=lambda: change_theme("dark"))
view_menu_sub.add_command(label="Светлая", command=lambda: change_theme("light"))
view_menu_sub.add_command(label="Серая", command=lambda: change_theme("grey"))
view_menu.add_cascade(label="Тема", menu=view_menu_sub)

font_menu_sub = tkinter.Menu(view_menu, tearoff=0)
font_menu_sub.add_command(label="Arial", command=lambda: change_font("Arial"))
font_menu_sub.add_command(label="Times New Roman", command=lambda: change_font("Times New Roman"))
font_menu_sub.add_command(label="Comic Sans MS", command=lambda: change_font("CSMS"))
font_menu_sub.add_command(label="Calibri", command=lambda: change_font("Calibri"))
view_menu.add_cascade(label="Шрифт", menu=font_menu_sub)

font_size = tkinter.Menu(view_menu, tearoff=0)
font_size.add_command(label="8", command=lambda: change_size(8))
font_size.add_command(label="10", command=lambda: change_size(10))
font_size.add_command(label="12", command=lambda: change_size(12))
font_size.add_command(label="14", command=lambda: change_size(14))
font_size.add_command(label="16", command=lambda: change_size(16))
font_size.add_command(label="20", command=lambda: change_size(20))
view_menu.add_cascade(label="Размер", menu=font_size)

menu_frame.add_cascade(label="Вид", menu=view_menu)

format_menu = tkinter.Menu(menu_frame, tearoff=0)
format_menu.add_command(label="Курсив", command=lambda: change_format("Italic"))
format_menu.add_command(label="Жирный", command=lambda: change_format("Bold"))
format_menu.add_command(label="Подчеркнутый", command=lambda: change_format("Underline"))
menu_frame.add_cascade(label="Формат", menu=format_menu)

position_menu = tkinter.Menu(menu_frame, tearoff=0)
position_menu.add_command(label="Слева", command=lambda: change_position("left"))
position_menu.add_command(label="По центру", command=lambda: change_position("center"))
position_menu.add_command(label="Справа", command=lambda: change_position("right"))
menu_frame.add_cascade(label="Положение", menu=position_menu)
screen.config(menu=menu_frame)

view_colors = {
    "dark": {
        "text_bg": "black", "text_fg": "white", "cursor": "white", "select_bg": "grey"
    }, 
    "light": {
        "text_bg": "white", "text_fg": "black", "cursor": "black", "select_bg": "blue"
    },
    "grey": {
        "text_bg": "dark grey", "text_fg": "white", "cursor": "white", "select_bg": "grey"
    }
}

fonts = {
    "Arial": {
        "style_font": "Arial"
    },
    "CSMS": {
        "style_font": "Comic Sans MS"
    },
    "Times New Roman": {
        "style_font": "Times New Roman"
    },
    "Calibri": {
        "style_font": "Calibri"
    }
}

text_fild = tkinter.Text(frame, padx=10, pady=10, wrap="word", spacing3=10, font="Arial 12")
text_fild.pack(side="left", fill="both", expand=True)

scroll = tkinter.Scrollbar(frame, command=text_fild.yview)
scroll.pack(side="right", fill="y")
text_fild.config(yscrollcommand=scroll.set)

screen.mainloop()