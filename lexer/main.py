"Nome: Vitor Gabriel Santos Porto"
"RA:119125926"
from tag import Tag
from token import Token
from lexer import Lexer
from parser import Parser

if __name__ == "__main__":
   lexer = Lexer('exemplo.txt')
   parser = Parser(lexer)
   parser.Programa()
   parser.lexer.closeFile()
   '''
   print("\n=>Lista de tokens:")
   token = lexer.proxToken()
   while(token is not None and token.getNome() != Tag.EOF):
      print(token.toString(), "Linha: " + str(token.getLinha()) + " Coluna: " + str(token.getColuna()))
      token = lexer.proxToken()
   '''

   print("\n=>Tabela de simbolos:")
   lexer.printTS()
   lexer.closeFile()
    
   print('\n=> Fim da compilacao')
