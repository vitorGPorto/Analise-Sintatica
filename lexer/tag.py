from enum import Enum
class Tag(Enum):
    # Fim de arquivo
    EOF = -1
    # Palavras-chave
    KW_program = 1
    KW_begin = 2
    KW_end = 3
    KW_turn = 4
    KW_degrees = 5
    KW_forward = 6
    KW_repeat = 7
    KW_do = 8
    KW_print = 9
    KW_if = 10
    # Operadores
    OP_soma = 11
    OP_subtração = 12
    OP_multiplicação = 13
    OP_divisão = 14
    # Simbolos
    SMB_dois_pontos = 15
    SMB_ponto_virgula = 16
    SMB_dupla_aspas = 17
    SMB_abre_chaves = 18
    SMB_fecha_chaves = 19
    # Identificador
    ID = 20
    Literal = 21
    NUM = 22
