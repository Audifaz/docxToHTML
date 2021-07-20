import jinja2

path='template.html'

templateLoader=jinja2.FileSystemLoader(searchpath="./")

templateEnv=jinja2.Environment(loader=templateLoader)

template=templateEnv.get_template(path)

output=template.render(variable="Does this work?")

print(output)