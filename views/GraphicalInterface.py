import sys
import tkinter
from tkinter import *
from ttkbootstrap import *
from tkinter import filedialog
from controllers.Converter import ConverterTo


class Interface(Frame):
    """
    Classe que gera a interface
    """
    container = Frame()
    container2 = Frame()
    file = filedialog.askopenfilenames()
    selected = Label(container2, text=f"Selecionado: {file[0]}", font=("Monospace", 14))

    # seleção do tipo de converção.
    types_files = ["pdf_file", "docx_file"]
    selected.grid(row=0, column=0, padx=10, pady=5)
    label_left = Label(container, text="De: ", font=("Monospace", 14))
    label_left.grid(row=2, column=0)
    select_box_left = Combobox(container, values=types_files, font=("Monospace", 16))

    label_right = Label(container, text="Para: ", font=("Monaspace", 14))
    label_right.grid(row=2, column=2)

    select_box_right = Combobox(container, values=types_files, font=("Monospace", 16))
    select_box_left.grid(row=2, column=1, padx=10, pady=20)
    select_box_right.grid(row=2, column=3, padx=10, pady=20)

    # botões de conversão:
    c = ConverterTo(file[0], "convertido.docx")
    button_converter = tkinter.Button(container, text="Converter", font=("Monospace", 16), command=c.converter_to_docx)
    #button_converter.bind('<Return>')
    button_cancel = tkinter.Button(container, text="Cancelar", command=exit, font=("Monospace", 16))
    # button_converter.bind('<Return>')
    button_converter.grid(row=4, column=2, padx=0, pady=150)
    button_cancel.grid(row=4, column=3, padx=0, pady=150)
    container2.pack()
    container.pack()

    @classmethod
    def exit(cls) -> None:
        """
        Encerra o programa
        :return: exit(0)
        """
        return sys.exit()


if __name__ == '__main__':
    style = Style('superhero')
    master = style.master
    master.title('Converter')
    master.geometry('725x340')
    gui = Interface(master)
    gui.mainloop()
