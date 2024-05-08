import random 
from tkinter import *
window = Tk()
window.title('Slot Machine')


wheelImages = ['♠', '♥', '♣', '♦', 'B', 'Ω']
wheels = [[0] for _ in range(3)]


def spin():
   
    for i in range(3):
        symbol_index = random.randint(0, len(wheelImages) - 1)
        wheels[i][0] = symbol_index
        spin_buttons[i].config(text=wheelImages[symbol_index])

    
    bs = sum(1 for wheel in wheels if wheelImages[wheel[0]] == 'B')
    win_amount = 0
    if bs == 1:
        win_amount += 0.1
    elif bs == 2:
        win_amount += 0.25
    elif bs == 3:
        win_amount += 0.50

    
    global total_amount_won
    total_amount_won += win_amount
    total_amount_won_label.config(text='Total Amount Won: ${:.2f}'.format(total_amount_won))

    win_amount_label.config(text='Win Amount: ${:.2f}'.format(win_amount))


spin_buttons = [Button(window, text='', width=4, height=2) for _ in range(3)]


for i, button in enumerate(spin_buttons):
    button.grid(row=3, column=i+1)


spin_button = Button(window, text='Spin', command=spin)
spin_button.grid(row=2, column=2)

total_amount_won = 0
total_amount_won_label = Label(window, text='Total Amount Won: $0.00', bg='#9FD996')
total_amount_won_label.grid(row=4, column=2, pady=5)

win_amount_label = Label(window, text='Win Amount: $0.00')
win_amount_label.grid(row=5, column=2, pady=5)

window_width = 275
window_height = 100
Label(
    window,
    text=' ',
).grid(row=1, column=0)



window.mainloop()





