#gramática generativa
# !pip install lark-parser --user
# !pip install hypothesis --user

from lark import Lark
from hypothesis.extra import lark

grammar = Lark ("""
start : PLANETA S "em" S SIGNO S "indica" S evento "."

evento : "que você terá" S PROBLEMA S ALVO | "uma boa fase" S ALVO
PLANETA : "Mercúrio" | "Vênus"
SIGNO : "Capricórnio" | "Peixes"
PROBLEMA : "problemas" | "decepções"
ALVO : "no amor" | "no trabalho" | "na vida financeira" | "na universidade"
S : " "
""")

frase = "Mercúrio em Peixes indica que você terá problemas na universidade."

tree=grammar.parse(frase)

print(tree.pretty)

gen = lark.from_lark(grammar)
for i in range(10):
    print(gen.example())
