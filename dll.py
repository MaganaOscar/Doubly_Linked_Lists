class DLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_front(self, val):    
        new_node = DLNode(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return self
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
            return self
    def print_values(self):
        runner = self.head
        if runner == None:
            print("No items in DLList")
            return self
        elif self.head == self.tail:
            print(runner.value,)
            return self
        else:
            print(runner.value)
            while runner.next != self.head:
                runner = runner.next
                print(runner.value)
        return self
    def add_to_back(self, val):
        new_node = DLNode(val)
        if self.head == None:
            self.add_to_front(val)
            return self
        elif self.head == self.tail:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = self.head
            self.tail = new_node
            return self
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail = new_node
            return self
    def remove_from_front(self):
        if self.head == None:
            print("No items in DLList")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return self
    def remove_from_back(self):
        if self.head == None:
            print("No items in DLList")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        return self
    def remove_val(self, val):
        if val == self.head.value:
            self.remove_from_front()
        elif val == self.tail.value:
            self.remove_from_back()
        else:
            runner = self.head.next
            while(runner.next != self.head):
                if runner.value == val:
                    runner.prev.next = runner.next
                    runner.next.prev  = runner.prev
                runner = runner.next
        return self
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
        else:
            index = 0
            new_node = DLNode(val)
            runner = self.head
            while index < n - 1:
                if runner.next != self.head:
                    runner = runner.next
                index += 1
            new_node.next  = runner.next
            new_node.prev = runner
            runner.next.prev = new_node
            runner.next = new_node
        return self
    
# my_list = DLList()
# my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

# my_list.remove_from_front().print_values()
# my_list.add_to_front("Linked Lists").print_values()
# my_list.remove_from_back().print_values()
# my_list.add_to_back("fun!").print_values()
# my_list.add_to_back("ish").print_values()
# my_list.remove_val('ar').print_values()
# my_list.insert_at('hello', 9).print_values()