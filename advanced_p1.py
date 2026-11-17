marks = [4, 9, 7, 5, 10, 3, 8, 6, 9, 2] 

tot = []
kha = []
trung_binh = []
yeu = [] 

for mark in marks:
  if mark >= 8: 
    tot.append(mark)
  if mark >= float(6.5) and mark <8:
    kha.append(int(mark))
  if mark >= 5 and mark < float(6.5):
    trung_binh.append(int(mark))
  if mark < 5: 
    yeu.append(mark)
print("Cac diem tot la" + str(tot))
print("Cac diem kha la" + str(kha))
print("Cac diem trung binh la"+ str(trung_binh))
print("Cac diem yeu la" + str(yeu))
