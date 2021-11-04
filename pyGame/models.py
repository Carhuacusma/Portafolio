class Entity:
    def __init__(self, health_points: int, hit_points: int):
        self.health_points = health_points
        self.hit_points = hit_points

    def __repr__(self) -> str:
        return ''.join(['SALUD: ',str(self.health_points)])

    def recibir_golpe(self, damage: int) -> None:
        self.health_points -= damage

aux = Entity(10,5)
aux.recibir_golpe(6)
print(aux)