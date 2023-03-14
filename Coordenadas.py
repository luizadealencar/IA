class Coordenadas:
    coordx: int 
    coordy: int
    aux = None
    FGH: []

    def __init__(self, x, y, aux = None):
      self.coordx = x
      self.coordy = y
      self.aux = aux
