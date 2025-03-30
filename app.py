# Função para calcular o saldo e determinar o nível
def calcular_nivel(vitorias, derrotas):
    # Calculando o saldo
    saldoVitorias = vitorias - derrotas
    
    # Determinando o nível com base nas vitórias usando match-case ao inves de elif
    match vitorias:
        case vitoria if vitoria < 10:
            nivel = "Ferro"
        case vitoria if 10 <= vitoria <= 20:
            nivel = "Bronze"
        case vitoria if 21 <= vitoria <= 50:
            nivel = "Prata"
        case vitoria if 51 <= vitoria <= 80:
            nivel = "Ouro"
        case vitoria if 81 <= vitoria <= 90:
            nivel = "Diamante"
        case vitoria if 91 <= vitoria <= 100:
            nivel = "Lendário"
        case vitoria if vitoria >= 101:
            nivel = "Imortal"
    
    return saldoVitorias, nivel

# Laço de repetição para pedir as entradas até que o usuário digite valores válidos
while True:
    try:
        # Recebendo o número de vitórias e derrotas
        vitorias = int(input("Digite o número de vitórias: "))
        derrotas = int(input("Digite o número de derrotas: "))
        
        # verifica se os valores são válidos
        if vitorias < 0 or derrotas < 0:
            print("Por favor, insira valores positivos para vitórias e derrotas.")
            continue
        
        # Chamando a função para calcular o saldo e o nível
        saldoVitorias, nivel = calcular_nivel(vitorias, derrotas)
        
        # Exibindo o resultado
        print(f"O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}")
        break
    
    except ValueError:
        print("Por favor, insira números válidos.")
