import tkinter
from python_project import average, median, find_max_number, find_min_number

def calculate():
    numbers = list(map(float, entry.get().split()))

    lable_average['text'] = f'Среднее: {average(numbers)}'
    lable_median['text'] = f'Медиана: {median(numbers)}'
    lable_max_value['text'] = f'Максимальное значение: {find_max_number(numbers)}'
    lable_min_value['text'] = f'Минимальное значение: {find_min_number(numbers)}'

window =tkinter.Tk()
window.geometry('300x350')
window.resizable(False , False)
window.title('Работа с массивами')
window['bg'] = '#F0F9F9'

entry = tkinter.Entry(font=('Calibri', 14))
entry.grid(padx=45,pady=13)

entry_label = tkinter.Label(text = 'введите несколько чисел', width = 20, fg = 'green')
entry_label.grid()

button_calculate = tkinter.Button(text='Посчитать',activebackground = 'yellow',activeforeground='green',
                                  bg = 'green',
                                  font=('Calibri', 12),
                                  command=calculate)

button_calculate.place(relx=0.5, y=80, anchor='n')

lable_average = tkinter.Label(text='Среднее', fg='green',
                              font=('Calibri', 12, ))

lable_average.place(x=10, y=120)

lable_median = tkinter.Label(text='Медиана', fg='green',
                             font=('Calibri', 12))

lable_median.place(x=10, y=150)

lable_max_value = tkinter.Label(text='Максимальное значение', fg='green',
                                font=('Calibri', 12))

lable_max_value.place(x=10,y=180)

lable_min_value = tkinter.Label(text='Минимальное значение', fg='green',
                                font=('Calibri',12))
lable_min_value.place(x=10, y=210)

tkinter.mainloop()