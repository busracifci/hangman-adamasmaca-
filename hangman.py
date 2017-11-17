import sys
import os
import random

# dosyadan kelime oku
file = open("wordlist.txt", "r")
sozluk = file.read().split()
file.close()

sozlukboyutu = len(sozluk)
kelime = sozluk[random.randint(0, sozlukboyutu)]

#kelime=['d','o','l','a','o']

uzunluk=len(kelime)
bil=[]
dizi=dict()

f = ['' for x in range(uzunluk)]

def displayword(characterlist):
    print("\n")
    for i in characterlist:
        if i == '':
            print "- ",
        else:
            print i,

def varyok(harf, sayac):
    if(harf in kelime):
        print("harf mevcut")
        characterpos=[pos for pos, char in enumerate (kelime) if char==harf]

        for x in characterpos:
            dizi[x] = harf
            f[x] = harf
        #print(f)
        displayword(f)
        print("\n")

        if(sorted(f)==sorted(kelime)):
            print("Tebrikler ")
            sys.exit()
        else:
            a=raw_input("\nYeni bir harf giriniz: ")
            varyok(a, sayac)
            print("\n")
    else:
        if(sayac==0):
            print("\n"+str(f)+"\n ____\n |  |\n O  |\n    |\n    |")
            sayac=sayac+1
            a=raw_input("Yeni bir harf giriniz:\n\n")
            varyok(a, sayac)
        if(sayac==1):
            print(f)
            print(" ____\n |  |\n O  |\n |  |\n    |")
            sayac=sayac+1
            a=raw_input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==2):
            print(f)
            print(" ____\n |  |\n O  |\n |  |\n |  |")
            sayac=sayac+1
            a=raw_input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==3):
            print(f)
            print(" ____\n |  |\n O  |\n/|  |\n |  |")
            sayac=sayac+1
            a=raw_input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==4):
            print(f)
            print(" ____\n |  |\n O  |\n/|\ |\n |  |")
            sayac=sayac+1
            a=raw_input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==5):
            print(f)
            print(" ____\n |  |\n O  |\n/|\ |\n/|  |")
            sayac=sayac+1
            a=raw_input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac==6):
            print(f)
            print(" ____\n |  |\n O  |\n/|\ |\n/|\ |")
            sayac=sayac+1
            a=raw_input("Yeni bir harf giriniz:\n")
            varyok(a, sayac)
        if(sayac>6):
            print(f)
            print(" ____\n |  |\n    |\n    |\nO//\|")
            print("Oyunu kaybettiniz")
            sys.exit()


print("Adam asmaca oyununa hosgeldiniz.");
print(kelime)
print(f);
harf=raw_input("\nBir harf giriniz: ")
varyok(harf, 0)

