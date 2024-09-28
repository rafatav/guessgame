import random
from art import logo
print(logo)

difficulty_setting = {
  "facil": 10,
  "dificil": 5
}

print("Bem vindo ao Jogo de Adivinhação de Número!")
print("Estou pensando em um número entre 1 a 100.")

# Programa precisa selecionar um número aleatório de 1 a 100
number = random.choice(range(1, 100))
# Usuário precisa escolher entre dois níveis de dificultade, fácil ou difícil
difficulty = input('Escolha um nível de dificuldade. Digite "facil" ou "dificil": ').lower()
# Baseado no nível de dificuldade escolhido, o usuário terá um número limitado de chances, 10 ou 5
attempts = difficulty_setting[difficulty]
game_over = False
while attempts > 0 and game_over == False:
  print(f"Você tem {attempts} tentativas restantes para adivinhar o número.")
  # Usuário precisa escolher um número de 1 a 100
  guess = int(input("Tente adivinhar o número: "))
  # Programa precisa verificar se o número é igual ao nr aleatório, nesse caso o usuário ganha e a partida acaba, ou se é maior ou menor, no caso o jogador precisa escolher um novo número dentro da quantidade de tentativas restantes
  if guess == number:
    print(f"Você acertou! A reposta era {number}.")
    game_over = True
  elif guess > number:
    attempts -= 1
    if attempts == 0:
      print("Muito alto.\nVocê não tem mais tentativas, você perdeu.")
    else:
      print("Muito alto.\nTente novamente.")
  elif guess < number:
    attempts -= 1
    if attempts == 0:
      print("Muito baixo.\nVocê não tem mais tentativas, você perdeu.")
    else:
      print("Muito baixo.\nTente novamente.")
# Se o numero de tentativas acabar, a partida termina e o usuário perdeu