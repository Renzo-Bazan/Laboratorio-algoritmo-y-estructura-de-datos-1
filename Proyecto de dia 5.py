import random
palabras = ["Pancho", "Pizza", "Hamburguesa", "Lomito", "Tallarines", "Ravioles", "Cafe", "Medialuna"]
palabra = random.choice(palabras).lower()
vidas = 6
letras_adivinadas = []
guiones = ["_" for _ in palabra]

print("¡Bienvenido al juego de Ahorcado!")
print(f"Tienes {vidas} vidas para adivinar la palabra.")

while vidas > 0 and "_" in guiones:
    print("\nPalabra: " + " ".join(guiones))
    
    letra = input("Elige una letra: ").lower()

    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra, intenta con otra.")
        continue

    letras_adivinadas.append(letra)

    if letra in palabra:
        print(f"¡Bien! La letra '{letra}' está en la palabra.")
        for i, l in enumerate(palabra):
            if l == letra:
                guiones[i] = letra
    else:
        vidas -= 1
        print(f"La letra '{letra}' no está en la palabra. Te quedan {vidas} vidas.")

if "_" not in guiones:
    print("\n¡Felicidades! Adivinaste la palabra:", palabra)
    print(r"""
__     ______  _    _  __          _______ _   _ 
\ \   / / __ \| |  | | \ \        / /_   _| \ | |
 \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
  \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
   | | | |__| | |__| |    \  /\  /   _| |_| |\  |
   |_|  \____/ \____/      \/  \/   |_____|_| \_|
    """)
else:
    print("\nTe has quedado sin vidas. La palabra era:", palabra)
    print(r"""
  _____                         ____                 
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                    
""")
