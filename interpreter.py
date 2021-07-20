#TODO Create class and function
#TODO Add the option to dinamically select which word document will be used

import docx2txt
import jinja2

def main():
    PATH='template.html'

    text=docx2txt.process("./WordDocs/Pensamientos 7.docx")

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
