import fajlbeolvasas
fajlbeolvasas.beolvas()

print("1. feladat")
print(f"\t A listán szereplő filmek száma: {fajlbeolvasas.filmek_szama()}")

print("2. feladat")
print(f"\t A legrövidebb film címe: {fajlbeolvasas.legrovidebb()}")

print("3. feladat")
print(f"\t 110 perces filmek száma: {fajlbeolvasas.szaztizperc()}")

print("4. feladat")
print(f"\t Ezeket a filmeket ajánljuk Önnek: {fajlbeolvasas.film_ajanlo()}")