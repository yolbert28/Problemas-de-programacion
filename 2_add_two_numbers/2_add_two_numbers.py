
class Node:
    
    def __init__(self, value = None):
        self.data = value
        self.next = None
        
# Solo funciones necesarias para el ejercicio
class LinkedList:
    
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
     
    def inverse_list_numbers_int(self):
        inverseNumber = ""
        last_node = self.head
        
        while last_node:
            inverseNumber += str(last_node.data)
            last_node = last_node.next
            
        return int(inverseNumber[::-1]) 
    
    def insert_str_numbers_in_linked_list(self, value: str):
        for number in value:
            self.insertAtBeginning(int(number))
    
    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
result_list = LinkedList()

linked_list_1.insertAtBeginning(3)
linked_list_1.insertAtBeginning(4)
linked_list_1.insertAtBeginning(2)

linked_list_2.insertAtBeginning(4)
linked_list_2.insertAtBeginning(6)
linked_list_2.insertAtBeginning(5)

linked_list_1.printList()
linked_list_2.printList()


result = linked_list_1.inverse_list_numbers_int() + linked_list_2.inverse_list_numbers_int()

result_list.insert_str_numbers_in_linked_list(str(result))

result_list.printList()
        

  