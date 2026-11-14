a = ['15', '42', '7', '33', '28']

max_a = int(a[0]) 

for i in a:
  if int(i) > max_a:
    max_a = int(i)

print(max_a)
