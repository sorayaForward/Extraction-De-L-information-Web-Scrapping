import re,sys
# -------extraction des medicaments du corpus + les ajouter dans les subst.dic(supp doub+ordre alpha) et subst-corpus.dic---------------------------------
if not(len(sys.argv)==2):
	print("Veuillez saisir le nom du corpus svp")
else:
	if not(sys.argv[1]=="corpus-medical.txt"):
		print("Veillez saisir le nom du fichier corpus-medical.txt")
	else:			
		with open('corpus-medical.txt','r+',encoding='utf-8') as c:
			with open('subst.dic','a',encoding='utf-16-le') as f1:
				with open('subst_corpus.dic','w+',encoding='utf-16-le') as f2:
					cpt = 1
					print("Affichage des medicaments trouvee dans le corpus :")	
					for i in c.readlines():
						x = re.findall("^-? ?(\w+) :? ?(\d+|,)+ (mg|ml|µg|µl|gr|g|l|½|¼|mg/m²|g/m²|(\d+)/j|fois).+",i,re.I)#regex to extract medics
						for j in x:          
							f1.write(j[0].lower()+",.N+subst\n")
							print(str(cpt)+" : "+j[0].lower())
							f2.write(j[0].lower()+",.N+subst\n")
							cpt = cpt+1
		# Suppression des doublants dans subst.dic
		with open('subst.dic','r',encoding='utf-16-le') as f1:
			x = f1.readlines()
			x = list(set(x))# to delete duplicate values we use set
			with open('subst.dic','w',encoding='utf-16-le') as f2:# ouvrir un fichier avec w supprime sans contenu meme avant d'ecrire
				# trie de subst.dic
				for i in sorted(x,key=lambda s: s.lower()):
					f2.write(i)	
		print("Enrichissement avec succes !")
		
		
		
#------------remplir info2 avec les info sur les substances extrait de corpus medical--------------------------
		medicaments = []
		total = 0
		alpha = ['a','b','c','d','e','é','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		with open('info2.txt','w',encoding='utf-16-le') as f1:
			with open('subst_corpus.dic','r',encoding='utf-16-le') as f2:
				a = f2.readlines()# if we want to do another readline we have to open the fie again (1st readline give us the contect 2nd readline give us an empty array)
				a = list(set(a))
				for alph in alpha:
					for med in a:
						x = re.search('\A'+alph, med)
						if x:
							medicaments.append(med)
					f1.write('\n--------------------------------------------------------\n')
					f1.write('Totale de substances de la lettre '+str(alph)+': '+str(len(medicaments)))
					f1.write('\n--------------------------------------------------------\n')
					for i in medicaments:
						f1.write(i)
					total = len(medicaments) + total
					medicaments = []
				f1.write('Nombre totale des substances active : '+str(total))
			print('Fichier info2.txt cree')



#------------------remplir info3 avec les info sur les substances effectivement ajouter------------------------
		medicaments = []
		with open('subst.dic','r',encoding='utf-16-le') as f2:
			b = f2.readlines()
			with open('subst_avant_enrich.dic','r',encoding='utf-16-le') as f1:
				yy = f1.readlines()	
				medicaments = set(b) - set(yy)# med reelement ajoutee = subst de fin - subst de debut
		n = 0
		total = 0
		med = []
		with open('info3.txt','w',encoding='utf-16-le') as f1:
			for alph in alpha:
				for m in medicaments:
					x = re.search('\A'+alph, m)
					if x:
						med.append(m)
						n = n+1
				f1.write('\n--------------------------------------------------------\n')
				f1.write('Totale de substances de la lettre '+str(alph)+': '+str(n))
				f1.write('\n--------------------------------------------------------\n')
				for i in med:
						f1.write(i)
				med = []
				n = 0
			f1.write('Nombre totale des substances active : '+str(len(medicaments)))
			print('Fichier info3.txt cree')

				

 
