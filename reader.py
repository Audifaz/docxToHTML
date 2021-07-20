#TODO Add the option to dinamically select which word document will be used
import docx2txt
import jinja2

PATH='template.html'

text=docx2txt.process("Pensamientos 7.docx")

templateLoader=jinja2.FileSystemLoader(searchpath="./")

templateEnv=jinja2.Environment(loader=templateLoader)

template=templateEnv.get_template(PATH)

output=template.render(variable=text)

encoded_unicode=output.encode("utf8")

f=open("pensamiento.html","wb")
f.write(encoded_unicode)
f.close()