import sys
import getpass
def kareklis():
	print("Gatavs pakārties!?")
	print("Spēles Noteikumi:")
	print("Tev ir jāuzmin otrā spēlētāja ievadītais vārds.Tev ir dotas 6 minējumu reizes, jeb dzīvības. Ja dzīvības tiek iztērētas, tas nozīmē, tu esi pakārts! Vārds ir obligāti jāmin, pa vienam burtam, pilnu ierakstītu vārdu neieskaitīs, kā pareizo atbildi!")
	vards=getpass.getpass("1.Speletajs ievada savu vardu: ").lower()
#Parveido speletaja ievadito vardu viena rinda un mazajiem burtiem
	print('\n'*20)
#Paslepj ievadito vardu
	uzsakt_speli(vards)
#sauc atpakal funkciju: uzsakt_speli
def uzsakt_speli(vards):
	speletaja_dzivibas = 6
	izmantotie_burti =[]
	burtu_daudzums=["_" for i in range(len(vards))]
#Saspiez sarakstu un burtu daudzumu
	print(visuals(speletaja_dzivibas))
	print("")
	print("")
	print(" ".join(burtu_daudzums))
#Izmantos join funkciju 
	while speletaja_dzivibas == speletaja_dzivibas:
#Atkartojas visulaiku
		ievadi_burtu =input("2.Speletaj, mini burtu: ")
		print('\n'*20)
		if len(ievadi_burtu) > 1:
#Parbauda vai inputa ir vairak ka divi burti
			speletaja_dzivibas-= 1
			print(visuals(speletaja_dzivibas))
			print(ievadi_burtu,"NAV \'BURTS ČĪTERI\'!")
			print("Izlietotie burti:"," ".join(izmantotie_burti))
			print((atjaunotie_burti(vards,ievadi_burtu,burtu_daudzums,)),'')
#nozog dzivibu, parada zimejumu, progesu un lietotos burtus
		elif ievadi_burtu  not in izmantotie_burti and ievadi_burtu in vards:
#Parbauda vai burts nav ieksa vārda.
			print(visuals(speletaja_dzivibas))
			print("Pareizi,",ievadi_burtu,"Ir iekšā varda!")
			if ievadi_burtu not in izmantotie_burti:
				izmantotie_burti.append(str(ievadi_burtu))
			else:
				pass
			print("Izlietotie burti:"," ".join(izmantotie_burti))
			print((atjaunotie_burti(vards,ievadi_burtu,burtu_daudzums,)),'')
#Uzliek jaunu zimejumu, un parada progresu
		elif ievadi_burtu not in vards :
#Parbauda vai minetais burts nav varda ieksa
			speletaja_dzivibas-=1
			print(visuals(speletaja_dzivibas))
			print("Nepareizi BOT,",ievadi_burtu,"nav pareizais burts!")
			if ievadi_burtu not in izmantotie_burti:
				izmantotie_burti.append(str(ievadi_burtu))
			else:
				pass
			print("Izlietotie burti:"," ".join(izmantotie_burti))
			print((atjaunotie_burti(vards,ievadi_burtu,burtu_daudzums,)),'')
#nozog divibas, un met ara zimejumus
		elif ievadi_burtu in izmantotie_burti:
#Parbauda, vaj burts nav gadijuma izmantots
			speletaja_dzivibas-=1
			print(visuals(speletaja_dzivibas))
			print("Necakare mani, so burtu jau vadiji ieksa",ievadi_burtu)
			if ievadi_burtu not in izmantotie_burti:
				izmantotie_burti.append(str(ievadi_burtu))
			else:
				pass
			print("Izlietotie burti:"," ".join(izmantotie_burti))
			print((atjaunotie_burti(vards,ievadi_burtu,burtu_daudzums,)),'')
#nozog divibas, un met ara zimejumus
		if speletaja_dzivibas == 0:
			tu_zaudeji_luzer(speletaja_dzivibas,vards)
#Parbauda vaj speletajs ir zaudejis, ja ta ir,tad izmanto funkciju : tu_zaudeji_luzer
		elif vards == "".join(burtu_daudzums):
			tu_uzvareji_varu_paspiest_roku(speletaja_dzivibas,vards)
#Parbauda vaj speletajs ir uzvarejis, ja ta ir ,tad lieto funkciju: tu_uzvareji_varu_paspiest_roku
def atjaunotie_burti(vards,ievadi_burtu,burtu_daudzums):
#tad kad speletajs uzmin burtus, si funkcija atkartojas
	for i in range(len(vards)):
		if ievadi_burtu == vards[i]:
#Parbauda vai vards ir vienads ar katru burtu atseviski
			burtu_daudzums[i] = ievadi_burtu
	return (" ".join(burtu_daudzums))
def tu_zaudeji_luzer(speletaja_dzivibas,vards):
#funkciju atgriez atpakal, kad speletajs zaude
	print("Minētajs zaudēja, lūzers","Vārds bija",vards)
	sys.exit()
#Parada vardu un tad bejdz programmu
def tu_uzvareji_varu_paspiest_roku(speletaja_dzivibas,vards):
#funkciju atgriez atpakal, kad uzmineja speletajs vardu
	print("Minētajs uzvarēja, malacis!","Vārds bija",vards)
	sys.exit()
#Parada kad bija vārds un beidz kodu
def visuals(speletaja_dzivibas):
    #Šī funkcija parada vizuali progresu
	if speletaja_dzivibas == 6:
		return"""
		_______
		|     |
		|     
		|
		|
		|
		|
		|________
		|        |
		"""
	elif speletaja_dzivibas == 5:
		return"""
		_______
		|     |
		|     O
		|
		|
		|
		|
		|________
		|        |
		"""
	elif speletaja_dzivibas == 4:
		return"""
		_______
		|     |
		|     O
		|   --|
		|
		|
		|
		|________
		|        |
		"""
	elif speletaja_dzivibas == 3:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|
		|
		|
		|________
		|        |
		"""
	elif speletaja_dzivibas == 2:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    |
		|
		|________
		|        |
		"""
	elif speletaja_dzivibaspeletaja_dzivibas == 1:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    | |
		|
		|________
		|        |
		"""
	elif speletaja_dzivibas == 0:
		return"""
		_______
		|     |
		|     l0
		|    |||
		|     |
		|    | |
		|
		|________
		| P A K A R T S|
		"""	
kareklis()
#uz sakumu
