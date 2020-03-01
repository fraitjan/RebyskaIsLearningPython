import random


class Animals:
    def __init__(self, file):
        self.animals = list()
        with open(file, 'r+') as file:
            header = file.readline().split(",")
            for line in file:
                self.animals.append(dict([z for z in zip(header, line.split(","))]))

    def get_random_animal(self):
        return random.choice(self.animals)

    def get_specific_animal(self, name):
        if type(name) == str:
            return self._get_one(name)
        elif type(name) == list:
            ret = list()
            for n in name:
                for r in self._get_one(n):
                    if r not in ret:
                        ret.append(r)
            return ret

    def _get_one(self, name):
        return [a for a in self.animals if (
                " " + name.lower() + " " in a["Common name"].lower()
                or
                a["Common name"].lower().startswith(name.lower() + " ")
                or
                a["Common name"].lower().endswith(" " + name.lower())
                or
                a["Common name"].lower() == name.lower())]
