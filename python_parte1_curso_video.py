#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import random


# In[ ]:


get_ipython().system('pip install -q random')
 


# In[ ]:


get_ipython().system('pip install -q ')


# In[ ]:


# raiz quadrada utilizando biblioteca
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raíz de {} é igual a {}".format(num, math.ceil(raiz)))


# In[ ]:


# numero aleatorio
num_randon = random.random()
print(num_randon)


# In[ ]:


# numero inteiro 
numero =float(input("Digite um número: "))
arrendondar = round(numero)

print("O número {} tem como parte inteira {}".format(numero,arrendondar))


# In[ ]:


# Calculo Hipotenusa 
co = float(input("Digite a medida do cateto oposto: "))
ca = float(input("Digite a medida do cateto adjacente: "))
hip = math.hypot(co, ca)

print("A medida da hipotenusar é {:.2f}".format(round(hip)))


# In[ ]:


# Calculo seno, cosseno, tangente 
n = (float(input("Digite o ângulo desejado: ")))
nd = math.radians(n)
seno = math.sin(nd)
cos = math.cos(nd)
tg = math.tan(nd)


print("Ângulo: {}, seno = {:.2f}, cosseno: {:.2f} e tangente: {:.2f}".format(n, seno, cos, tg))


# In[ ]:


# Escolher o aluno ao acaso
import randon 

al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')

alunos = [al1, al2, al3, al4]

sortear = random.choice(alunos)
# ou ainda 
#sortear = alunos[random.randrange(len(alunos))]
print("O aluno escolhido foi {}". format (sortear))


# In[ ]:


# Escolher o aluno ao acaso
import randon 

al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')

alunos = [al1, al2, al3, al4]
random.shuffle(alunos)

print("O aluno escolhido foi:")
print(alunos)


# In[ ]:


get_ipython().system('pip install pygame')


# In[ ]:


import pygame
pygame.init()
#pygame.mixer.music.load("memories.mp3")
pygame.mixer.music.play()
pygame.event.wait()


# In[12]:


# Manipulando strings 
frase = 'Curso em vídeo Python'
frase


# In[37]:


## Fatiamento 


# In[20]:


# de uma letra até a outra
frase[9:14]
# de uma letra até a outra, pulando de 2 em 2 
frase[9:14:2]
# de uma letra até o fim
frase[2:]


# In[29]:


frase[9::3]


# In[38]:


##Análise


# In[31]:


#comprimento da String 
len(frase)


# In[42]:


frase.count('o')


# In[41]:


#contagem de letras dentro da string
frase.count('o', 0, 21)


# In[43]:


#encontre 
frase.find('deo')


# In[44]:


# se ele não encontra, não há resultado, ele retorna -1 
frase.find('Android')


# In[45]:


#operador
"Curso" in frase


# In[46]:


##Transformação 


# In[47]:


#trocar palavras
frase.replace("Python", "Android")


# In[49]:


nome2 = frase.replace("Python", "Matheus")


# In[50]:


nome2


# In[51]:


frase


# In[52]:


#letras em maiúsculo 
frase.upper()


# In[55]:


#letras minúsculas 
frase.lower()


# In[56]:


frase


# In[57]:


#primeira letra em maiúculo e o restante em minúsculo
frase.capitalize()


# In[58]:


#Analisa quantas palavras tem e o capitalize palavra por palavra
frase.title()


# In[62]:


frase2 = "     Aprenda Python      "
frase2


# In[61]:


#remove os espaços desnecessários de ambos os lados
frase2.strip()


# In[63]:


#remove somento os  espaços da direita
frase2.rstrip()


# In[64]:


#remove somento os  espaços da esquerda
frase2.lstrip()


# In[65]:


## divisão 


# In[68]:


#divisão das string onde há espaços
#cria uma lista com cada palavra
frase.split()


# In[69]:


#pode chamar cada um dos elementos da lista
frase.split()[2]


# In[70]:


## Junção 


# In[71]:


#usar o separador hiven para separar letra por letra
'-'.join(frase)


# In[72]:


' '.join(frase)


# In[76]:


print(frase.replace("Python", "Pamella"))


# In[56]:


## Desafio 022
nome = str(input("Digite seu nome: ")).strip()
print("Seu nome em maiúsculo é {}".format(nome.upper()))
print("Seu nome em minúsculo é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome.replace(" ",""))))
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))


# In[18]:


## Desafio 023
num = input("Digite um número de 0 a 9999: ")
num_sep = (' '.join(num)).split()

qtde = len(num_sep)

if qtde == 1: 
    print("Unidade: {}".format(num_sep[0]))
if qtde == 2: 
    print("Unidade: {}".format(num_sep[1]))
    print("Dezena {}".format(num_sep[0]))
if qtde == 3:
    print("Unidade: {}".format(num_sep[2]))
    print("Dezena {}".format(num_sep[1]))
    print("Centena: {}".format(num_sep[0]))
if qtde == 4:
    print("Unidade: {}".format(num_sep[3]))
    print("Dezena {}".format(num_sep[2]))
    print("Centena: {}".format(num_sep[1]))
    print("Milhar: {}".format(num_sep[0]))


# In[61]:


## refazendo o 023 de acordo com o vídeo
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10 
d = num // 10 % 10 
c = num // 100 % 10 
m = num // 1000 % 10 

print("Unidade: {}".format(u))
print("Dezena {}".format(c))
print("Centena: {}".format(d))
print("Milhar: {}".format(m))


# In[67]:


## Desafio 024
cidade = str(input('Em que cidade você nasceu? ')).strip()
cidadeupper = cidade.upper()
cid = cidadeupper.split()

if 'SANTO' in cid[0]:
    print("Há a palavra Santo na sua cidade")
else:
    print("Não há a palavra Santo na sua cidade")


# In[72]:


## Desafio 025 
nome_silva = str(input('Digite o seu nome: ')).strip()
nome_s_u = nome_silva.upper()

if 'SILVA' in nome_s_u:
    print('Seu nome contém Silva')
else: 
    print('Seu nome não contém Silva')


# In[1]:


## Desafio 026
frase = input('Digite a sua frase: ').strip()
frase_up = frase.upper()
numas = frase_up.count('A')

print('------------------------------------------')
print('Há nesta frase {} lestras a na frase'. format(numas))
print('------------------------------------------')
print('A primeira letra a aparece na posição {}'. format(frase_up.find('A')+1))
print('------------------------------------------')
print('A ultima letra a aparece na posição {}'. format(frase_up.rfind('A')+1))


# In[3]:


## Desafio 027 
nome_completo = input('Digite seu nome completo: ').strip()
nome_sep = nome_completo.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_sep[0]))
print('Seu último nome é {}'. format(nome_sep[len(nome_sep) - 1]))


# In[ ]:




