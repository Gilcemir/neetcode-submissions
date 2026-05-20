# Esse exercício tem dois "gotchas"
# 1. Na cache (que será um dict), deve-se salvar no valor uma referência ao Nó, e não o valor em si
# 2. Usar dois Nós Dummies, para ter acesso ao início e fim da lista. Esses dois nós devem começar apontando um ao outro head -> tail e vice versa
# Usar doubly linked list; de um lado tem o mais recente usado, na outra ponta, o menos recente
# Como está usando o próprio Nó como referência, ele pode "se remover" da double linked list em O(1); 
# Por isso devemos usar double linked list e não deque - porque deque não temos referência

class Node:
    
    def __init__(self, key: int = 0, value: int = 0):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()

        self.head.next, self.tail.prev = self.tail, self.head

    # se auto remove o nó que é passado por referênciua
    def _remove_node(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    # adiciona no inicio - assim se torna o mais recente
    def _add_node_left(self, node: Node):
        temp = self.head.next
        self.head.next, node.prev = node, self.head
        node.next, temp.prev = temp, node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove_node(self.cache[key])
            self._add_node_left(self.cache[key])
            return self.cache[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])
            self._add_node_left(self.cache[key])
            self.cache[key].value = value
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_node_left(self.cache[key])
            if self.capacity < len(self.cache):
                deleted_key = self.tail.prev.key
                self._remove_node(self.tail.prev)
                del self.cache[deleted_key]

        
