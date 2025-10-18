from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: 'Node' = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def insert_at_beginning(self, data: Any) -> None:
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node

    def insert_at_end(self, data: Any) -> None:
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def get_LinkedLists(self) -> str:
        linked_list_values = ''
        current_node:Node = self.head
        if current_node is None:
            return None

        while current_node:
            linked_list_values += str(current_node.data) + '->'
            current_node = current_node.next
        return linked_list_values.rstrip('->')

    def search_for(self, target: Any) -> bool:
        current_node = self.head
        while current_node:
            if current_node.data == target:
                return True
            current_node = current_node.next
        return False

    def remove_beginning(self) -> Any:
        if self.head is None:
            return None  # list is empty

        deleted_data = self.head.data
        self.head = self.head.next  # move head to the next node

        if self.head is None:
            self.tail = None  # if list became empty, reset tail too

        return deleted_data
    
    def remove_at_end(self) -> Any:
        if self.tail is None:
            return None  # list is empty

        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        
        current = self.head
        while current.next.next:
            current = current.next

        deleted_data = current.next.data
        current.next = None
        return deleted_data

    def remove_at(self, index: int) -> Any:
        if self.head is None:
            return None  # empty list

        if index == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return deleted_data

        current = self.head
        for i in range(index - 1):
            if current.next is None:  
                return None
            current = current.next

        to_delete = current.next
        if to_delete is None:  
            return None

        deleted_data = to_delete.data
        current.next = to_delete.next

        if current.next is None:  
            self.tail = current

        return deleted_data

        
        
if __name__ == '__main__':
    llst = LinkedList()
    llst1 = LinkedList()
    llst2 = LinkedList()
    for i in range(10):
        llst.insert_at_end(i**2)
        llst1.insert_at_end(i**2)
        llst2.insert_at_end(i**2)
    print(f'Before: {llst.get_LinkedLists()}\nRemoved Node:{llst.remove_beginning()}\nAfter: {llst.get_LinkedLists()}\n') #remove_beginning()
    print(f'Before: {llst1.get_LinkedLists()}\nRemoved Node:{llst1.remove_at_end()}\nAfter: {llst1.get_LinkedLists()}\n') #remove_at_end()
    print(f'Before: {llst2.get_LinkedLists()}\nRemoved Node:{llst2.remove_at(5)}\nAfter: {llst2.get_LinkedLists()}\n') #remove_at()
