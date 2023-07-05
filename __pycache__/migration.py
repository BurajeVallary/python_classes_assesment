class Migration:
    def __init__(self, weatherPattern, riverLevels):
        self.weatherPattern = weatherPattern
        self.riverLevels = riverLevels
        
    def migration(self):
        if self.weatherPattern == "dry" and self.riverLevels == "low":
            print("migration of animals will occur due to lack of water and food in their recent location")
        else:
            print("The migration will not occur because there is presence of food and water")


migrationInstance = Migration("wet", "high")
migrationInstance.migration()
        
    
    