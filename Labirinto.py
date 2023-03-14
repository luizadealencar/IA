class Labirinto:
  grid = []

  def __init__(self, txtFile):
    file = open(txtFile, "r")
    linha = file.readline()
    while (linha != ""):
        lista = linha.strip().split(" ")
        self.grid.append(lista)
        linha = file.readline()
