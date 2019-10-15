import random 
naipes = ('ouros','espadas','copas','paus')
numero_cartas = ('dois','tres','quatro','cinco','seis','sete','oito', 'nove', 'dez', 'valete', 'dama', 'rei', 'as1','as11')
valor_cartas = {'dois':2, 'tres':3, 'quatro':4, 'cinco':5, 'seis':6, 'sete':7, 'oito':8, 'nove':9, 'dez':10, 'valete':10, 'dama':10, 'rei':10, 'as1':1 , 'as11':11}

jogando = True
# classes para o deck e a carta o str serve para printar o naipe junto com o numero que neste caso esta como o numero_carta
class Carta: 
    def __init__(self, naipe, numero_carta):
        self.naipe = naipe
        self.numero_carta = numero_carta
    
    def __str__(self):
        return self.numero_carta + ' de ' + self.naipe
class Deck:
    def __init__(self):
        self.deck = []
        for naipe in naipes:
            for numero_carta in numero_cartas:
                self.deck.append(Carta(naipe,numero_carta))
    def __str__(self):
        deck_num = ''
        for carta in self.deck:
            deck_num += '/n' + carta.__str__()
        return 'O deck tem: ' + deck_num
    def misturar__str__(self):
        random.misturar(self.deck)
    def distribuir(self):
        uma_carta = self.deck.pop()
        return uma_carta
    
teste_deck = Deck()
print (teste_deck)  