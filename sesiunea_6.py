#definitia unei clase : cuvantul cheie class, NumeClass : NumeClass():
# CLASELE INCEP CU LITERA MARE
class Dog:
   #atribute - variabilele clasei
   nume = 'Ziki'
   rasa = 'labrador'
   varsta = 5
   pedigree= True

   #metode- functiile clasei, comportamentul unui subiect de tip Dog
   #constructor explicit
   def __init__(self, nume, rasa, pedigree):
      self.nume = nume
      self.rasa = rasa
      self.pedigree = pedigree
   def adu_batu(self):
       print(f'{self.nume} aduce batul!')

ziki= Dog("Ziki","labrador",True)
ziki.adu_batu()