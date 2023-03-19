from Lobo import Lobo
from Goblin import Goblin
from Personagem import Personagem

goblin = Goblin(vida=100, ataque=15, tipo="Pequeno", inteligencia=50)
lobo = Lobo(vida=0, ataque=50, forca=10, tipo="Grande") #lobo com vida 0 para testar logica de ataque
personagem = Personagem(vida=100, nome="Mateus", ataque=10)

goblin.atacar(lobo) # Goblin ataca lobo | lobo não pode ser atacado pois
#sua vida já está zerada (morto)
lobo.ver_vida() #verificando vida do lobo

print("-------------------")

personagem.atacar(goblin) #personagem (Mateus) atacando goblin