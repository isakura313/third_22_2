products = "skovorodki skovorodka chainick kniga shkag pampersi sigara"

sizes = ['xs', 'xl', 'xxl']

product_arr = products.split()
print(product_arr)
skovorodki = []
skovorodki_all_sizes = []

for word in product_arr:
    if word.startswith("sko") == True:
        skovorodki.append(word)

print(skovorodki)

for skovordka in skovorodki:
    for size in sizes:
        skovorodki_all_sizes.append(skovordka + "_"+size)

print(skovorodki_all_sizes)