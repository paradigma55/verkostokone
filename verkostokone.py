
# kysyy käyttäjän identiteetin

ego = input("Please enter your name: ")

# luo käyttäjän identiteetistä muuttujan jonka arvo on 0?
laheisia = ""

while laheisia != "K" and laheisia != "E":
	laheisia = input("Onko sinulla läheisiä? K/E: ")
	if laheisia == "E":
		print ("Harmin loista :(")
	elif laheisia == "K":
		print ("Okei! Sitten niiden muodostamaa verkostoa voidaan analysoida.")
	else:
		print ("Vastauksesi oli epäkorrekti. Yritä uudelleen.")

print ("Seuraavaksi voit mainita jokaisen läheisen nimen yksi kerrallaan.")

laheiset = []
siinakaikki = "K"

while siinakaikki == "K":
	nimi = input("Anna yhden läheisesi nimi: ")
	laheiset.append(nimi)
	siinakaikki = input("Onko muita? K/E: ")
	if siinakaikki != "K" and siinakaikki != "E":
		print ("Muista vastata vain joko K tai E")

print ("Käyttäjän " + ego + " läheisiä ovat:")
print (laheiset)

laheisyys = ""
laheisen_laheisyys = 0

for laheinen in laheiset:
	print ("case " + laheinen)
	laheisyys = input("Asteikolla 0-10, kuinka läheinen olet hänen kanssaan?")
	if laheisyys != 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
		print ("Osaatko lukea?")
		continue
	print (laheinen + " on sinulle läheinen arvolla " + laheisyys + ".")
 
# luo läheisen nimestä muuttujan (jonka arvo on 0?)

# kysyy käyttäjältä miten läheinen hän on tämän henkilön kanssa (asteikolla 0-10)
# kertoo tämän läheisyysarvon kahdella (koska omista ihmissuhteista tietää paljon paremmin kuin muiden, tätä voi myöhemmin muuttaa) 

# lisää läheiselle läheisyysarvon

# kysyy käyttäjältä, tunteeko läheinen muita aiemmin syötettyjä läheisiä (looppi)
# jos tuntee, kuinka läheisiä he ovat (asteikolla 0-10)

# muodostaa listan, jossa läheiset ovat järjestyksessä sen mukaan, kenen kanssa on läheisin