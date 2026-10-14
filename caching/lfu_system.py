from datetime import datetime,timedelta

class Node:
    #base construtor for the Node
    def __init__(self,dict,freq,key):
        self.key = key
        self.data = dict
        self.freq = freq
        self.exp_time = datetime.now() + timedelta(minutes = 30)
        self.next = None
        self.prev = None

class doublyLL:
    #function for checking if list is empty or not
    def __init__(self):
        self.head = Node(None,{},-1)
        self.tail = Node(None,{},-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self) -> bool:
        return self.head.next == self.tail

    #function for inserting a node
    def add_in_front(self,newNode):
        next_of_head = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = next_of_head
        next_of_head.prev = newNode
        return newNode

    def remove_particular(self,node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left

    def remove_last(self):
        left = self.tail.prev.prev
        node = self.tail.prev
        left.next = self.tail
        self.tail.prev = left
        return node
 
class cacheing_system:
    count = 0
    min_freq = 1

    def __init__(self,capacity:int):
        self.cache_data = {}
        self.cache_freq = {}
        self.capacity = capacity

    def frequency_incrementer(self,current_Node:Node):
        current_Node.freq += 1 


    def get(self,cache_key):
        current_node = self.cache_data.get(cache_key)
        if current_node:
            if current_node.exp_time < datetime.now():
                self.cache_freq[current_node.freq].remove_particular(current_node)
                self.cache_data.pop(cache_key)
                if self.cache_freq[self.min_freq].is_empty():
                    min_freq += 1
                self.count -= 1
                return None
            self.cache_freq[current_node.freq].remove_particular(current_node)
            self.frequency_incrementer(current_node)
            if not self.cache_freq.get(current_node.freq):
                self.cache_freq[current_node.freq] = doublyLL()
            self.cache_freq[current_node.freq].add_in_front(current_node) 
            return current_node.data
        return None
        
        
    def store(self,cache_key,data : dict) -> bool:
        if self.capacity == self.count:
            node = self.cache_freq[self.min_freq].remove_last()
            self.cache_freq.pop(node.key)
        self.count+=1
        newNode = Node(data,freq= 1,key = cache_key)
        self.cache_data[cache_key] = newNode
        if not self.cache_freq.get(1):
            self.cache_freq[1] = doublyLL()
        self.cache_freq[1].add_in_front(newNode)
        return True