# Conversor de Temperatura

c = str(input("Qual medida você deseja converter?\n Celsius para Fahrenheit, digite: C\n Fahrenheit para Celsius, digite: F\n Celsius para Kelvin, digite: Ck\n Kelvin para Celsius, digite: Kc\n Fahrenheit para Kelvin, digite: Fk\n Kelvin para Fahrenheit, digite Kf\n Digite aqui:"))
if c == "C":
	ce = float(input("Digite a temperatura em Celsius:"))
	t = ((ce * 9) / 5) + 32
	print(t, "graus Fahrenheit")
if c == "F":
	fa = float(input("Digite a temperatura em Fahrenheit:"))
	g = (fa - 32) / 1.8
	print(g, "graus Celsius")
if c == "Ck":
	ke = float(input("Digite a temperatura em Celsius:"))
	p = ke + 273
	print(p, "graus kelvin")
if c == "Kc":
	Kel = float(input("Digite a temperatura em Kelvin:"))
	q = Kel - 273
	print(q, "graus Celsius")
if c == "Fk":
	fel = float(input("Digite a temperatura em Fahrenheit:"))
	x = (fel - 32) / 1.8
	xz = x + 273
	print(xz, "graus Kelvin")
if c == "Kf":
	kelva = float(input("Digite a temperatura em Kelvin:"))
	z = ((kelva * 9) / 5) + 32
	zx = z + 273
	print(zx, "graus Fahrenheit")

