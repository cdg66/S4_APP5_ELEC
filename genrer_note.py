import numpy as np

def fct_generer_note(fondamentale):
    SOL_Facteur = 0.891
    MIbemol_Facteur = 0.707
    FA_Facteur = 0.794
    RE_Facteur = 0.667
    fondamentale_transformee = [SOL_Facteur*fondamentale,MIbemol_Facteur*fondamentale,FA_Facteur*fondamentale,RE_Facteur*fondamentale]
    return fondamentale_transformee
