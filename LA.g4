lexer grammar LA;

ALGORITMO     :	'algoritmo'
    ;
DECLARE       :	'declare'
    ;
LITERAL       :	'literal'
    ;
ESCREVA       :	'escreva'
    ;
INTEIRO       :	'inteiro'
    ;
REAL          : 'real'
    ;
LEIA          :	'leia'
    ;
FIM_ALGORITMO :	'fim_algoritmo'
    ;
SE            :	'se'
    ;
ENTAO         :	'entao'
    ;
FIM_SE        :	'fim_se'
    ;
SENAO         :	'senao'
    ;
FIM_SENAO     :	'fim_senao'
    ;
ENQUANTO      :	'enquanto'
    ;
FIM_ENQUANTO  :	'fim_enquanto'
    ;
PARA          :	'para'
    ;
FACA        :	'faca'
    ;
FIM_PARA      :	'fim_para'
    ;
ATE           :	'ate'
    ;
CONSTANTE     :	'constante'
    ;
TIPO          :	'tipo'
    ;
REGISTRO      :	'registro'
    ;
FIM_REGISTRO  :	'fim_registro'
    ;
PROCEDIMENTO  :	'procedimento'
    ;
FIM_PROCEDIMENTO :	'fim_procedimento'
    ;
VAR           :	'var'
    ;
FUNCAO        :	'funcao'
    ;
FIM_FUNCAO    :	'fim_funcao'
    ;
RETORNE       :	'retorne'
    ;
LOGICO        :	'logico'
    ;
CASO          :	'caso'
    ;
SEJA          :	'seja'
    ;
FIM_CASO      :	'fim_caso'
    ;
DOISPONTOS    :	'..'
    ;
E             :	'e'
    ;
OU            :	'ou'
    ;
NAO           :	'nao'
    ;
MENOR    :	'<'
    ;
MAIOR    :	'>'
    ;
IGUAL    :	'='
    ;
DIFERENTE:	'<>'
    ;
MENORIGUAL:	'<='
    ;
MAIORIGUAL:	'>='
    ;
MAIS    :   '+'
    ;
MENOS   :   '-'
    ;
MULT    :   '*'
    ;
DIV     :   '/'
    ;
ABRECOL :	'['
    ;
FECHACOL:	']'
    ;
DELIM	:	':'
	;
ABREPAR :	'('
	;
FECHAPAR:	')'
	;
VIRGULA	:	','
    ;
ATRIBUICAO : '<-'
    ;
PONTO   :   '.'
    ;
TIL     :   '~'
    ;
FECHA_CHAVE: '}'
    ;
SIFRAO  :   '$'
    ;
MODULO  :   '%'
    ;
PONTEIRO:   '^'
    ;
E_COMERCIAL: '&'
    ;
FALSO   :   'falso'
    ;
VERDADEIRO: 'verdadeiro'
    ;
NUM_INT	: ('0'..'9')+
	;
NUM_REAL	: ('0'..'9')+ ('.' ('0'..'9')+)?
	;
IDENT : ('a'..'z'|'A'..'Z')+ ('_' |'-')* ('a'..'z'|'A'..'Z'|'0'..'9')*
	 ;
CADEIA 	: '"' ( ESC_SEQ | ~('\n'|'"'|'\\') )* '"'
	;
fragment
ESC_SEQ	: '\\"';
COMENTARIO:   ('{' ~('\n'|'\r'|'}')* '}') -> skip
    ;
CADEIA_NAO_FECHADA: '"' (ESC_SEQ | ~('\n'|'"'|'\\'))* '\n'
    ;
COMENTARIO_NAO_FECHADO: ('{' (' '| '\t'| '\r'| '\n')*)
    ;
WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;