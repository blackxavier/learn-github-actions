first_number = 2
second_number  = 3

total = first_number + second_number
print(total)

def multiple(x,y):
  return x*y

def test_add():
  assert multiple(2,3) == 6
  assert multiple(4,4) == 16
