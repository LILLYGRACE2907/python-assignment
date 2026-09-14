class Movie:
    def __init__(self, name, hero, year, rating):
        self.name = name
        self.hero = hero
        self.year = year
        self.rating = rating

    def display(self):
        print("Movie:", self.name)
        print("Hero:", self.hero)
        print("Year:", self.year)
        print("Rating:", self.rating)


m = Movie("RRR", "Ram Charan", 2022, 9)

m.display()