a = [5, 2, 8, 3, 6, 1, 4]

a_even = []

a_odd = []

for i in a:
  if i % 2 == 0:
    a_even.append(i)
  else:
    a_odd.append(i)
print(a_even) 
print(a_odd)

new_list = []
max_len = max(len(a_even), len(a_odd))

for j in range(max_len):
  if j < range(a_even):
    new_list.append(a_even[j])
  if j < range(a_odd):
    new_list.append(a_odd[j]) 
print(new_list)
