paciente = input()
doador = input()
if doador == "O":
    print("transfusao compativel")
elif paciente == "AB":
    print("transfusao compativel")
elif paciente == doador:
    print("transfusao compativel")
else:
    print("transfusao incompativel")