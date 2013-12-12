"""
 koostada funktsioon, mis viib teksti kursori soovitud koordinaatidele
 x, y ja trukib sinna etteantud teksti
 print "033[y;xH"
 -VIIB KURSORI KOORDINAATIDELE x  ja y
 print "\033[2J"
 -ekraan tuhjaks
"""


def kursor():

    print "\033[6;5HHello"
    
print "\033[2J"

kursor ()    

"""
ulesanne , kasutades eelmises funktsioonis loodud kursori positsioneeri-
mise ja teksti valjastamise funktsiooni...
Loo uus funktsioon, mis valjastab ekraanile kasti servad. Funktsiooni
parameetrid x, y, w, h
"""

def kast (x, y, w, h):
	
	     kursor(x, y, "#")
	     kursor(x+w, y, "#")
	     
	     kursor(x, y+h, "#")
	     kursor(x+y, y+h, "#")
	     
kast(10,15,5,10)	    
	       
	


	
