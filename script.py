
#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import cryptocompare

while True :
        print("Que voulez-vous savoir ? \n")
        print(" \n")
        print("1) Valeur d'une crypto-monnaie \n")
        print("2) Liste des crypto-monnaies \n")
        print("3) Quitter \n")

        user_question = input('>>> ')

        if(user_question.startswith('1')):
                print('Quelle crypto-monnaie en Euro, voulez-vous? \n')
                user_value = input('>>> ')
                print(cryptocompare.get_price(user_value, curr='EUR'))

        elif(user_question.startswith('2')):
                for list_crypto in cryptocompare.get_coin_list(format=True):
                        print(list_crypto)

        elif(user_question.startswith('3')):
                print("A bientôt \n")
                exit()
        else:
                print("Répondez par '1', '2' ou '3' \n")