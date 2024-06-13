def vokal(bokstav):
    vokaler = "aeiouyåäö"
    return bokstav.lower() in vokaler

ord = input("Skriv ett ord du vill översätta till rövarspråk: ")

översatt_ord = ""

for bokstav in ord:
    if vokal(bokstav):
        översatt_ord = översatt_ord + bokstav
    else:
        översatt_ord = översatt_ord + bokstav + 'o' + bokstav

print(översatt_ord)