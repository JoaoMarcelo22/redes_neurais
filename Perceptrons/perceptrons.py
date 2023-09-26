
w = 6
w2 = 2
baias= 0
limit = 5

print("""-------------------------------------------
Responda as Perguntas a seguir com S ou N, dado ao evento a seguir...
Haverá um evento familiar, e há um levantamento de requisitos para a sua ida,
responda as questões e observe o resultado.
-------------------------------------------""")
      
res = str.upper(input("Você conferiu a previsão do tempo, o tempo vai estar bom ? "))
x1 = w if res == "S" else 0

res = str.upper(input("Você esta namorando, o seu namorado(a) vai ir junto com você ? "))
x2 = w2 if res == "S" else 0

res = str.upper(input("Você não tem viculo, e há a necessidade de ir via transporte publico, o local do evento é proximo a linhas de transporte publicos ? "))
x3 = w2 if res == "S" else 0

if((x1 + x2 + x3)+ baias > limit):
    print("""
********************************
    Você deve ir ao evento
          
********************************""")
else: 
    print("""
********************************
    Você não deve ir ao evento
          
********************************""")