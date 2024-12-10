class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(peoples: list) -> list:
    person_list = []
    for pers in peoples:
        person = Person(pers["name"], pers["age"])
        person_list.append(person)
    for pers in peoples:
        person = Person.people[pers["name"]]
        if "wife" in pers and pers["wife"] is not None:
            setattr(person, "wife", Person.people.get(pers["wife"]))
        if "husband" in pers and pers["husband"] is not None:
            setattr(person, "husband", Person.people.get(pers["husband"]))
    return person_list
