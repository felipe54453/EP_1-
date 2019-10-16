import random 
dinheiro=100
print()
print("\n    Bem Vindo ao BlackJack!\n")
print("-"*30+"\n")
i=int(input('\033[1;32;40mquantos baralhos vc \033[1;33;40mquer usar?'))
print("-"*30+"\n")



soma=0
while dinheiro>0:
    lista=[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
    lista=lista*i
    print('seu dinheiro:',dinheiro)
    texto = input('qual a sua aposta?')
    if texto == "fim":
        break;
    aposta=int(texto)
    if aposta>dinheiro or aposta<0:
        ctz=input('voce tem ctz?')
        if ctz=='sim':
            break
        else:
            texto = input('qual a sua aposta?')
            if texto == "fim":
                break;
            aposta=int(texto)
            
    if aposta!=0:
        carta1=random.randint(0,51*i)
        carta2=random.randint(0,51*i)
        while carta1==carta2:
            carta2=random.randint(0,51*i)
       
        print('sua primeira carta é:',lista[carta1])
        print('sua segunda carta é:',lista[carta2])
        if lista[carta1]==lista[carta2]:
            split=input('quer splitar as suas cartas?')
            if split=='sim':
                soma=lista[carta1]
                while soma < 21:
                    mais_carta=input('quer mais uma carta para o primeiro bolo?')
                    if mais_carta=='sim':
                        carta7=random.randint(0,51*i)
                        print('sua carta do bolo é:',lista[carta7])
                        soma+=lista[carta7]
                        if lista[carta7]==1:
                            soma+=10
                            if soma > 21:
                                soma-=10
                        if lista[carta1]==1 and soma>21:
                            soma-=10
                            
                        print('voce esta com:',soma,'no primeiro bolo')
                    else:
                        break
                    
                    
                    
                    
                soma2=lista[carta2]
                while soma2 < 21:
                    mais_carta=input('quer mais uma carta para o segundo bolo?')
                    if mais_carta=='sim':
                        carta8=random.randint(0,51*i)
                        print('sua carta do bolo é:',lista[carta8])
                        soma2+=lista[carta8]
                        if lista[carta8]==1:
                            soma2+=10
                            if soma2 > 21:
                                soma2-=10
                        if lista[carta2]==1 and soma>21:
                            soma2-=10
                            
                        print('voce esta com:',soma2,'no segundo bolo')
                    else:
                        break
                
                carta9=random.randint(0,51*i)
                carta10=random.randint(0,51*i)
                print('as cartas da mesa sao:',lista[carta9],'e',lista[carta10])
                soma3=lista[carta9]+lista[carta10]
                if lista[carta9]==1 or lista[carta10]==1:
                            soma3+=10
                            if soma3 > 21:
                                soma3-=10
                print('primeiramente a banca esta com:',soma3)
                
                while soma3 < 17:
                    carta11=random.randint(0,51*i)
                    soma3+=lista[carta11]
                    if lista[carta11]==1:
                        soma3+=10
                        if soma3 > 21:
                            soma3-=10
                    if lista[carta9]==1 and soma3>21 or lista[carta10]==1 and soma3>21:
                                soma3-=10
                    print('a nova carta da banca é:',lista[carta11])
                    print('agora a banca esta com:',soma3)
                    
                      
                if soma > 21 and soma2 > 21:
                    dinheiro-=aposta
                    print()
                    print('voce passou do limite nos dois bolos')
                    print()
                    
                    
                    
                elif soma3>21:
                    dinheiro+=aposta
                    print()
                    print('a banca estorou?')
                    print()
                    
                elif soma >  soma3 and soma2 > soma3:
                    dinheiro+=aposta
                    print()
                    print('vc ganho da banca nos dois bolos')
                    print()
                    
                elif soma >  soma3 and soma2 < soma3:
                    dinheiro+=aposta
                    print()
                    print('vc ganho da banca no primeiro bolo')
                    print()
                    
                elif soma <  soma3 and soma2 > soma3:
                    dinheiro+=aposta
                    print()
                    print('vc ganho da banca no segundo bolos')
                    print()
                    
                elif soma < soma3 and soma2 <soma3:
                    dinheiro-=aposta
                    print()
                    print('vc perdeu nos dois bolos')
                    print()
                else:
                    print()
                    print('voce empatou com a banca')
                    print()
                    
            
                
        
                
        else:
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
                print('a banca estorou')
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
        if aposta>dinheiro:
            print()
            print('voce n tem tanta grana')
            break
        else:
            print()
            print('voce quebrou!')
            print()
            break