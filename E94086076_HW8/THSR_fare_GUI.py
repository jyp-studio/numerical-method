import tkinter as tk
from THSR_fare import *

# define WIDTH & HEIGHT
WIDTH = 675
HEIGHT = 400

# init tickets
tickets_init()

# flag for earse result_label
earsed = True
result_list = []

# define windows
win = tk.Tk()
# define caption
win.title('高鐵票價查詢')
# define size (WIDTH * HEIGHT)
win.geometry(f'{WIDTH}x{HEIGHT}')

# define label
start_label = tk.Label(
    win, text='The starting station is :', font=('Arial', 14))
end_label = tk.Label(win, text='The end station is :', font=('Arial', 14))
start_label.grid(row=0, column=0, padx=20, pady=20, sticky='w')
end_label.grid(row=1, column=0, padx=20, sticky='w')

# text input
start_text = tk.Text(win, width=45, height=2)
end_text = tk.Text(win, width=45, height=2)
start_text.grid(row=0, column=1)
end_text.grid(row=1, column=1)


# get start and end station
def search_station():
    global earsed
    global result_label
    global result_list
    # earse label
    if earsed != True:
        for text in result_list:
            text.grid_forget()
        result_list.clear()
    # get text
    start_input = start_text.get('1.0', 'end-1c')
    end_input = end_text.get('1.0', 'end-1c')
    # search results
    result = search(start_input, end_input)
    # grid results
    for i in range(len(result)):
        result_label = tk.Label(win, text=result[i], font=('Arial', 14))
        result_label.grid(row=3+i, column=0, columnspan=2, padx=20, sticky='w')
        result_list.append(result_label)
    earsed = False


# buttom
button = tk.Button(win, text='Check the fares',
                   font=('Arial', 14), width=61, height=2, command=search_station)
button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

# mainloop
win.mainloop()
