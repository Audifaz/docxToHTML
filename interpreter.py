#TODO Create class and function

import docx2txt
import jinja2
import tkinter as tk
from tkinter import filedialog

def main():
    window = tk.Tk()
    window.withdraw()
    folder=filedialog.askopenfilename()
    print(folder)

    PATH='template.html'

    text=docx2txt.process(folder)

    templateLoader=jinja2.FileSystemLoader(searchpath="./Templates")

    templateEnv=jinja2.Environment(loader=templateLoader)

    template=templateEnv.get_template(PATH)

    output=template.render(variable=text)

    encoded_unicode=output.encode("utf8")

    f=open("./Output/pensamiento.html","wb")
    f.write(encoded_unicode)
    f.close()


if __name__ == "__main__":
    main()
