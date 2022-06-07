from Nodo import Node

class LinkedList:
    def __init__(self):
        self.First = None
        self.Last = None
    
    def empty(self):
        if self.First == None:
            return True
        else:
            return False

    def append(self, Value):
        if self.empty():
            self.First = self.Last = Node(Value)
        else:
            aux = self.Last
            self.Last = aux.next = Node(Value)
            self.Last.back = aux
        self.First.back = self.Last
        self.Last.next = self.First

    def recorrer(self):
        aux = self.First
        while aux:
            print(aux.value)
            aux = aux.next
            if aux == self.First:
                break
    
    def search(self, value):
        if self.First is None:
            return
        aux = self.First
        while aux is not None:
            if aux.value == value:
                siguiente = aux.next
                anterior = aux.back
                print("anterior:",anterior.value,"actual:",aux.value,"siguiente:",siguiente.value)
                break
            aux = aux.next

        
