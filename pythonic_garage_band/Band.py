from abc import abstractmethod, ABC


class Band():
    instances, allBand, soloList = [], [], []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        for i, member in enumerate(self.members):
            if member.get_instrument() == 'guitar':
                Band.soloList.append("face melting guitar solo")
            elif member.get_instrument() == 'bass':
                Band.soloList.append("bom bom buh bom")
            elif member.get_instrument() == 'drums':
                Band.soloList.append("rattle boom crash")
        return Band.soloList

    def __str__(self): return f"{self.name}"

    def __repr__(self): return f"{self.name}"

    @classmethod
    def to_list(cls): return cls.instances


class Musician():
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self): pass

    @abstractmethod
    def __repr__(self): pass

    def play_solo(self): pass


class Guitarist(Musician):
    def __str__(self): return f"My name is {self.name} and I play guitar"

    def __repr__(self): return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self): return 'guitar'

    def play_solo(self): return "face melting guitar solo"


class Bassist(Musician):
    def __str__(self): return f"My name is {self.name} and I play bass"

    def __repr__(self): return f"Bassist instance. Name = {self.name}"

    def get_instrument(self): return 'bass'

    def play_solo(self): return "bom bom buh bom"


class Drummer(Musician):
    def __str__(self): return f"My name is {self.name} and I play drums"

    def __repr__(self): return f"Drummer instance. Name = {self.name}"

    def get_instrument(self): return 'drums'

    def play_solo(self): return "rattle boom crash"
