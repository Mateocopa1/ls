datos_invitados = {'Andres' : 1234, 'Mafe' : 5678, 'Kata' : 8912}
a = list(dict.keys(datos_invitados))
b = list(dict.values(datos_invitados))
c = 0
for c in range (len(a)):
    print(f'Nombre de invitado {a[c]}, numero de telefono {b[c]}')
    c += 1

datos_invitados.update({'Andres' : 3456})
a = list(dict.keys(datos_invitados))
b = list(dict.values(datos_invitados))

for c in range (len(a)):
    print(f'Nombre de invitado {a[c]}, numero de telefono {b[c]}')
    c += 1
