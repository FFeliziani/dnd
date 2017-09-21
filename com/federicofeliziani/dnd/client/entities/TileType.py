class TileType:
    name = ""
    path = ""
    speed = 1.0

    def by_name(self, name="Dirt"):
        if name.lower().strip() == "dirt" or name.lower().strip() == "d":
            self.name = "Dirt"
            self.path = b"dirt.png"
            self.speed = 1.0
        if name.lower().strip() == "concrete" or name.lower().strip() == "c":
            self.name = "Concrete"
            self.path = b"concrete.jpg"
            self.speed = 1.0
        return self
