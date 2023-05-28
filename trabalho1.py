# UFSCar - Departamento de Computação
# Construção de compiladores
# Autor: Igor Teixeira Machado RA: 769708
# Autor: Júlia Aparecida de Sousa RA:
# Autor: Rafael Vinicius Polato Passador RA:

# pip install antlr4-python3-runtime


# Importação de bibliotecas
import sys

from antlr4 import *
from LA import LA

def saidaArquivo(nomeArquivo, tokens):
    arquivo = open(nomeArquivo, 'w')
    for token in tokens:
        arquivo.write(f'{token}\n')
    arquivo.close()

def main(arquivoEntrada, arquivoSaida):

    #arquivoEntrada = sys.argv[1]
    #arquivoSaida = sys.argv[2]
    '''
    symbolicNames = [ "<INVALID>",
            "'algoritmo'", "'declare'", "'literal'", "'escreva'", "'inteiro'", "'real'", "'leia'", 
            "'fim_algoritmo'", "'se'", "'entao'", "'fim_se'", "'senao'", "'fim_senao'", 
            "'enquanto'", "'para'", "'fim_para'", "'ate'", "'constante'", "'tipo'", 
            "'registro'", "'fim_registro'", "'procedimento'", "'fim_procedimento'", 
            "'var'", "'funcao'", "'fim_funcao'", "'retorne'", "NUM_INT", "NUM_REAL", 
            "IDENT", "CADEIA", "COMENTARIO", "WS", "'<'", "'>'", "'='", 
            "'<>'", "'<='", "'>='", "'+'", "'-'", "'*'", 
            "'/'", "'['", "']'", "':'", "'('", "')'", 
            "','", "'<-'" , "'.'", "CADEIA_NAO_FECHADA", "ERRO", 
            "COMENTARIO_NAO_FECHADO", "~", "}", "$" ]'''

    arquivo = FileStream(arquivoEntrada, encoding="utf-8")
    lexer = LA(arquivo)
    tokens = lexer.getAllTokens()
    saida = []
    literalNames = lexer.literalNames
    symbolicNames = lexer.symbolicNames

    for t in tokens:

        if t.type <= 63:
            if literalNames[t.type] == "'~'" or literalNames[t.type] == "'}'" or literalNames[t.type] == "'$'":
                saida.append(f'Linha {t.line}: {literalNames[t.type][1]} - simbolo nao identificado') # Arrumar aspas
                break

            saida.append(f'<\'{t.text}\',{literalNames[t.type]}>')
        else:
            if symbolicNames[t.type] == 'ERRO':
                saida.append(f'Erro na linha {t.line}: {t.text}')
                break
            elif symbolicNames[t.type] == 'COMENTARIO_NAO_FECHADO':
                saida.append(f'Linha {t.line}: comentario nao fechado')
                break
            
            elif symbolicNames[t.type] == 'CADEIA_NAO_FECHADA':
                saida.append(f'Linha {t.line}: cadeia literal nao fechada')
                break
            
            saida.append(f'<\'{t.text}\',{symbolicNames[t.type]}>')
        
    saidaArquivo(arquivoSaida, saida)

if __name__ == "__main__":
    main()