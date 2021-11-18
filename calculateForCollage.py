import tkinter as tk
from math import sin,cos,tan

window = tk.Tk()
window.title('Калькулятор')
window.geometry('439x570')
window.resizable(False, False)
window.configure(bg='black')


# логика
def math(operation):
    global formula
    if operation == 'C':
        formula = ' '
    elif operation == 'Del':
        formula = formula[0: -1]
    elif operation == 'x^2':
        formula = str((eval(formula)) ** 2)
    elif operation == '=':
        formula = str((eval(formula)))
    elif operation == 'sin':
        formula = str((round(sin(eval(formula)),4)))
    elif operation == 'cos':
        formula = str((round(cos(eval(formula)),4)))
    elif operation == 'tan':
        formula = str((round(tan(eval(formula)),4)))
    elif operation == 'ctg':
        formula = str((round(1/tan(eval(formula)), 4)))
    else:
        if formula == '0':
            formula = ''
        formula += operation
    lable_text.configure(text=formula)


formula = '0'
lable_text = tk.Label(text=formula, font=('Roboto', 35, 'bold'), bg='black', fg='white')
lable_text.place(x=25, y=20)
# buttons
buttons = ['C', 'sin','cos','tan','ctg','Del', '+/-', '*', '7', '8', '9', '/', '4', '5', '6', '-', '1', '2', '3', '+', '0', '%', 'x^2', '=']
x = 17
y = 120
for button in buttons:
    get_lbl = lambda x=button: math(x)
    tk.Button(text=button, bg='grey', font=('Roboto', 20,), command=get_lbl).place(x=x, y=y, width=108, height=60)
    x += 100
    if x > 400:
        x = 16
        y += 74

window.mainloop()
