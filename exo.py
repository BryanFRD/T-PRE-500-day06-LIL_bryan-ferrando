def bread():
  print("<//////////>")
def lettuce():
  print("~~~~~~~~~~~~")
def tomato():
  print("O O O O O O ")
def ham():
  print("============")

def make_sandwiches(number: int, vegan: bool = False):
  if(number < 0):
    return
  
  for i in range(number):
    bread()
    lettuce()
    tomato()
    if vegan:
      ham()
      ham()
    bread()

make_sandwiches(1)
make_sandwiches(1, True)

import time

start = time.time_ns()

def power(number, power):
  return number**power

print(power(2, 999))
print(f"{(time.time_ns() - start)/1000}ms")