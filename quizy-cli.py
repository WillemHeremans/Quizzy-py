#!/usr/bin/python﻿
# coding: utf-8

import random

mot = random.choice(["information", "employeur", "fournisseur", "automatiquement", "navigation", "contenu", "fichier"])
tab_vide = []
tab_mot = []

for x in mot:
	tab_vide.append('_')
	tab_mot.append(x)

print('Mot à deviner : \n' + ' '.join(tab_vide))

point = 0

while tab_vide != tab_mot:
	resp = raw_input("\nDevinez une lettre du mot mystère: ")

	if (resp in tab_mot) and (resp not in tab_vide):
		point += 5
		indices = [i for i, x in enumerate(tab_mot) if x == resp]
		for indices in indices:
			tab_vide[indices] = tab_mot[indices]
		print("\nOUI! La lettre '" + resp + "' se trouve dans le mot! ++score = " + str(point) + " point(s)++ :\n")
		print(' '.join(tab_vide) + "\n")
	elif (resp in tab_mot) and (resp in tab_vide):
		point -= 1
		print("Lettre déjà complétée! **Pénalité -1 point** [score = " + str(point) + " point(s)] :\n")
	else:
		point -=5
		print("\nNON! pas de lettre '" + resp + "' dans ce mot! --score = " + str(point) + " point(s)--...\n")	
	
exit()
