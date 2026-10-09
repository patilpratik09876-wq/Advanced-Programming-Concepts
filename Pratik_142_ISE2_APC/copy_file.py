import os
with open("input.txt","w") as f:
  f.write(" Hello! Welcome to Python Workshop")
  f.close()

with open("input.txt","r") as f:
  data=f.read().upper()
  f.close()

with open("output.txt","w") as f:
  f.write(data)
  f.close()

print(data)
