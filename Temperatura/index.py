c = str(input("Qual medida você deseja converter?"))
h = str(input("Celsius para Fahrenheit, digite: C"))
ha = str(input("Fahrenheit para Celsius, digite: F"))
haa = str(input("Celsius para Kelvin, digite: Ck"))
ho = str(input("Kelvin para Celsius, digite: Kc")) 
hoo = str(input("Fahrenheit para Kelvin, digite Fk"))
hi = str(input("Kelvin para Fahrenheit, digite:Kf))
hii = str(input("Digite aqui:"))
if h == "C":
	ce = float(input("Digite a temperatura em Celsius:"))
	t = ((ce * 9) / 5) + 32
	print(t, "graus Fahrenheit")
if ha == "F":
	fa = float(input("Digite a temperatura em Fahrenheit:"))
	g = (fa - 32) / 1.8
	print(g, "graus Celsius")
if haa == "Ck":
	ke = float(input("Digite a temperatura em Celsius:"))
	p = ke + 273
	print(p, "graus kelvin")
if ho == "Kc":
	Kel = float(input("Digite a temperatura em Kelvin:"))
	q = Kel - 273
	print(q, "graus Celsius")
if hoo == "Fk":
	fel = float(input("Digite a temperatura em Fahrenheit:"))
	x = (fel - 32) / 1.8
	xz = x + 273
	print(xz, "graus Kelvin")
if hi == "Kf":
	kelva = float(input("Digite a temperatura em Kelvin:"))
	z = ((kelva * 9) / 5) + 32
	zx = z + 273
	print(zx, "graus Fahrenheit")
