class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def remove(self, value):
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.value:
            node.right = self._remove_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._remove_recursive(node.right, successor.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def clear(self):
        self.root = None

    def print_tree(self):
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node is not None:
            self._print_tree_recursive(node.left)
            print(node.value, end = ' ')
            self._print_tree_recursive(node.right)


# Exemplo de uso
tree = BinaryTree()
x = 0
y = number = None
while True:
    print("\n0 --- Sair            ")
    print("1 --- inserir elemento")
    print("2 --- remover elemento")
    print("3 --- buscar elemeno  ")
    print("4 --- mostrar elementos da arvore")
    print("5 --- limpar arvore\n")
    x = int(input("digite um valor: "))
    
    if (0 == x):
        print("SAINDOOO...")
        break
    if (1 == x):
        # Inserindo números na árvore
        y = int(input("digite o valor do numero pra ser inserido: "))
        tree.insert(y)
        continue
    if (4 == x):
       # Exibindo os números armazenados na árvore
        print("\nNúmeros armazenados na árvore:\n")
        tree.print_tree() 
        print("\n")
        continue
    if (2 == x):
        # Removendo um número específico
        number = int(input("Digite um número para remover da árvore: "))
        
        
        if tree.search(number):
            tree.remove(number)
            # Exibindo os números armazenados após a remoção
            print("\nNúmeros armazenados na árvore após a remoção:\n")
            tree.print_tree()
            print("\n")
        else:
            print("O número não está presente na árvore")
        continue
    if (5 == x):
        # Esvaziando completamente a árvore
        tree.clear()
        tree.print_tree()
        print("\narvore limpa\n")
        continue
    if(3 == x):
        #ver se elemnto esta ou nao na arvore
        number = int(input("Digite um número para buscar na árvore: "))
        if tree.search(number):
            print("O número está presente na árvore.")
        else:
            print("O número não está presente na árvore")