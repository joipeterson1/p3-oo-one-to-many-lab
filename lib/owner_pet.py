class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self._pet_type = pet_type
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value in Pet.PET_TYPES:
            self._pet_type = value
        else:
            raise Exception
        

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
       return Pet.all
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        else:
            pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        return sorted_pets
    
