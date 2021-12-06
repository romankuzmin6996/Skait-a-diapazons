def noteiktDiapozonu(d1, d2, sk) :
  rezultats = "Skaitlis nav diapazonā!"
  if d1>=sk<=d2:
    rezultats = "Skaitlis ir diapozonā!"
  return rezultats

d1 = int(input("Ievadi diapozona sākuma:"))
d2 = int(input("Ievadi diapozona beiguma:"))
sk = int(input("Ievadi skaitli:"))
rez = noteiktDiapozonu(d1, d2, sk)
print(rez)