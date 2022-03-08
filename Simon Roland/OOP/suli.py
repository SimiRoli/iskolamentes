class Embik:
    def __init__(self, nev):
        self.nev = nev
    def bemutatkozik(self):
        print(f"Szia a nevem {self.nev}", end=" ")
class Diakok(Embik):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly

    def bemutatkozik(self):
        super().bemutatkozik()
        print(f" és a(z) {self.osztaly} osztályba járok")

class Tanar(Embik):
    def __init__(self, nev, szak):
        super().__init__(nev)
        self.szak = szak

    def bemutatkozik(self):
        super().bemutatkozik()
        print("".join(self.szak), "szakos tanár vagyok")

diak_01 = Diakok ('Kiss Péter', "10.A")
tanar_01 = Tanar ('Horváth Zita', 'biológia-kémia' )
tanar_02 = Tanar ('Schmidt Emil', 'matematika')


diak_01.bemutatkozik()
tanar_01.bemutatkozik()
tanar_02.bemutatkozik()