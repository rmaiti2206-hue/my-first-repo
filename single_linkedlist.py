class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertbeg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insertpos(self, pos, data):
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insertbeg(data)
            return
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1
        if not current:
            print("Position out of range")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def deletebeg(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def deleteend(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def deletevalue(self, value):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print("Value not found in the list.")

    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                print(f"Value {value} found at position {position}")
                return
            current = current.next
            position += 1
        print("Value not found")

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Total nodes: {count}")


def menu():
    ll = SinglyLinkedList()

    while True:
        print("\n--- Singly Linked List Menu ---")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at position")
        print("4. Delete from beginning")
        print("5. Delete from end")
        print("6. Delete by value")
        print("7. Search for value")
        print("8. Display list")
        print("9. Count nodes")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter data to insert at beginning: ")
            ll.insertbeg(data)
        elif choice == '2':
            data = input("Enter data to insert at end: ")
            ll.insertend(data)
        elif choice == '3':
            pos = int(input("Enter position to insert at: "))
            data = input("Enter data to insert: ")
            ll.insertpos(pos, data)
        elif choice == '4':
            ll.deletebeg()
        elif choice == '5':
            ll.deleteend()
        elif choice == '6':
            val = input("Enter value to delete: ")
            ll.deletevalue(val)
        elif choice == '7':
            val = input("Enter value to search for: ")
            ll.search(val)
        elif choice == '8':
            ll.display()
        elif choice == '9':
            ll.count_nodes()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
