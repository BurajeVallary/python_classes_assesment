class Migration:
    def __init__(self, weatherPattern, riverLevels, species, location):
        self.weatherPattern = weatherPattern
        self.riverLevels = riverLevels
        self.species = species
        self.location = location

    def migration(self):
        riverlevel = "low"
        weatherPattern = "dry"

        if self.weatherPattern == weatherPattern and self.riverLevels == riverlevel:
            print(f"migration of {self.species} will occur from {self.location} due to lack of water and food in their recent location")
        else:
            print(f"migration of {self.species} will occur from {self.location} due to lack of water and food in their recent location")

migrationInstance = Migration("dry", "low", "Zebra", "Serengeti")
migrationInstance.migration()