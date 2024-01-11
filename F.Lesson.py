from random import *

#-----------------------------------------------------:

#1 ÜL
#try:
    #print("Tere Maailm!")
    #nimi=input("Mis on sinu nimi?")
    #vanus=int(input("Kui vana sa oled")) 
    #print("Tere tulemast!"+ " "+ nimi + ". Sa oled"+str(vanus)+"aastat vana")
    #print("Tere tulemast!", nimi, ". Sa oled",vanus,"aastat vana")
    #print("Tere tulemast! {0} Sa oled {1} aastat vana".format(nimi, vanus)) 
    #print("Muutuja vanus=",vanus,"tüüp on",type(vanus))
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:

#-----------------------------------------------------:

#2 ÜL 
#try:
    #vanus = 18
    #eesnimi = "Jaak"
    #pikkus = 16.5
    #kas_käib_koolis = True

    #print("Muutuja vanus=",type(vanus))
    #print("Muutuja eesnimi=",type(eesnimi))
    #print("Muutuja pikkus=",type(pikkus))
    #print("Muutuja kas_käib_koolis=",type(kas_käib_koolis))
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:

#-----------------------------------------------------:

#3 ÜL

#1v (with random)

#from random import *
#try:
    #kokku=randint(10,100)
    #print("Kokku: ",kokku)
    #mitu=int(input("Mitu kommi tahav võtta?"))
    #kokku-=mitu
    #print("Nüüd laua peal on",kokku,"kommid")
#except:
#   print("Viga andmetüübiga")

#2v (without random)
#try:
    #kommid = 500
    #print(kommid)
    #mitu_kommid_võtta = int(input("Mitu kommi sa tahad ära võtta?"))
    #kommid =- mitu_kommid_võtta
    #print(kommid)
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:
 
#-----------------------------------------------------:

#4 ÜL
#try:
    #puu_ümbermõõt = int(input("Milline on puu ümbermõõt?"))
    #print("puu läbimõõt on võrdne", 2 * puu_ümbermõõt)
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:

#-----------------------------------------------------:

#5 ÜL
#try:
    #n = int(input("kui palju n?"))
    #m = int(input("kui palju m?"))
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:

#-----------------------------------------------------:

#5 ÜL
#try:
    #N = float(input("Sisestage ristküliku pikkus N meetrites: "))
    #M = float(input("Sisestage ristküliku laius M meetrites: "))
    #diagonaali_pikkus = (N ** 2 + M ** 2) ** 0.5
    #print("Ristküliku diagonaali pikkus on:", diagonaali_pikkus , "meetrit")
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:

#-----------------------------------------------------:

#6 ül
#   1v

# teepikkus = int(input("sisestage tee pikkus: "))
# aeg = int(input("sisestage aeg: "))
# kiirus = teepikkus / aeg

#   2v

#try:
#    aeg = float(input("Mit tundi kulus süiduks? "))
#    teepikkus = float(input("Mitu kilomeetrit sõtsid"))
#    kiirus = teepikkus / aeg
#    print("Sinu kiirus oli " + str(kiirus) + " km/h")
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:

#-----------------------------------------------------:

#7 ÜL
#   1v

#try:
    #for i in range(5):        
        #numbrit = int(input("Sisestage numbrit: "))
        #sum =+ numbrit
#except:
#   print("Viga andmetüübiga")
#finally:
#   print("Keskmine on:", sum / 5)

#   2v

#try:
    #numbrit1 = int(input("Sisestage numbrit: "))
    #numbrit2 = int(input("Sisestage numbrit: "))
    #numbrit3 = int(input("Sisestage numbrit: "))
    #numbrit4 = int(input("Sisestage numbrit: "))
    #numbrit5 = int(input("Sisestage numbrit: "))

    #sum = numbrit1 + numbrit2 + numbrit3 + numbrit4 + numbrit5 + 
#except:
#   print("Viga andmetüübiga")
#finally:
#   print("Keskmine on:", sum / 5)

#-----------------------------------------------------:

#-----------------------------------------------------:

#8 ÜL
#try:
    #print('    @..@\n   (----)\n  ( \__/ )\n  ^^ "" ^^')
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:

#-----------------------------------------------------:

#9 ÜL

#try:
    #a = float(input("Sisestage numbrit: "))
    #b = float(input("Sisestage numbrit: "))
    #c = float(input("Sisestage numbrit: "))
    #P = a + b + c
    #print(P)
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:

#-----------------------------------------------------:

#10 ÜL
#   1v

#try:
    #hinnang = 12.90
    #jootraha_protsent = 10
    #kokku = hinnang + (hinnang * (jootraha_protsent / 100))
    #igaüks_makseb = kokku / 2
    #print("Igaüks peab maksma:", igaüks_makseb, "eurot")
#except:
#   print("Viga andmetüübiga")

#   2v

#try:
    #P = randint(1, 5)
    #hind = 12.90
    #hind *= 1.1 #hind koos jatatega
    #osa = round(hind / P, 2)
    #print("Iga sõber maksab:", osa)
#except:
#   print("Viga andmetüübiga")

#-----------------------------------------------------:
