line = input("Enter a string: ")
sin, cos, log = 'sin', 'cos', 'log'

if sin in line:
    line = line.replace('sin', 'sin()')
if cos in line:
    line = line.replace('cos', 'cos()')
if log in line:
    line = line.replace('log', 'log()')

print("{0}".format(line))
