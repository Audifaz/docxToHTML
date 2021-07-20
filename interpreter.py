#TODO Create File separation
#TODO Add the option to dinamically select which word document will be used
#TODO Create class and function
import docx2txt
import jinja2

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