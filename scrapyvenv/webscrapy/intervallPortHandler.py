import re
import sys
#1722

def display(medicaments):
        inf = sys.argv[1].split("_")[0].lower()
        sup = sys.argv[1].split("_")[1].lower()
        if(inf>sup):# traiter le cas d'err par ex : Z-A
            inter = inf
            inf = sup
            sup = inter
        for med in medicaments:
                x = re.search('\A['+inf+'-'+sup+']', med)#starts with inf or sup
                if x:
                    print(med) 
# generer info1
def info1Generator(medicaments):
    n = 0
    total = 0
    alpha = ['a','b','c','d','e','é','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    with open('info1.txt','w',encoding='utf-16-le') as f:
        for alph in alpha:
            for med in medicaments:
                x = re.search('\A'+alph, med)#starts with alph
                if x:
                    n = n+1
            f.write('Totale de substances de la lettre '+str(alph)+': '+str(n)+'\n')
            total = n + total
            n = 0
        f.write('Nombre totale des substances active : '+str(total)+'\n')


            

    