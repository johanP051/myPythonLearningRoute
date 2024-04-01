while True:
    try:
        name = input('Inserte un name: ')
        n = int(input('Inserte un n: '))
    except Exception as e:
        print(f"Error: {e}")
        pass
        print("Esto se ejecuta porque el pass no hace nada, solo dice que el ciclo continúe")
        continue
        print("Esto no se ejecuta porque arriba hay un continue")
    else:
        dic = dict(n = n, name = name)
        print(f"Datos: {dic}")
        #Se rompe solo cuando no hay excepciones, es decir, el usr inserta todos los datos bien
        break
    finally:
        #Esto siempre se ejecuta 
        print('Thanks!')
