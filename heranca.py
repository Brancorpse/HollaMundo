# Herança é quando uma classe herda métodos e funções de outra classe. reusa o código
# Exercício exemplo herança

# Classe mãe criada inicialmente, onde as filhas herdarão funções

class Mammal:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print("walk")

# Agora, as classes Dog e Cat herdará a função da classe mãe

class Dog(Mammal):
    def bark(self):
        print(f"Eu sou {self.name}")
        print("Au Au Au")



# Sempre reuse seu código. Não se repita. Deixará o código melhor
# Instanciando objetos

class Cat(Mammal):
    def meow(self):
        print(f"Eu sou {self.name}")
        print("Miau miau")

sabbath = Dog("Eu sou Sabbath")
sabbath.walk()
sabbath.bark()

batou = Cat("Eu sou Batou")
batou.walk()
batou.meow()





