class animal:
    def __init__(self, nome, idade, som):
        self.nome = nome
        self.idade = idade 
        self.som = som     

class Gato(animal):
    def __init__(self, nome, idade, som, raca):
        super().__init__(nome, idade, som) 
        self.raca = raca                   

    def fazer_som(self):
        return "Miau!"

meu_gato = Gato("Luci", 5, "Miau", "Persa")
print(f"Nome do gato: {meu_gato.nome}")
print(f"Idade do gato: {meu_gato.idade}")
print(f"Raça do gato: {meu_gato.raca}")
print(f"Som do gato: {meu_gato.fazer_som()}") 

class Cachorro(animal):
  def __init__(self, nome, idade, som, raca):
    super().__init__(nome, idade, som)
    self.raca = raca

  def fazer_som(self):
    return "Au! Au!"

meu_cachorro = Cachorro("Brutus", 12, "Au! Au!", "Pastor Alemão")
print(f"\nNome do cachorro: {meu_cachorro.nome}")
print(f"Idade do cachorro: {meu_cachorro.idade}")
print(f"Raça do cachorro: {meu_cachorro.raca}")
print(f"Som do cachorro: {meu_cachorro.fazer_som()}")