san=int(input("Sandy engiziniz:"))
san2=int(input("2 sandy engiziniz:"))

def qosu (birinshi_san,ekinshi_san):
   nat=birinshi_san+ekinshi_san
   print("eki san kosyndysy:",nat)

def azaitu (birinshi_san,ekinshi_san):
   nat=birinshi_san-ekinshi_san
   print("eki san aiyrmasy:",nat)

def kobeitu (birinshi_san,ekinshi_san):
   nat=birinshi_san*ekinshi_san
   print("eki san kobeitindisi:",nat)

def bolu (birinshi_san,ekinshi_san):
   nat=birinshi_san/ekinshi_san
   print("eki san bolindisi:",nat)

qosu(san,san2)
azaitu(san,san2)
kobeitu(san,san2)
bolu(san,san2)