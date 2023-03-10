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
# ================== EXERCISE 1=====================
    # find_min method
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    #find_max method same as find_min
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    #calculate sum
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    #Post order traversal
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)
        
        return elements
    
    #Pre order traversal
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
#===================== Part 2 ======================
    def delete(self, val):
        if val < self.data:
            if self.left:
                self. left = self.left.delete(val)
        elif val > self.data:
            if self.left:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
            
#================= Exercise 2 ===============
            #just flip min to max and right to left
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self
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
    print("=========================================")
    print("Numbers: ", numbers)
    print("=========================================") 
    print("The Min is: ", numbers_tree.find_min())
    print("The Max is: ", numbers_tree.find_max())
    print("The Sum of the Numbers is: ", numbers_tree.calculate_sum())
    #post and pre oredr
    print("The Post order traversal is: ", numbers_tree.post_order_traversal())
    print("The Pre order traversal is: ", numbers_tree.pre_order_traversal())
    
    #in order and delete
    print("In order traversal: ", numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print("Deleted a number: ", numbers_tree.in_order_traversal())
    print()
    
    print("=================[FULL NAME]========================") 
    #Full name tree 
    full_name = ['V', 'I', 'N', 'C', 'E','J','E', 'R','E','M','Y','L','A','D','I','O','N']
    name_tree = build_tree(full_name)
    
    print("Name: ", full_name)
    #MIN AND MAX OF NAME
    print("The Min is: ", name_tree.find_min())
    print("The Max is: ", name_tree.find_max())    
    #ASCENDING ORDER IN_ORDER_TRAVERSAL
    print("Ascending order(In order traversal): ",name_tree.in_order_traversal())
    
    #post order traversal
    print("Post order traversal: ", name_tree.post_order_traversal())
    print("Pre order traversal: ", name_tree.pre_order_traversal())  
    #search for a letter
    search_letter = input("Input letter to see if the letter is in the name(use capital letter): ")
    def searchFromName():
        indicator = name_tree.search(search_letter)
        if indicator is True:
            print("The input is in the name!\n")
        if indicator is False:
            print("The input is NOT in the name!\n")
    def delete_letter():
        input_letter = input("Input letter to delete: ")
        name_tree.delete(input_letter)
        print("Deleted " + input_letter + ": The new set is: ", name_tree.in_order_traversal())
    searchFromName()
    delete_letter()
    
