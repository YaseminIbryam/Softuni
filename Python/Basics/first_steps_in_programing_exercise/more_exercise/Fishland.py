price_mackerel = float(input())
price_sprat = float(input())
kg_bonito = float(input())
kg_scad = float(input())
kg_mussels = int(input())
bonito = (60/100 * price_mackerel) + price_mackerel
scad = (80/100 * price_sprat) + price_sprat
mussels = 7.50
price_bonito = bonito * kg_bonito
price_scad = scad * kg_scad
price_mussels = mussels * kg_mussels
bill = price_bonito + price_scad + price_mussels
print(f"{bill:.2f}")
