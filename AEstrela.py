from funcoes.Labirinto import Labirinto
from funcoes.Coordenadas import Coordenadas

class AEstrela:
  mapa = Labirinto
  partida: Coordenadas
  chegada: Coordenadas
  lstaberta=[]
  lstfechada=[]
  caminho=[]

  def __init__(self, mapa, inicio, fim):
    self.mapa=mapa
    if ( self.Acessivel(inicio)==False or self.Acessivel(fim)==False):
      print("Ponto de inicio ou final não válidos")
      return None
    self.partida=inicio
    self.chegada=fim

  def EncontrarCaminho(self):
    self.partida.FGH=self.CalculaFGH(self.partida)
    self.lstaberta.append(self.partida)
    self.caminho=[] 

    while(True):
      self.Ordenacao(self.lstaberta)
      corrente=self.lstaberta[0]
      del self.lstaberta[0]
      self.lstfechada.append(corrente)
      caminho=self.CaminhosExistentes(corrente)
      for i in caminho:
        index=self.ExisteCaminho(i, self.lstaberta)
        if (index==-1):
          self.lstaberta.append(i)
        else:
          if (i.FGH[1]<self.lstaberta[index].FGH[1]):
            self.lstaberta[index]=i
      indexChegada=self.ExisteCaminho(self.chegada, self.lstfechada)
      if (indexChegada>=0):
        self.caminho.append(self.lstfechada[indexChegada])
        aux=self.lstfechada[indexChegada].aux

        while (aux!=None):
          self.caminho.append(aux)
          aux=aux.aux
        return self.caminho

      if (len(self.lstaberta)==0):
        return None

  def Ordenacao(self, lstaberta):
    return lstaberta.sort(key= lambda Coordenadas: Coordenadas.FGH[0])

  def ExisteCaminho(self, j, lista):
    for i in range(len(lista)):
      if (lista[i].coordx==j.coordx and lista[i].coordy==j.coordy):
        return i
    return -1

  def  HeuristicaEuclidiana(self, x, y):
    return ((self.chegada.coordx - x)**2 + (self.chegada.coordy - y)**2)**(1/2) 

  def CalculaFGH(self, i):
    x=i.coordx
    y=i.coordy
    aux=i.aux
    h=self.HeuristicaEuclidiana(x,y)
    g=0
    while (aux!=None):
      g=g+10
      aux=aux.aux
    f=h+g
    return [f, g, h]

  def Acessivel(self, i):
    x=i.coordx
    y=i.coordy
    if (x<0 or y<0):
      return False
    if (x>len(self.mapa.grid)-1 or y>len(self.mapa.grid[0])-1):
      return False
    if (self.ExisteCaminho(i, self.lstfechada)>=0):
      return False
    if (self.mapa.grid[x][y]=="1"):
      return False
    return True  

  def CaminhosExistentes(self, i):
    lst=[]
    x=i.coordx
    y=i.coordy
    no1=Coordenadas(x-1, y, i)
    no2=Coordenadas(x+1, y, i)
    no3=Coordenadas(x, y-1, i)
    no4=Coordenadas(x, y+1, i)
    preNos=[no1,no2,no3,no4]

    for j in preNos:
      if (self.Acessivel(j)):
        j.FGH = self.CalculaFGH(j)
        lst.append(j)

    return lst

  def Impressao(self):
    if  (len(self.caminho)>0):
      for i in range(len(self.caminho)-1,-1,-1):
          if (i!=0):
              print( f"{self.caminho[i].coordx}-{self.caminho[i].coordy} -> ", end="")
          else:
              print( f"{self.caminho[i].coordx}-{self.caminho[i].coordy}.", end="")
    else:
      print( "Não existe caminho")
