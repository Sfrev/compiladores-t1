# UFSCar - Departamento de Computação
# Construção de compiladores
# Analisador Léxico para a linguagem LA

# Autor: Igor Teixeira Machado RA: 769708
# Autor: Júlia Aparecida de Sousa RA: 769707
# Autor: Rafael Vinicius Polato Passador RA: 790036

# Para instalar o ANTLR4 no Windows, basta executar o comando abaixo no terminal
# pip install antlr4-python3-runtime

# Para executar o ANTLR4 no Windows, basta executar o comando abaixo no terminal
# java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 LA.g4

# Para executar o programa, basta executar o comando abaixo no terminal
# python trabalho1.py <arquivo_entrada> <arquivo_saida>

# Para executar o corretor, basta executar o comando abaixo no terminal
# java -jar <caminho_do_corretor> "<python <caminho_programa>>" gcc <pasta_saidas> <pasta_casos_de_teste> <RAs dos integrantes> t1"
# Exemplo:
# java -jar .\compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar 
# "python C:\Repositorio\Compiladores\compiladores-t1\trabalho1.py" 
# gcc C:\Repositorio\Compiladores\compiladores-t1\saidas C:\Repositorio\Compiladores\casos-de-teste RA t1"

# Importação de bibliotecas
import sys
from antlr4 import *
from LA import LA

# Função para escrever a saída em um arquivo
def saidaArquivo(nomeArquivo, saida):
    arquivo = open(nomeArquivo, 'w')
    for linha in saida:
        arquivo.write(f'{linha}\n')
    arquivo.close()

def main():

    # Lendo o caminho para o arquivo de entrada e de saída passados na linha de comando
    arquivoEntrada = sys.argv[1]
    arquivoSaida = sys.argv[2]

    # Lendo o arquivo de entrada
    arquivo = FileStream(arquivoEntrada, encoding="utf-8")

    # Criando o analisador léxico
    lexer = LA(arquivo)

    # Criando os tokens
    tokens = lexer.getAllTokens()

    # Lista para armazenar a saída
    saida = []

    # Dicionário para armazenar os nomes dos tokens
    literalNames = lexer.literalNames
    symbolicNames = lexer.symbolicNames

    for t in tokens:
        
        # Verificando se o token é um token literal
        if t.type <= 63:

            # Verificando se o token é um símbolo não identificado
            if literalNames[t.type] == "'~'" or literalNames[t.type] == "'}'" or literalNames[t.type] == "'$'":
                saida.append(f'Linha {t.line}: {literalNames[t.type][1]} - simbolo nao identificado')
                break
            
            saida.append(f'<\'{t.text}\',{literalNames[t.type]}>')

        else:

            # Se não foi possível verificar se o token pertence à linguagem
            if symbolicNames[t.type] == 'ERRO':
                saida.append(f'Erro na linha {t.line}: {t.text}')
                break

            # Verificando se o token é um comentário não fechado
            elif symbolicNames[t.type] == 'COMENTARIO_NAO_FECHADO':
                saida.append(f'Linha {t.line}: comentario nao fechado')
                break
            
            # Verificando se o token é uma cadeia literal não fechada
            elif symbolicNames[t.type] == 'CADEIA_NAO_FECHADA':
                saida.append(f'Linha {t.line}: cadeia literal nao fechada')
                break
            
            saida.append(f'<\'{t.text}\',{symbolicNames[t.type]}>')
    
    # Escrevendo a saída no arquivo
    saidaArquivo(arquivoSaida, saida)

if __name__ == "__main__":
    main()
