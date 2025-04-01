count = 0

def add():
    global count
    count += 1

class bob:
    def forward(self):
        add()
    def backward(self):
        add()
    def right(self):
        add()
    def left(self):
        add()


n = 10
for i in range(n):
  for j in range(n):
      for k in range(n):
        bob.forward(10)
        bob.right(360/n)
      bob.forward(20)
  bob.right(360/n)


print(count)