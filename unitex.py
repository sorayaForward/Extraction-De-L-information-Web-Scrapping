import os
from os import path
#add UnitexToolLogger to your  environment variables in your machine Or ..
#Change Unitex_path variable to the location of "UnitexToolLogger" folder in your machine 
Unitex_path=".\\UnitexToolLogger" 
if path.exists("corpus-medical_snt"):
    os.system("rd /s corpus-medical_snt") 
os.mkdir("corpus-medical_snt")
os.system(f"{Unitex_path} Normalize corpus-medical.txt -r Norm.txt")
os.system(f"{Unitex_path} Tokenize corpus-medical.txt -a Alphabet.txt")# <--- fichier alphabet
os.system(f"{Unitex_path} Compress subst.dic -o subst.bin")
os.system(f"{Unitex_path} Dico -t corpus-medical.snt -a Alphabet.txt subst.bin") # <--- fichier alphabet
os.system(f"{Unitex_path} Grf2Fst2 posologie.grf")
os.system(f"{Unitex_path} Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all") # <--- fichier alphabet
os.system(f"{Unitex_path} Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")


# Le fichier d’alphabet est un fichier texte décrivant tous les caractères d’une langue,
# ainsi que les correspondances entre lettres minuscules et majuscules, 
# l'alphabet c'est l'unite atomique de tous les mots du langage alors sa présence est obligatoire pour qu’Unitex puisse fonctionner
# je l'ai utiliser pour generer les tokens
# pour generer les dictionnaires dlf, dlc, err ..
