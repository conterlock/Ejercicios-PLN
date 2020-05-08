import nltk
from nltk.book import *
text1.concordance("monstrous")  # Ocurrencia de una palabra dada en un texto
text1.similar("monstrous")      # Palabras asimiladas
text2.common_contexts(["monstrous", "very"])    # Contextos compartidos entre palabras
