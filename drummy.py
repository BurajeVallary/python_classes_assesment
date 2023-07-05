class Drum:
    def __init__(self,material,size):
        self.size=size
        self.material=material

    def predictSound(self):
        print(f"{self.__class__.__name__},{self.sound} and its material is {self.material} which is {self.size}")


class Djembe(Drum):
    sound="Wide range of tones"

class TalkingDrum(Drum):
    sound="Mimics lines of human speech"

class Bougarabou(Drum):
    sound="Deep bass tones"    


drum1=TalkingDrum("Leather","Small")    
drum1.predictSound()
        