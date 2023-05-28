#!/usr/bin/python3



import os
import time

#Crea las variables para los diferentes diseños de banner que puedes elegir
banner1 = '''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⣄⠀⠀⠀⠀⠀⠀⣠⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣠⣴⣶⣶⣦⣄⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣉⣉⣉⣉⣉⣉⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀
⠀⠀⢸⣿⠟⠛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⠛⠛⠛⠛⢿⡿⠛⠿⣿⡇⠀⠀
⠀⠀⢸⡏⢠⣾⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⣽⡇⠀⠀
⠀⠀⢸⡇⢸⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⡇⢸⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⡇⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⠿⣿⡇⠀⠀
⠀⠀⢸⡇⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⠶⠶⣾⡇⠀⠀
⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⠶⠶⢾⡇⠀⠀
⠀⠀⢸⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣷⣶⣶⣿⡇⠀⠀
⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

banner2 = '''
.--. .   .          .  
|   | | _ | _.  _.._ |- 
|   ; |/ \||(_||(_][ )|-
--' '   ''._.       -'
'''

banner3 = '''
  ____                 _                      
 | __ )  __ _ ___ ___(_) ___     __ _ _ __  
 |  _ \ / _ / / | |/ |   / _` | '_ \ 
 | |_) | (_| \ \ \ | (   | (_| | |_) |
 |____/ \,_|___/___/_|\___|___\,_| .__/ 
                            |_____| |_|    
'''

#Crea las variables para los diferentes colores que puedes elegir
color1 = '\u001b[31;1m' #rojo
color2 = '\u001b[32;1m' #verde
color3 = '\u001b[34;1m' #azul

#Solicita al usuario que ingrese su nombre
name = input('Ingresa tu nombre: ')

#Muestra las opciones de banner y solicita al usuario que elija una
print('\nElige un diseño para tu banner:')
print('1. Banner 1')
print('2. Banner 2')
print('3. Banner 3')

banner_choice = input('\nIngresa el número correspondiente al diseño que deseas: ')
if banner_choice == '1':
    banner = banner1
elif banner_choice == '2':
    banner = banner2
else:
    banner = banner3

#Muestra las opciones de color y solicita al usuario que elija uno
print('\nElige un color para tu banner:')
print('1. Rojo')
print('2. Verde')
print('3. Azul')

color_choice = input('\nIngresa el número correspondiente al color que deseas: ')
if color_choice == '1':
    color = color1
elif color_choice == '2':
    color = color2
else:
    color = color3

#Crea el banner con el diseño y el color elegidos y lo muestra en la pantalla
os.system('clear')
print(color + banner + '\u001b[0m')
print('Hola, ' + name + '! ¡Bienvenido/a a Termux!')