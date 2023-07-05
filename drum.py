class Drum:
    def __init__(self,material,size):
        self.material=material
        self.size=size
    def predict_sound(self):
        print(f"{self.__class__.__name__},{self.sound}")
class Djembe(Drum):
    sound=("produces a saprano sound")
class TalkingDrum(Drum):
    sound=("Produces a soft sound")
class Bougarabao(Drum):
    sound=("produces a base sound")
drum1=TalkingDrum("skin","big")
drum1.predict_sound()
drum2=Djembe("smooth animal skin","small")
drum2.predict_sound()
drum3=Bougarabao("smooth animal skin","small")
drum3.predict_sound()