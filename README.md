# Trabalho 01 - Construção de Compiladores

## Documentação Externa

### Integrantes do Grupo:

- Igor Teixeira Machado (RA: 769708)
- Júlia Aparecida Sousa de Oliveira (RA: 769707)
- Rafael Vinicius Polato Passador (RA: 790036)

### Introdução

Este relatório apresenta o trabalho desenvolvido pela equipe composta pelos integrantes acima mencionados, como atividade avaliativa da disciplina de Construção de Compiladores. O objetivo do trabalho foi a implementação de um analisador léxico para a Linguagem Algorítmica (LA), desenvolvida pelo Prof. Jander, no contexto do Departamento de Computação da UFSCar.

O analisador tem a finalidade de ler um programa-fonte em LA e gerar uma lista contendo os tokens identificados. Durante o processo, são ignorados espaços em branco e comentários. Em caso de erro léxico, o programa interrompe a execução, reportando o tipo de erro identificado, bem como o primeiro caractere ou símbolo onde ocorreu. Além disso, também são reportados erros de comentário não-fechado na mesma linha e cadeia não-fechada na mesma linha.

### Modo de Execução e Compilação

#### Instalação do ANTLR4 no Windows
Utilize o seguinte comando no terminal:
```
pip install antlr4-python3-runtime
```
#### Execução do ANTLR4 no Windows
Utilize o seguinte comando no terminal:
```
java -jar antlr-4.9.2-complete.jar -Dlanguage=Python3 LA.g4
```
#### Execução do Código do Trabalho
Utilize o seguinte comando no terminal:
```
python trabalho1.py <arquivo_entrada> <arquivo_saida>
```
#### Uso do Corretor
Para utilizar o corretor, siga as seguintes etapas:
1. Execute o seguinte comando no terminal para iniciar o corretor:
```
java -jar <caminho_do_corretor> "<python <caminho_programa>>" gcc <pasta_saidas> <pasta_casos_de_teste> <RAs dos integrantes> t1"
```
2. Certifique-se de substituir `<caminho_do_corretor>`, `<caminho_programa>`, `<pasta_saidas>`, `<pasta_casos_de_teste>` e `<RAs dos integrantes>` pelos respectivos valores específicos do seu ambiente de trabalho.

#### Exemplo 
```
java -jar .\compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar
```
```
"python C:\Repositorio\Compiladores\compiladores-t1\trabalho1.py"
```
```
gcc C:\Repositorio\Compiladores\compiladores-t1\saidas C:\Repositorio\Compiladores\casos-de-teste RA t1"
```

