#print the table of 9 except for 9*5

for i in range(1,11):
   if i == 5:
      continue 
   print(f"9 * {i} = {9 * i}")
print("Loop ended")
