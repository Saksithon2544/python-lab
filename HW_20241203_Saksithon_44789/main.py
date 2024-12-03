import sys
from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('\n')
            country, capital = line.split(',')
            country = country.capitalize()
            capital = capital.capitalize()
            world_capitals[country] = capital
            
def write_to_file(country_name, capital_name):
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write('\n' + country_name + ',' + capital_name)

root = Tk()
root.withdraw()
world_capitals = {}
while True:
    read_from_file()
    simpledialog.askstring
    query_country = ''
    query_country = simpledialog.askstring('Country', 'Type the name of a country:')
    query_country = query_country.capitalize()
    if query_country in world_capitals:
        result = world_capitals[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
    else:
        new_capital = simpledialog.askstring('Teach me', 'I don\'t know! Please teach me! What is the capital of ' + query_country + '?')
        write_to_file(query_country, new_capital)
        messagebox.showinfo('Thank you', 'Thank you for teaching me!')
    answer = simpledialog.askstring('Continue', 'Do you want to try again? y/n')
    if answer == 'n':
        messagebox.showinfo('Thank you', 'Thank you for playing!')
        root.destroy()
        sys.exit()


    
    

            
            