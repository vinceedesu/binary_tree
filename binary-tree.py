class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
# ================== EXERCISE =====================
    # find_min method
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
    
if __name__ == '__main__':
    numbers = [17, 4 , 1, 20, 9, 23, 18, 34,]
    numbers_tree = build_tree(numbers)
    
    # countries = ['India', 'China', 'USA', 'Germany', 'UK', 'Pakistan']
    # country_tree = build_tree(countries)
    # print("UK is in the list? ", country_tree.search('UK'))
    # print("Japan is in the list? ", country_tree.search('Japan'))
    
    # print(numbers_tree.in_order_traversal())
    
    print("Input numbers: ", numbers)
    print("Min: ", numbers_tree.find_min())