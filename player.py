# Importer itertools, som f.eks. kan bruges til at lave ID'er
import itertools

# Klassen player
class Player():
    # Definere __init__ med parameterene name, age og team
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team

    # Funktionen get_all_info som retunere variablerne og en beskrivelse.
    def get_all_info(self):
        return f"Spilleren hedder {self.name}, han er {self.age} år gammel. Han spiller for {self.team}"

# Klassen Attacker, som er har superklassen Player
class Attacker(Player):
    # Sætter id_generator til at starte ved 1
    id_generator = itertools.count(1)
    # Definere __init__ med parameterene name, age, team, goals, position="attacker"
    def __init__(self, name, age, team, goals, position="Attacker"):
        # Inkludere superklassen, hvor der skal bruges parameterne name, age og team
        super().__init__(name, age, team)
        # Sætter id til den næste, altså 1,2,3,4 osv
        self.id = next(self.id_generator)
        # Sætter goals lig med inputtet for goals
        self.goals = goals

# Klassen Midfielder, som har superklassen Player
class Midfielder(Player):
    # Sætter id_generator til at starte ved 1
    id_generator = itertools.count(1)
    # Definere __init__ med parameterene name, age, team, passes, position="Midfielder"
    def __init__(self, name, age, team, passes, position="Midfielder"):
        # Inkludere superklassen, hvor der skal bruges parameterne name, age og team
        super().__init__(name, age, team)
        # Sætter passes lig med inputtet for passes
        self.passes = passes
        # Sætter id til den næste, altså 1,2,3,4 osv
        self.id = next(self.id_generator)

# Klassen Defender, som har superklassen Player
class Defender(Player):
    # Sætter id_generator til at starte ved 1
    id_generator = itertools.count(1)
    # Definere __init__ med parameterene name, age, team, blocked, position="Defender"
    def __init__(self, name, age, team, blocked, position="Defender"):
        # Inkludere superklassen, hvor der skal bruges parameterne name, age og team
        super().__init__(name, age, team)
        # Sætter blocked lig med inputtet for blocked
        self.blocked = blocked
        # Sætter id til den næste, altså 1,2,3,4 osv
        self.id = next(self.id_generator)

# Klassen Goalkeeper, som har superklassen Player
class Goalkeeper(Player):
    # Sætter id_generator til at starte ved 1
    id_generator = itertools.count(1)
    # Definere __init__ med parameterene name, age, team, position, position="Goalkeeper"
    def __init__(self, name, age, team, saves, position="Goalkeeper"):
        # Inkludere superklassen, hvor der skal bruges parameterne name, age og team
        super().__init__(name, age, team)
        # Sætter saves lig med inputtet for saves
        self.saves = saves
        # Sætter id til den næste, altså 1,2,3,4 osv
        self.id = next(self.id_generator)