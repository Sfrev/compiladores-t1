# Trabalho 01 - Construção de Compiladores

## Documentação Externa

### Integrantes do Grupo:

- Igor Teixeira Machado (RA: 769708)
- Júlia Aparecida Sousa de Oliveira (RA: 769707)
- Rafael Vinicius Polato Passador (RA: 790036)

### Introdução

Este relatório apresenta o trabalho desenvolvido pela equipe composta pelos integrantes acima mencionados, como atividade avaliativa da disciplina de Construção de Compiladores. O objetivo do trabalho foi a implementação de um analisador léxico para a Linguagem Algorítmica (LA), desenvolvida pelo Prof. Jander, no contexto do Departamento de Computação da UFSCar.

O analisador tem a finalidade de ler um programa-fonte em LA e gerar uma lista contendo os tokens identificados. Durante o processo, são ignorados espaços em branco e comentários. Em caso de erro léxico, o programa interrompe a execução, reportando o tipo de erro identificado, bem como o primeiro caractere ou símbolo onde ocorreu. Além disso, também são reportados erros de comentário não-fechado na mesma linha e cadeia não-fechada na mesma linha.
