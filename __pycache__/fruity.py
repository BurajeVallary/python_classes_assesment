class Baobab:
     def __init__(self,fruit,power,effect,season):
          self.fruit=fruit
          self.power=power
          self.effect=effect
          self.season=season
     def show(self):
        return f"Baobab(fruit='{self.fruit}', power='{self.power}', effect='{self.effect}', season='{self.season}')"
fruit1=Baobab(fruit="Baobab fruit",power="Strenght",effect="strong",season="dry")
fruit2=Baobab(fruit="Mango",power="Strenght",effect="strong",season="wet")
fruit3=Baobab(fruit="Banana",power="Strenght",effect="strong",season="wet")
database=[]
database.extend([fruit1,fruit2,fruit3])
print(database)
class Season:
     def __init__(self,season):
          self.season=season
     def predictFruit(self):
      listoffruits=[fruit for fruit in database if fruit.season==self.season]
      for fruit in listoffruits:
       print (   f"fruit:{fruit.fruit},power:{fruit.power},effect:{fruit.effect}")
s=Season(season="wet")
s.predictFruit()   

        

        