user = "johan:posada"

userSplit = user.split(":")
name = user.split(":")[0]
lastname = user.split(":")[1]

print(userSplit)
lista = []
lista.append(tuple(userSplit))
print(lista)

print(name)
print(f"Lastname: {lastname}")

### Probando strip
usuario = "     user:johan"

print(usuario)
stripedUsuario = usuario.strip(" ")
print(stripedUsuario)

print(f"\n Juntando split y stripsss")
user = "    johan:posada"
print(user)
N_user = user.split(":")[0].strip()
print(N_user)