class Ankara:
    def __init__(self, temperature, mood):
        self.temperature = temperature
        self.mood = mood
    def get_pattern(self):
        if self.temperature >= 20 and self.mood >= 5:
            return "Wear light and more patterned Ankara."
        else:
            return "Wear dull and less patterned Ankara."
    # def set_temperature(self, temperature):
    #     self.temperature = temperature
    # def set_mood(self, mood):
    #     self.mood = mood
ankara = Ankara(20, 7)
print(ankara.get_pattern())

ankara=Ankara(15,3)
print(ankara.get_pattern())


# class Ankara:
#     def __init__(self,temperature,mood):
#         self.mood=mood
#         self.temperature=temperature
#     def detect_pattern_changes(self):
#       moods = ["happy","sad","bored"]
#       if self.temperature>30 and self.mood in moods:
#             return f"The pattern changes to Polka dot"
#       elif self.temperature<30 and self.mood in moods:
#             return f"The pattern changes to Wavy"
#       else:
#             return f"The pattern does not change"
# person=Ankara(20,"sad")
# print(person.detect_pattern_changes())

# class Ankara:
#     def __init__(self,temperature,mood):
#         self.temperature=temperature
#         self.mood=mood

 
#     def get_pattern(self):
#      mood=["happy","sad"]
#      if self.temperature>30 and self.mood in mood:
#          return f"The pattern changes to polka"
#      elif self.temperature<30 and self.mood in mood:
#          return f"The pattern changes to wavy"
#      else :
#          return f"The pattern does not change"
     


# person=Ankara (20,"sad") 
# print(person.get_pattern())  

# class Ankara:
#     def __init__(self,temperature,mood):
#         self.temperature=temperature
#         self.mood=mood

#     def get_pattern(self):
#         mood=["sad","happy"]

#         if self.temperature>30 and self.mood in mood:
#             return f"The pattern changes to polkar dots"
#         elif self.temperature<30  and self.mood in mood:
#             return f"The pattern changes to wavy"
#         else:
#             return f"The pattern did not change"
        
# person=Ankara(20,"Happy") 
# print(person.get_pattern())       


          



         
      
        
        