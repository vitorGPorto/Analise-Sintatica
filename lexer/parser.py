import sys
import copy

from tag import Tag
from token import Token
from lexer import Lexer

'''
[TODO-OPC-1]: 
tratar retorno 'None' do Lexer que esta sem Modo Panico
[TODO-OPC-2]: 
para deixar as mensagens de erro sintatico mais esclarecedoras,
a tabela preditiva poderia ser implementada.
'''

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        # Leitura inicial obrigatoria do primeiro simbolo
        self.token = lexer.proxToken()
        if self.token is None:  # erro no Lexer
            sys.exit(0)
    def sinalizaErroSintatico(self, message):
        print("[Erro Sintatico] na linha " + str(self.token.getLinha()) + " e coluna " + str(
            self.token.getColuna()) + ": ")
        print(message, "\n")
    # avanca o token
    def advance(self):
        print("[DEBUG] token: ", self.token.toString())
        self.token = self.lexer.proxToken()
        if self.token is None:  # erro no Lexer
            sys.exit(0)
    # verifica token esperado t
    def eat(self, t):
        if (self.token.getNome() == t):
            self.advance()
            return True
        else:
            return False
    # Programa -> CMD EOF
    def Programa(self):
        if (self.eat(Tag.KW_program)):
              if(not self.eat(Tag.Literal)):
                  self.sinalizaErroSintatico("Esperado \"Literal\", encontrado " + "\"" + self.token.getLexema() + "\"")
              self.Decl()
              self.Block()
              if (self.token.getNome() != Tag.EOF):
                  self.sinalizaErroSintatico("Esperado \"EOF\"; encontrado " + "\"" + self.token.getLexema() + "\"")


    def Decl(self):
        if(self.eat(Tag.SMB_dois_pontos)):
            if (not self.eat(Tag.ID)):
                self.sinalizaErroSintatico("Esperado \"ID\", encontrado " + "\"" + self.token.getLexema() + "\"")
            if (not self.eat(Tag.SMB_ponto_virgula)):
                self.sinalizaErroSintatico("Esperado \";\", encontrado " + "\"" + self.token.getLexema() + "\"")
            self.Decl()
    def Block(self):
        if(self.eat(Tag.KW_begin)):
            self.StatementList()
            if (not self.eat(Tag.KW_end)):
                self.sinalizaErroSintatico("Esperado \"end\", encontrado " + "\"" + self.token.getLexema() + "\"")

    def StatementList(self):
        self.Statement()
        self.StatementListLinha()
    def StatementListLinha(self):
        if (self.eat(Tag.SMB_ponto_virgula)):
            self.StatementList()
    def Statement(self):
        if (self.eat(Tag.KW_turn)):
            self.Term()
            if (not self.eat(Tag.KW_degrees)):
                self.sinalizaErroSintatico("Esperado \"degrees\", encontrado " + "\"" + self.token.getLexema() + "\"")
        elif(self.eat(Tag.KW_forward)):
            self.Term()
        elif (self.eat(Tag.KW_repeat)):
            self.Term()
            if (not self.eat(Tag.KW_do)):
                self.sinalizaErroSintatico("Esperado \"do\", encontrado " + "\"" + self.token.getLexema() + "\"")
            self.Block()
        elif (self.eat(Tag.KW_print)):
            if (not self.eat(Tag.Literal)):
                self.sinalizaErroSintatico("Esperado \"Literal\", encontrado " + "\"" + self.token.getLexema() + "\"")
        elif(self.eat(Tag.SMB_dois_pontos)):
            self.AssignmentStatement()
        elif (self.eat(Tag.KW_if)):
            self.IfStatement()
    def AssignmentStatement(self):
            if (not self.eat(Tag.ID)):
                self.sinalizaErroSintatico("Esperado \"ID\", encontrado " + "\"" + self.token.getLexema() + "\"")
            self.Expr()
    def IfStatement(self):
        if (self.eat(Tag.KW_if)):
            self.Expr()
            if (not self.eat(Tag.KW_do)):
                self.sinalizaErroSintatico("Esperado \"do\", encontrado " + "\"" + self.token.getLexema() + "\"")
            self.Block()
    def Expr(self):
        self.Expr1()
        self.ExprLinha()
    def ExprLinha(self):
        if (self.eat(Tag.OP_soma) or self.eat(Tag.OP_subtração)):
            self.Expr1()
            self.ExprLinha()
    def Expr1(self):
        self.Expr2()
        self.Expr1Linha()
    def Expr1Linha(self):
        if (self.eat(Tag.OP_multiplicação) or self.eat(Tag.OP_divisão)):
            self.Expr2()
            self.Expr1Linha()
    def Expr2(self):
        self.Term()
    def Term(self):
        if (self.eat(Tag.SMB_dois_pontos)):
            if (not self.eat(Tag.ID)):
                self.sinalizaErroSintatico("Esperado \"ID\", encontrado " + "\"" + self.token.getLexema() + "\"")
        elif (not self.eat(Tag.NUM)):
            self.sinalizaErroSintatico("Esperado \"NUM\", encontrado " + "\"" + self.token.getLexema() + "\"")



