import pyfiglet
import random
from termcolor import colored
n1 = "Hecho por L.M"

n1 = pyfiglet.figlet_format(n1)
print(colored(n1,"green"))
# Mostrar el banner de bienvenida
bienvenid = pyfiglet.figlet_format("Apuesta y Gana")
print(colored(bienvenid, "blue"))

# Pedir el depósito inicial del usuario
cuenta_bancaria = int(input(colored("Deposite: ", "light_magenta")))

print("Juega entre 1 y 10")

# Bucle del juego
while cuenta_bancaria > 0:
    maquina_numero = random.randint(1, 10)  # Número aleatorio de la máquina
    apuesta = int(input(colored("¿Cuánto quieres apostar?: ", "yellow")))

    if apuesta > cuenta_bancaria:
        print(colored("No puedes apostar más de lo que tienes en tu cuenta.", "red"))
        continue  # Salta a la siguiente iteración si la apuesta es mayor que el saldo

    numero_usuario = int(input("¿A qué número juegas?: "))

    # Mensajes de ganancia y pérdida
    si_ganas = ["¡Buena! Sabes de esto", "¡Ganaste!", "¡Eres un campeón!"]
    si_no_ganas = ["Novato, perdiste", "Uff, mala suerte hermano", "Jaja, yo gano"]

    # Verificar si el número del usuario coincide con el de la máquina
    if maquina_numero == numero_usuario:
        cuenta_bancaria += apuesta  # Sumar la apuesta a la cuenta bancaria
        print(random.choice(si_ganas))
        print(f"Tu cuenta es de {cuenta_bancaria}")
    else:
        cuenta_bancaria -= apuesta  # Restar la apuesta de la cuenta bancaria
        print(random.choice(si_no_ganas))
        print(colored(f"La máquina sacó: {maquina_numero}", "red"))
        print(f"Tu cuenta es de {cuenta_bancaria}")

    # Verificar si el usuario se quedó sin dinero
    if cuenta_bancaria <= 0:
        print(colored("Te quedaste sin dinero. ¡Juego terminado!", "red"))
        break


    
        




