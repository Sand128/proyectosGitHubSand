import numpy as np
listaproductos=list()
listapresios=list()

def guardar(pd,pc):
    listaproductos.append(pd)
    listapresios.append(pc)
    return          

def jabones():
    tipo=int(input("1.-Barra o 2.-Polvo deterjente: "))
    if tipo==1:
        print ("\t1.-Barra Zote\n\t2.-Barra 123\n\t3.-Barra Ace")
        op = int(input("Elige una opción de compra: "))
        while 4 > op or op > 0 : 
            if op == 1 :
                opc=int(input("\t1.-Zote Grande $30\n\t2.-Zote Chico$20: "))
                if  opc<3: 
                    if opc==1 :
                        nom="zoteG"
                        pre=30
                        break
                    else:
                        nom="zoteCh"
                        pre=20
                        break      
            elif op == 2 : 
                opc=int(input("\t1.-123 Grande $35\n\t2.-123 Chico $20: "))
                if  opc<3: 
                    if opc==1 :
                        nom="123G"
                        pre=35
                        break
                    else:
                        nom="123Ch"
                        pre=20
                        break
                break     
            elif op == 3 :
                    opc=int(input("\t1.-Ace Grande $35\n\t2.-Ace Chico$23: "))
                    if  opc<3: 
                        if opc==1 :
                            nom="AceG"
                            pre=35
                            break
                        else:
                            nom="AceCh"
                            pre=23
                            break
                    break        
    elif tipo==2:
        print("1.-Polvo Ace\n2.-Salvo\n3.-Ariel\n4.-Roma")
        op = int(input("Elige una opción de compra: "))
        while 5 > op or op > 0 : 
            if op == 1 :
                opc=int(input("\tPolvo Ace\n\t1.-1 Kl $40\n\t2.- 1/2 kg $25\n\t3.-1/4 $15: "))
                if  opc<5:
                    if opc==1:
                        nom="Ace 1 kl"
                        pre=40
                        break
                    elif opc==2:
                        nom="Ace 1/2 kl"
                        pre=25
                        break
                    elif opc==3:
                        nom="Ace 1/4 1kl"
                        pre=15
                        break
                    break 
            elif op==2:
                opc=int(input("\tPolvo Salvo\n\t1.-1 Kl $40\n\t2.- 1/2 $25\n\t3.-1/4 $15: "))
                if  opc<4:
                    if opc==1:
                        nom="Salvo 1 kl"
                        pre=40
                        break
                    elif opc==2:
                        nom="salvo 1/2 kl"
                        pre=25
                        break
                    elif opc==3:
                        nom="salvo 1/4 1kl"
                        pre=15
                        break 
                    break          
            elif op==3:
                opc=int(input("\tPolvo Ariel\n\t1.-1 Kl $40\n\t2.- 1/2 $25\n\t3.-1/4 $15: "))
                if  opc<4:
                    if opc==1:
                        nom="Ariel 1 kl"
                        pre=40
                        break
                    elif opc==2:
                        nom="Ariel 1/2 kl"
                        pre=25
                        break
                    elif opc==3:
                        nom="Ariel 1/4 1kl"
                        pre=15
                        break
                    break   
            elif op==4:
                opc=int(input("\tPolvo Roma\n\t1.-1 Kl $35\n\t2.-1/2 $23\n\t3.-1/4 $14: "))
                if  opc<4:
                    if opc==1:
                        nom="Roma 1 kl"
                        pre=35
                        break
                    elif opc==2:
                        nom="Roma 1/2 kl"
                        pre=23
                        break
                    elif opc==3:
                        nom="Roma 1/4 1kl"
                        pre=14
                        break 
                break
    guardar(nom,pre)

    return 

def lacteos():
    tipo=int(input("1.-Yogurt o 2.-Leche: "))
    if tipo==1:
        print("\t1.-Yogurt Lala\n\t2.-Yogurt Alpura \n\t3.-Yogurt Yoplait")
        op = int(input("Elige una opción de compra: "))
        while 4 > op or op > 0 : 
            if op == 1 :
                opc=int(input("\t1.-lala 1 kl $50\n\t2.-lala 350 gr $10: "))
                if  opc<3: 
                    if opc==1:
                        nom="Lala 1kt"
                        pre=50
                        break
                    else:
                        nom="Lala 350gr"
                        pre=10                        
                        break
                break
            elif op==2:
                opc=int(input("\t1.-Alpura 1 kl $50\n\t2.-Alpura 350 gr $10: "))
                if  opc<3: 
                    if opc==1:
                        nom="Alpura 1kt"
                        pre=50
                        break
                    else:
                        nom="Alpura 350gr"
                        pre=10
                        break
                break
            elif op==3:
                opc=int(input("\t1.-Yoplait 1 kl $50\n\t2.-Yoplait 350 gr $10: "))
                if  opc<3: 
                    if opc==1:
                        nom="Yoplait 1kt"
                        pre=50
                        break
                    else:
                        nom="Yoplait 350gr"
                        pre=10
                        break        
                break
    elif tipo==2:
        print("1.-Leche Alpura, 2.-Leche Lala o 3.-Leche Santa Clara")
        op = int(input("Elige una opción de compra: "))
        while 4 > op and op > 0 : 
            if op == 1 :
                opc=int(input("\t1.-Alpura 3 kl $90\n\t2.-Alpura 1.5 kl $5050\n\t3.-Alpura 1 lt $27: "))
                if  opc<3: 
                    if opc==1:
                        nom="Alpura 1kt"
                        pre=50
                        break
                    elif opc==2:
                        nom="Alpura 1.5 lt"
                        pre=50
                        break
                    else:
                        nom="Alpura 1 lt"
                        pre=28
                        break
                break
            elif op==2:
                opc=int(input("\t1.-Leche Lala 3lt $90\n\t2.-Leche Lala 1.5 lt $50\n\t3.-Leche Lala 1lt $27: "))
                if  opc<3: 
                    if opc==1:
                        nom="Lala 3lt"
                        pre=90
                        break
                    elif opc==2:
                        nom="Lala 1.5 lt"
                        pre=50
                        break
                    else:
                        nom="Lala 1 lt"
                        pre=27
                        break
                break
            elif op==3:
                opc=int(input("\tSanta Clara\n\t1.-3 lt $100\n\t2.-1.5 lt $60\n\t3.-1 lt $30: "))
                if  opc<3: 
                    if opc==1:
                        nom="Santa Clara 3lt"
                        pre=100
                        break
                    elif opc==2:
                        nom="Santa Clara 1.5lt"
                        pre=60
                        break
                    else:
                        nom="Santa Clara 1lt"
                        pre=30
                        break        
                break
    guardar(nom,pre)
    return 

def botanas():
    tipo=int(input("1.- Chetos, 2.-Sabritas o 3.-Takis: "))
    while 4> tipo or tipo>0:
        if tipo ==1:
            opc=int(input("\t1.-Chetos Grande $40\n\t2.-Chetos Medianas $25\n\t3.-Chetos Chicas $13: "))
            if opc==1:
                nom="Chetos G"
                pre=40
                break
            elif opc==2:
                nom="Chetos M"
                pre=25
                break
            elif opc==3:
                nom="Chetos Ch"
                pre=13
                break  
            break          
        elif tipo==2:
            opc=int(input("\tSabritas Grande $80\n\t2.-Sabritas Medianas $40\n\t3.-Sabritas Chicas $12: "))
            if opc==1:
                nom="Sabritas G"
                pre=80
                break
            elif opc==2:
                nom="Sabritas M"
                pre=40
                break
            elif opc==3:
                nom="Sabritas ch"
                pre=12
                break
            break
        elif tipo==3:    
            opc=int(input("\t1.-Takis Grande $50\n\t2.-Takis Medianas $29\n\t3.-Takis Chicas $15: "))
            if opc==1:
                nom="Takis G"
                pre=50
                break
            elif opc==2:
                nom="Takis M"
                pre=29
                break
            elif opc==3:
                nom="Takis Ch"
                pre=15
                break
            break
    guardar(nom,pre)
    return 

def refrescos():
    tipo=int(input("1.- Coca-cola, 2.-Munded o 3.-Pepsi: "))
    while 4> tipo and tipo>0:
        if tipo ==1:
            opc=int(input("\t1.-Coca-cola 3lt $45\n\t2.-Coca-cola 2lt $37\n\t3.-Coca-cola 1lt $28: "))
            if opc==1:
                nom="Coca-cola 3lt"
                pre=45
                break
            elif opc==2:
                nom="Coca-cola 2lt"
                pre=37
                break
            elif opc==3:
                nom="Coca-cola 1lt"
                pre=28
                break  
            break          
        elif tipo==2:
            opc=int(input("\t1.-Munded 3lt $38\n\t2.-Munded 2 lt $28\n\t3.-Munded 1 lt $25: "))
            if opc==1:
                nom="Munded 3 lt"
                pre=38
                break
            elif opc==2:
                nom="Munded 2 lt"
                pre=28
                break
            elif opc==3:
                nom="Munded 1 lt "
                pre=25
                break
            break
        elif tipo==3:    
            opc=int(input("\t1.-Pepsi 3 lt $40\n\t2.-Pepsi 2 lt $28\n\t3.-Pepsi 1 lt $20: "))
            if opc==1:
                nom="Pepsi 3lt"
                pre=40
                break
            elif opc==2:
                nom="Pepsi 2lt"
                pre=28
                break
            elif opc==3:
                nom="Pepsi 1lt"
                pre=20
                break
        break
    guardar(nom,pre)
    return 

def imprimir():
    print("\t\tTIKET")
    fila = len(listapresios)
    col = len(listaproductos)
    print(listaproductos[nom],"-",listapresios[pre])
            
    total=int(sum(listapresios))
    print(np.array(m))
    print("\tTotal a pagar:$",total)
    
print("Iniciar compra")
opc=True
while(opc==True):
    print("Bienbenido a la tienda de abarrotes UMB")
    print("Menu: \n1.-Jabones\n2.-Lacteos\n3.-Botanas\n4.-Refrescos\n5.-Salir")
    op=int(input("Elige una opción de compra: "))
    if op==1:
        jabones()
    elif op==2:
        lacteos()
    elif op==3:
        botanas()
    elif op==4:
        refrescos()
    else:
        print("\n\n........................................")
        imprimir()
        print("........................................\n\tGracias por su compra")
        opc=False


