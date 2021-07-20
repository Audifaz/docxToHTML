import docx2txt
import jinja2

text=docx2txt.process("Pensamientos 7.docx")

print((text))

f=open("test.txt","w")
#f.write(text)
f.close()

path='template.html'

templateLoader=jinja2.FileSystemLoader(searchpath="./")

templateEnv=jinja2.Environment(loader=templateLoader)

template=templateEnv.get_template(path)

output=template.render(variable=text)

f=open("pensamiento.html","w")
f.write(output)
f.close()