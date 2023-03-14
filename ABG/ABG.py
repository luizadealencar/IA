import random
import math

geracoes=[]
novageracao=[]

def inicializarpopulacao():
	individuos=10
	min=-20
	max=20 
	bits=16 
	populacao=[]
	for i in range(individuos):
		cromossomos=''
		for j in range(bits):
			bit=random.randint(0, 1)
			if cromossomos=='':
				cromossomos=str(bit)
			else:
				cromossomos+=str(bit)
		populacao.append([cromossomos, math.inf])
	populacao=decodificar(min, max, bits, populacao)
	return populacao

def decodificar(min, max, bits, populacao):
	for i in range(len(populacao)):
		decimal=int(populacao[i][0], 2)
		x=min+(((max-min)*decimal)/((2**bits)-1))
		f=round((math.cos(x)*x)+2, 2)
		populacao[i][1]=f
	populacao.sort(key=lambda x: x[1])
	return populacao

def selecao(populacao):
	listapais=[]
	for i in range(len(populacao)):
		aux1=populacao[random.randint(0, len(populacao)-1)]
		aux2=populacao[random.randint(0, len(populacao)-1)]
		if min(aux1[1], aux2[1])==aux1[1]:
			aux=aux1
		else:
			aux=aux2
		listapais.append(aux)
	return listapais

def crossover(listapais, n):
	listafilhos=[]
	for i in range(0, len(listapais)-1, n):
		r=round(random.uniform(0, 1), 1)
		if r<=0.6:
			corte=random.randint(1, 16)
			aux1=listapais[i][0]
			aux2=listapais[i+1][0]
			index1=[aux1[0:corte]+aux2[corte:len(aux2)], math.inf]
			index2=[aux2[0:corte]+aux1[corte:len(aux1)], math.inf]
		else:
			index1=listapais[i]
			index2=listapais[i+1]
		listafilhos.append(index1)
		listafilhos.append(index2)
	return listafilhos

def mutacao(listafilhos):
	for i in range(len(listafilhos)):
		individuo=listafilhos[i][0]
		for j in range(len(individuo)):
			r=round(random.uniform(0, 1), 2)
			if r<=0.01:
				if individuo[j]=="0":
					individuo=individuo[:j]+"1"+individuo[j+1:]
				else:
					individuo=individuo[:j]+"0"+individuo[j+1:]
	decodificar(-20, 20, 16, listafilhos)
	return listafilhos

def elitismo(listafilhos, populacao):
	listafilhos.sort(key=lambda x:x[1])
	populacao.sort(key=lambda x:x[1])
	if listafilhos[-1]>populacao[0]:
		for i in range(len(listafilhos)):
			if listafilhos[i][1]==populacao[-1][1]:
				del listafilhos[i]
				break
		listafilhos.append(populacao[0])
	listafilhos.sort(key=lambda x:x[1])
	novageracao=listafilhos.copy()
	geracoes.append(novageracao)
	novageracao=[]

def ImpimirMedia():
	dic={}
	i=1
	for geracao in geracoes:
		soma=0
		dic["Geracao %d" %(i)]=0
		for individuo in geracao:
			soma+=individuo[1]
		dic["Geracao %d" %(i)]+=soma/len(geracao)
		i+=1
	print("GERAÇÃO \t MÉDIA")
	for ger in dic.keys():
		print("%s \t %.2f" %(ger, dic[ger]))
	print()


def main():
	#global geracoes
	n=2
	qtdGeracoes=10
	totalGeracoes=2
	while totalGeracoes>0:
		populacao=inicializarpopulacao()
		solucao=True
		while solucao:
			listapais=selecao(populacao)
			listafilhos=crossover(listapais, n)
			listafilhos=mutacao(listafilhos)
			elitismo(listafilhos, populacao)
			if len(geracoes)==qtdGeracoes:
				ImpimirMedia()
				solucao=False
				listapais=selecao(populacao)
				listafilhos=crossover(listapais, n)
				listafilhos=mutacao(listafilhos)
				elitismo(listafilhos, populacao)
				if len(geracoes)==qtdGeracoes:
					ImpimirMedia()
					solucao=False
		totalGeracoes-=1
		qtdGeracoes=20

if __name__=='__main__':
  main()