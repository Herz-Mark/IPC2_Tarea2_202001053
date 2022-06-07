from Lista_Enlazada_Circular import LinkedList

List = LinkedList()

List.append(9)
List.append(11)
List.append(45)
List.append(66)
List.append(10)

print("Lista Completa:")
List.recorrer()
print()
print("Seleccione numero: ") 
numero = int(input())

List.search(numero)
