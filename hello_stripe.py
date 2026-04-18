from mako.template import Template

# 1. Open the template file
my_template = Template(filename='makofile.txt')

# 2. "Render" it by filling in the blanks
result = my_template.render(user_name="Alice", date="Monday")

print(result)
