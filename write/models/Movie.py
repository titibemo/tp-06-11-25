class Movie:
    id = 31

    def __init__(self, titre: str, annee_production: int, genre: str, age_limite: int):
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite
        self.id += 1

    def __str__(self):
        print(f"{self.titre} - {self.annee_production}, {self.genre}, {self.age_limite}")
