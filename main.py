print("ESP: Hola soy 'Santek', estoy probando GitHub.\nENG: Hi, im 'Santek', im testing GitHub.")
print()
name = input("ESP: ¡Ingrese el nombre de quien esta ejecutando!\nENG: Enter the name of the person executing this!\n>")
while True:
    if not name.isalpha() or name == "":
        print("ESP: Oye! Ingresa un nombre válido!\nENG: Hey! Enter a valid name!")
        name = input("ESP: ¡Ingrese el nombre de quien esta ejecutando!\nENG: Enter the name of the person executing this!\n>")
    else:
        nameTrue = name
        print(f"ESP: ¡Bienvenido/a {nameTrue.title()} un placer!\nENG: Welcome {nameTrue.title()} its a pleasure!")
        break        

age = input(f"ESP: ¿Qué edad tienes?\nENG: How old are you?\n>")
while True:
    if not age.isdigit() or age == "" or int(age) < 0:
        print("ESP: Oye! Ingresa una edad válida en formato númerico!\nENG: Hey! Enter a valid age in numeric format!")
        age = input(f"ESP: ¿Qué edad tienes?\nENG: How old are you?\n>")
    else:
        ageTrue = int(age)
        break
print(f"ESP: Bien! Eres {nameTrue.title()} y tienes {ageTrue} años.\nENG: Nice! You are {nameTrue.title()} and you are {ageTrue} years old.")
