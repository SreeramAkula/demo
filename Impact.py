# shares=int(input("number of shares"))
# a=int(input("Buying Price"))
# b=int(input("Selling Price"))
# profit=(shares*b)-(shares*a)
# print(profit)




# import math
# b=2
# l=3
# h=(b*b)+(l*l)
# #result=math.sqrt(h)
# result=(h**0.5)
# print(result)





# word=input("Enter the Word")
# cap=word.upper()
# reverse=cap[::-1]
# print(cap==reverse)



# num=int((input("Enter the number of books to buy")))
# costofbook=2*89
# x=costofbook*num
# print("Total Amount to be paid is",x)



# num=input("enter the mobile number")
# numv=num.isdigit()
# f=num[0] in "987"
# if((len(num)==10)&f&numv):
#     print("valid")
# else :
#     print("invalid")

        


# num = input("Enter the ERP number: ")
# if num.isdigit() and len(num) == 12:
#     if num[0] == '2' and num[1] == '1':
#         print("You have to sit in D Block")
#     elif num[0] == '1' and num[1] == '9':
#         print("You have to sit in A Block")
#     elif num[0] == '2' and num[1] == '2':
#         print("You have to sit in N Block")
#     else:
#         print("You have to sit in Corridor")
# else:
#     print("Invalid ERP number. Please enter a 12-digit number.")



# import random
# a=random.randint(1,100)
# guess=a+1
# while guess!=a:
#     guess=int(input("Enter a number"))
#     if(guess<=0):
#         print("Sorry! You are quiting")
#         break;
#     elif(guess<a):
#         print("Number is too small")
#     elif(guess>a):
#         print("Number is too large")
# else:
#     print("The number is right")



# text = input("Enter a paragraph: ")
# para = list(set(text.split()))
# print(para)



# text=input("Enter a paragraph")
# word=text.split()
# para=[]
# c=0
# for words in word :
#     if words not in para:
#         para.append(words)
#         continue
#     c+=1
# newpara=" ".join(para)    
# print(newpara)
# print(f"number of duplicates found{c}")        




# #palindrome numbers from 1 to 1000
# for num in range(1,1000) :
#     num=str(num)
#     if num==num[::-1]:
#         print(num)



# #sorting the numbers
# total = int(input("Enter total number of questions: "))
# qnumbers = []

# print("Enter question numbers here:")
# for i in range(total):
#     question = int(input())
#     qnumbers.append(question)

# print("Selected questions are:", qnumbers)

# for i in range(len(qnumbers)):
#     for j in range(i + 1, len(qnumbers)):
#         if qnumbers[i] > qnumbers[j]:
#             qnumbers[i], qnumbers[j] = qnumbers[j], qnumbers[i]

# print("Selected questions in order:", qnumbers)




# num = int(input("Enter question numbers: "))
# l = []

# print("Enter question numbers here:")
# for i in range(num):
#      question = int(input())
#      l.append(question)
#      l.sort()

# print(l)

# que=int(input("Enter the question number"))
# if que in l:
#      print("page number is",(l.index(que))+1)
# else:
#      print("No answer solved for this wuestion")     


# import time as t
# for i in range(11):
#      print(i)
#      t.sleep(1)


# def os(lst):
#     m = {}

#     def s1(i, j):
#         if i > j:
#             return 0
#         k = (i, j)

#         if k in m:
#             return m[k]

#         o1 = lst[i] + min(s1(i + 2, j), s1(i + 1, j - 1))
#         o2 = lst[j] + min(s1(i + 1, j - 1), s1(i, j - 2))
#         m[k] = max(o1, o2)

#         return m[k]

#     return s1(0, len(lst) - 1)

# lst = list(map(int, input().split()))
# sd = os(lst)
# ts = sum(lst)
# SM = ts - sd

# print(f"Dheeraj wins with {max(sd - SM, 0)} card!")





# def bubblesort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         print(f"Before Pass {i+1}: {arr}")
#         for j in range(n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#         print(f"After Pass {i+1}: {arr}")

# arr = [37, 54, 21, 85, 68, 12, 9, 57]
# print("Initial array:")
# print(arr)
# bubblesort(arr)
# print("Final sorted array:")
# print(arr)




# def find_product(products, id):
#     for i, product in enumerate(products):
#         if product.id == id:
#             return i
#     return -1

# def buy_product(products):
#     id = int(input("Enter the product ID: "))
#     index = find_product(products, id)
#     if index == -1:
#         print("Product not found.")
#         return
#     quantity = int(input("Enter the quantity: "))
#     if quantity > products[index].quantity:
#         print("Not enough quantity available.")
#         return
#     products[index].quantity -= quantity
#     print("Product purchased successfully.")

# def sell_product(products):
#     id = int(input("Enter the product ID: "))
#     index = find_product(products, id)
#     if index == -1:
#         print("Product not found.")
#         return
#     quantity = int(input("Enter the quantity: "))
#     if quantity > products[index].quantity:
#         print("Not enough quantity available.")
#         return
#     products[index].quantity += quantity
#     print("Product sold successfully.")

# def search_product(products):
#     id = int(input("Enter the product ID: "))
#     index = find_product(products, id)
#     if index == -1:
#         print("Product not found.")
#         return
#     print(f"Product ID: {products[index].id}")
#     print(f"Product Name: {products[index].name}")
#     print(f"Price: {products[index].price:.2f}")
#     print(f"Quantity: {products[index].quantity}")

# if __name__ == "__main__":
#     products = [Product(1001, "Apple", 1.50, 100)]
#     num_products = 1

#     choice = 0
#     while choice != 5:
#         display_menu()
#         choice = int(input())
#         if choice == 1:
#             display_products(products)
#         elif choice == 2:
#             buy_product(products)
#         elif choice == 3:
#             sell_product(products)
#         elif choice == 4:
#             search_product(products)
#         elif choice == 5:
#             print("Thank you for using our supermarket system.")
#         else:
#             print("Invalid choice. Please try again.")





#AVL

# class Node(object):
#     def _init_(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.height = 1
# class AVLTree(object):
#     def create (self,data):
#         return Node(data)
    
#     def insert(self, node, data):
#         if node is None:
#             return self.create(data)
#         elif data < node.data:
#             node.left = self.insert(node.left, data)
#         else:
#             node.right = self.insert(node.right, data)
#         node.h = 1 + max(self.Height(node.left),self.Height(node.right))
        
#         b = self.Balance(node)
#         if b > 1 and data < node.left.data:
#             return self.rightRotate(node)
        
#         if b < -1 and data > node.right.data:
#             return self.leftRotate(node)
        
#         if b > 1 and data > node.left.data:
#             node.left = self.leftRotate(node.left)
#             return self.rightRotate(node)
        
#         if b < -1 and data < node.right.data:
#             node.right = self.rightRotate(node.right)
#             return self.leftRotate(node)
        
#         return node
       
#     def leftRotate(self, z):
#         y = z.right
#         T2 = y.left
#         y.left = z
#         z.right = T2
#         z.height = 1 + max(self.Height(z.left),self.Height(z.right))
#         y.height = 1 + max(self.Height(y.left),self.Height(y.right))
#         return y
    
#     def rightRotate(self, z):
#         y = z.left
#         T3 = y.right
#         y.right = z
#         z.left = T3
#         z.height = 1 + max(self.Height(z.left),self.Height(z.right))
#         y.height = 1 + max(self.Height(y.left),self.Height(y.right))
#         return y
    
#     def Height(self, node):
#         if node is None:
#             return 0
#         return node.height
    
#     def Balance(self, node):
#         if node is None:
#             return 0
#         return self.Height(node.left) - self.Height(node.right)
    
#     def display(self, root):
#         if root is not None:
#             self.Inorder(root.left)
#             print(root.data,end=" ")
#             self.Inorder(root.right)
        
# T1 = AVLTree()
# root = T1.create(100)
# T1.insert(root, 50)
# T1.insert(root, 125)
# T1.insert(root, 25)
# T1.insert(root, 75)
# T1.insert(root, 150)
# T1.insert(root, 85)
# T1.insert(root, 175)
# T1.insert(root, 95)
# print("Tree : ")
# T1.display(root)



def is_balanced(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack:
                return False
            if (c == ')' and stack[-1] != '(') or \
               (c == ']' and stack[-1] != '[') or \
               (c == '}' and stack[-1] != '{'):
                return False
            stack.pop()
    return not stack

def balanced_braces(braces):
    result = []
    for s in braces:
        result.append("YES" if is_balanced(s) else "NO")
    return result

if __name__ == "__main__":
    n = int(input())
    braces = [input() for _ in range(n)]
    result = balanced_braces(braces)
    for res in result:
        print(res)
