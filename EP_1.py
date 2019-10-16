import random 
dinheiro=100
i=int(input('quantos baralhos vc quer usar?'))
while dinheiro>0:
    lista=[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
    lista=lista*i
    print('seu dinheiro:',dinheiro)
    aposta=int(input('qual a sua aposta?'))
    if aposta!=0 or aposta<=dinheiro or aposta!='fim':
        carta1=random.randint(0,51*i)
        carta2=random.randint(0,51*i)
        while carta1==carta2:
            carta2=random.randint(0,51*i)
       
        print('sua primeira carta é:',lista[carta1])
        print('sua segunda carta é:',lista[carta2])
        soma=lista[carta1]+lista[carta2]
        
            
        if lista[carta1]==1 or lista[carta2]==1:
            soma+=10
            if soma > 21:
                soma-=10
        print('a soma é:',soma)
            
        
        
        while soma < 21:
            mais_carta=input('quer mais uma carta?')
            if mais_carta=='sim':
                carta3=random.randint(0,51*i)
                print('sua terceira carta é:',lista[carta3])
                soma+=lista[carta3]
                if lista[carta3]==1:
                    soma+=10
                    if soma > 21:
                        soma-=10
                if lista[carta1]==1 and soma>21 or lista[carta2]==1 and soma>21:
                        soma-=10
                print('voce esta com:',soma)
            else:
                break
        
            
            
        carta4=random.randint(0,51*i)
        carta5=random.randint(0,51*i)
        print('as cartas da mesa sao:',lista[carta4],'e',lista[carta5])
        soma2=lista[carta4]+lista[carta5]
        if lista[carta4]==1 or lista[carta5]==1:
                    soma2+=10
                    if soma2 > 21:
                        soma2-=10
        print('primeiramente a banca esta com:',soma2)
        
        while soma2 < 17:
            carta6=random.randint(0,51*i)
            soma2+=lista[carta6]
            if lista[carta6]==1:
                soma2+=10
                if soma2 > 21:
                    soma2-=10
            if lista[carta4]==1 and soma2>21 or lista[carta5]==1 and soma2>21:
                        soma2-=10
            print('a nova carta da banca é:',lista[carta6])
            print('agora a banca esta com:',soma2)
        
            
            
        if lista[carta1] == 1 and lista[carta2]==10 or lista[carta1]==10 and lista[carta2]==1:
            print()
            print('vc tem um blackjack!')
            print()
            dinheiro+=1.5*aposta
            
            
        elif soma > 21:
            dinheiro-=aposta
            print()
            print('voce passou do limite')
            print()
            
            
        elif soma2>21:
            dinheiro+=aposta
            print()
            print('a banca estorou?')
            print()
            
            
            
        elif soma >  soma2:
            dinheiro+=aposta
            print()
            print('vc ganho da banca')
            print()
            
        elif soma < soma2:
            dinheiro-=aposta
            print()
            print('vc perdeu da banca')
            print()
        else:
            print()
            print('voce empatou com a banca')
            print()
    else:
        print()
        print('voce quebrou!')
        print()
        break
            
            
        