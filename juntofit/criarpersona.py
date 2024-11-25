#'''Individualmente
# Crie uma persona com a biblioteca  com nome, idade e cidade.
# Criando o atributo random.int para gerar valores aleatórios para idade.'''

from faker import Faker
import csv
fake = Faker()
fake = Faker('pt_BR')

nome = fake.name()
nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
idade = (2024 - nascimento.year)
cidade = fake.city()
print (nome, cidade, idade)

def criar_persona_lista():
 persona_lista = []
 
 for i in range (15):
        nome = fake.name()
        persona_lista.append(nome)
 return (persona_lista)
print (criar_persona_lista())