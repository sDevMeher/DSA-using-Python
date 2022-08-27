class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def viewLL(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data , end =" ")
                temp = temp.next
                

    def deleteFirst(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            self.head = self.head.next
            
    def insertLast(self,data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
LL1 = LinkedList()
LL1.insertLast(10)
LL1.insertLast(20)
LL1.insertLast(30)
LL1.insertLast(40)
LL1.insertLast(50)
LL1.viewLL()
LL1.deleteFirst()
LL1.viewLL()

                
#Note* head contains the first node that is the object of node class
# So head access the next variable of the Node class which contains the next node
                
#****************************************
##    def show_LL(self):
##        if self.head is None:
##            print("Linked list is empty")
##        else:
##            n = self.head
##            while n is not None:
##                print(n.data)
##                n = n.nextNode
##    def add_begin(self,data):
##        new_node = Node(data)
##        new_node.nextNode = self.head
##        self.head = new_node

##LL1 = LinkedList()
##LL1.add_begin(10)
##LL1.add_begin(20)
##LL1.show_LL()

        


        
        
