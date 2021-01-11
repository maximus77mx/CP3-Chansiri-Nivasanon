from tkinter import *
from tkinter import ttk
from forex_python.converter import *

currency_rate = CurrencyRates()

def click_on_convert_rate(event):
    exchange_rate = currency_rate.get_rate(text_box_from_currency.get(), text_box_to_currency.get())
    if exchange_rate != 1:
        text_box_rate.configure(text=exchange_rate)


def click_on_convert_amount(event):
    converted_amount = currency_rate.convert(text_box_from_currency.get(), text_box_to_currency.get(),
                                             (text_box_amount.get()))
    text_box_converted_amount.configure(text=converted_amount)


main_window = Tk()
main_window.option_add("*Font", "LeelawadeeUI 12 bold")
main_window.title('CurrencyConverter')
main_window.resizable(0, 0)

label_from_currency = Label(main_window, text="From Currency")
label_from_currency.grid(row=0, column=0, padx=5, pady=5)
text_box_from_currency = ttk.Combobox(main_window, values=list(currency_rate.get_rates("").keys()))
text_box_from_currency.current(29)
text_box_from_currency.bind("<<ComboboxSelected>>")
text_box_from_currency.grid(row=0, column=1, padx=10, pady=10)

label_to_currency = Label(main_window, text="To Currency")
label_to_currency.grid(row=1, column=0, padx=5, pady=5)
text_box_to_currency = ttk.Combobox(main_window, values=list(currency_rate.get_rates("").keys()))
text_box_to_currency.current(10)
text_box_to_currency.bind("<<ComboboxSelected>>")
text_box_to_currency.grid(row=1, column=1, padx=5, pady=5)

rate_button = Button(main_window, text="Conversion Rate", bg="deep sky blue", fg="White")
rate_button.bind('<Button-1>', click_on_convert_rate)
rate_button.grid(row=2, column=0, padx=5, pady=5)
text_box_rate = Label(main_window, text="1 USD = ")
text_box_rate.grid(row=2, column=1, padx=5, pady=5)

label_amount = Label(main_window, text="Amount")
label_amount.grid(row=3, column=0, padx=5, pady=5)
text_box_amount = Entry(main_window)
text_box_amount.grid(row=3, column=1)

convert_button = Button(main_window, text="Convert Amount", bg="RoyalBlue3", fg="White")
convert_button.bind('<Button-1>', click_on_convert_amount)
convert_button.grid(row=4, column=0, padx=5, pady=5)
text_box_converted_amount = Label(main_window, text=" ")
text_box_converted_amount.grid(row=4, column=1, padx=5, pady=5)

main_window.mainloop()