class Laptop:
    made_in = "Germany"

    def __init__(self, memory:int, model:str, price: float):
        self.memory = memory
        self.model = model
        self.price = price

    @classmethod    # създава точно определена инстанция на класа
    def low_ram_laptop(cls):
        return cls(256, "Asus")

    @classmethod
    def made_in_other(cls):
        cls.made_in = "Neverland"
        return f"{cls.made_in}"
