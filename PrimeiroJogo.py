print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
  print("Tentativa {} de {}".format(rodada, total_de_tentativas))
  chute_str = input("Digite o seu número: ")
  print("Você digitou: ", chute_str)
  chute = int(chute_str)

  acertou = numero_secreto == chute
  chutemaior = chute > numero_secreto
  chutemenor = chute < numero_secreto

  if(acertou):
    print("Você acertou!")
  else:
   if(chutemaior):
     print("Você errou! O seu chute foi maior do que o número secreto.")
   elif(chutemenor):
       rodada = rodada + 1
   print("Você errou! Seu chute foi menor que o número secreto.")




