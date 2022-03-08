class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz
    def kerulet (self):
        return self.oldal_hossz * 4 
    def terulet (self):
        return self.oldal_hossz * self.oldal_hossz
    def info(self):
        print(f'A(z) {self.oldal_hossz} oldalhosszúságú négyzet területe {self.terulet()}, kerülete {self.kerulet()} ')

negyzet_01 = Negyzet (10)
print(negyzet_01.info())

negyzetek = []
hossz = int(input('Add meg a négyzet hosszát! '))
while hossz != 0:
    negyzet = Negyzet(hossz)
    negyzetek.append(negyzet)
    hossz = int(input("Add meg a négyzet hosszát! "))
for index in range (len(negyzetek)):
    print(index, negyzetek[index])

    
