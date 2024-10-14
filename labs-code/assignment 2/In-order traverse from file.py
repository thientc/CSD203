'''
input.txt:
        2 4 6 8 0 0 0 0 0 
        3 5 7 9 0 0 0 0 0      
               ||
              \||/
matrix: [[2,4,6,8,0,0,0,0,0],[3,5,7,9,0,0,0,0,0]]
     
           1
      2        3 
   4    5    6   7
 8   9
'''
arr = []

class Node:
  def __init__(self,info):
      self.info = info
      self.left = None  
      self.right = None 

def _readfile():
  input = open('binarb.txt','r')  
  for lines in input.readlines():
      k = 1
      arr1 = []
      for i in range(len(lines.split())+1):
          arr1.append(0)
      for i in lines.split():
          arr1[k] = int(i)
          k +=1
      arr.append(arr1) 
  return arr

arr = _readfile()

def _createarb(index):

    if index != 0:
       new = Node(index)
       new.left = _createarb(arr[0][index])
       new.right = _createarb(arr[1][index])
       return new
    else: return None 
 
out = []
def _inorder(node):
    if node is not None:
       _inorder(node.left)
       out.append(node.info)  
       _inorder(node.right) 

root = _createarb(1)
print "Inorder:"
_inorder(root)
print out

