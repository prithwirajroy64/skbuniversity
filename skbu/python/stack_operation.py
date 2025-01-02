def push():
  global top, size
  if top < size - 1 :
    n = input("Type for adding: ")
    top += 1
    stack.append(n) 
  else:
        print("Stack Overflow! Cannot add more elements.")
  decision()
    
def pop():
  global top
  if top >= 0:
    stack.pop()
    top -= 1
  else:
    print("Stack Underflow! No elements to remove.")
  decision()
    
def peek():
  if stack:
    print("Top element: ", stack[-1])
  else:
    print("Stack is empty.")
  decision()
  
def display():
  if stack:
    print("Stack is: ", stack)
  else:
    print("Stack is empty.")
  decision()

def instraction():
  print('''Press 1 for push.
Press 2 for pop.
Press 3 for peek.
Press 4 for display.
Press 5 for exit.''')

def decision():
  n = input("Do you want to continue?(y/n)")
  if n == 'y':
    instraction()
    s()
  else:
    exit()


def s():
  while True:
    n=int(input("Choose option: "))
    if n > 0 and n <= 5:
      if n==1:
        push()
        print()
        instraction()
      elif n == 2:
        pop()
        print()
        instraction()
      elif n == 3:
        peek()
        print()
        instraction()
      elif n == 4:
        display()
        print()
        instraction()
      elif n == 5:
        break
    else:
      print("Enter a valid number.")
 
top = -1
size = 4
stack = []
     
instraction()      
s()