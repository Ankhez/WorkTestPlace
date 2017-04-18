from pyparsing import *


s = 'import matplotlib.pyplot as plt'
b = '01456'
module_digith = Word(srange("[0-4]"))
module_words = ZeroOrMore(Suppress(Word(alphas))) + (module_digith) + ZeroOrMore(Suppress(Word(alphas)))
full_sub = ZeroOrMore(module_words)
