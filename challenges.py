import re

def palindrome(string: str):
  string = re.sub("[^a-zA-Z0-9]", "", string).lower().replace(" ", "")
  print(string)
  return string == string[::-1]

print(palindrome("kayak"))
print(palindrome("never odd or even"))
print(palindrome("Was it a car or a cat I saw ?"))

import os
def list_files(path):
  for i in os.scandir(path):
    if i.is_dir():
      list_files(i.path)
    else:
      print(i)

list_files("./")

def lower(s, n):
  return len(re.findall("[a-z]", s)) >= n

def upper(s, n):
  return len(re.findall("[A-Z]", s)) >= n

def length(s, n):
  return len(s) >= n

def special(s, n):
  return len(re.findall("[.*_-]", s)) >= n

def number(s, n):
  return len(re.findall("[0-9]", s)) >= n

def check_password(function, length, password):
  try:
    return bool(function(password, length))
  except:
    print("Error while trying to execute function")
    return False

pwd = "mysecretpassword.-"

print(check_password(lower, 4, pwd) and check_password(special, 2, pwd))