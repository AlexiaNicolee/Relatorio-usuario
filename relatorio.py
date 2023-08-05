#Dev: Alexia Nicole 

def bytes_para_megabytes(bytes):
    # Função que converte o tamanho em bytes para megabytes
    return bytes / (1024.0 * 1024.0)

def calcula_o_percentual(used_space, total_space):
    # Função que calcula o percentual de espaço usado em relação ao espaço total
    return (used_space / total_space) * 100

def dados():
    # Lista para armazenar os usuários e seus tamanhos em disco
    usuarios = []
    # Variável para acompanhar o espaço total ocupado
    total_space = 0

    # Lendo os dados do arquivo "usuarios.txt"
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            # Dividindo a linha em nome do usuário e espaço ocupado
            nome, espaco = linha.split()
            # Adicionando à lista de usuários
            usuarios.append((nome, int(espaco)))
            # Somando ao espaço total ocupado
            total_space += int(espaco)

    # Ordenando os usuários por espaço ocupado (maior para menor)
    usuarios.sort(key=lambda x: x[1], reverse=True)

    # Calculando o espaço total ocupado em megabytes
    total_ocupado = bytes_para_megabytes(total_space)

    # Calculando o espaço médio ocupado em megabytes
    if usuarios:
        media_space_mb = total_ocupado / len(usuarios)
    else:
        media_space_mb = 0

    # Gerando o relatório com codificação utf-8
    with open("relatório.txt", "w", encoding="utf-8") as relatorio:
        # Escrevendo cabeçalho e separadores
        relatorio.write("ACME Inc.   Uso do espaço em disco pelos usuários\n")
        relatorio.write("--------------------------------------------------------------\n")
        relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")

        # Escrevendo os dados dos usuários
        for i, (nome, espaco) in enumerate(usuarios, 1):
            espaco_mb = bytes_para_megabytes(espaco)
            percentual = calcula_o_percentual(espaco_mb, total_ocupado)

            relatorio.write(f"{i:<4} {nome:<15} {espaco_mb:>10.2f} MB {percentual:>10.2f}%\n")

        # Escrevendo o espaço total e a média
        relatorio.write(f"\nEspaço total ocupado: {total_ocupado:.2f} MB\n")
        relatorio.write(f"Espaço médio ocupado: {media_space_mb:.2f} MB\n")

if __name__ == "__main__":
    dados()