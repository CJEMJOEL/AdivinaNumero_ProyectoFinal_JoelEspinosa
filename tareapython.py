def adivina_numero():
    print("🎲 Bienvenido al juego: Adivina el número")

    # Pedir nombre del usuario
    nombre = input("¿Cuál es tu nombre? ")
    print(f"\nHola {nombre}, piensa en un número entre 1 y 100...")
    input("Cuando estés listo, presiona ENTER.\n")

    bajo = 1
    alto = 100
    intentos = 0

    while bajo <= alto:
        intentos += 1
        medio = (bajo + alto) // 2
        print(f"{nombre}, intento {intentos}: ¿Es {medio} tu número?")
        respuesta = input("Responde con (mayor / menor / correcto): ").strip().lower()

        if respuesta == "mayor":
            bajo = medio + 1
        elif respuesta == "menor":
            alto = medio - 1
        elif respuesta == "correcto":
            print(f"✅ ¡Genial {nombre}! He adivinado tu número en {intentos} intentos. Era {medio}.")
            break
        else:
            print(f"⚠️ {nombre}, esa no es una respuesta válida. Usa 'mayor', 'menor' o 'correcto'.")


if __name__ == "__main__":
    adivina_numero()
