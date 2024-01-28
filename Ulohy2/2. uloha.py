import os

def precti_body(cesta_k_souboru):
    """Čte body ze souboru a vrací je jako seznam dvojic."""
    try:
        with open(cesta_k_souboru, 'r') as soubor:
            radky = soubor.read().splitlines()
        body = []
        for radek in radky:
            casti = radek.split()
            body.append((float(casti[0]), float(casti[1])))
        return body
    except:
        raise ValueError("Neplatný formát vstupu")

def vzdalenost(b1, b2):
    """Vrací vzdálenost mezi dvěma body."""
    return ((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2)**0.5

def jsou_kolinearni(b1, b2, b3):
    """Zjišťuje, zda jsou tři body kolineární (leží na jedné přímce)."""
    if vzdalenost(b1, b2) + vzdalenost(b2, b3) == vzdalenost(b1, b3):
        return True
    if vzdalenost(b1, b2) + vzdalenost(b1, b3) == vzdalenost(b2, b3):
        return True
    if vzdalenost(b1, b3) + vzdalenost(b2, b3) == vzdalenost(b1, b2):
        return True
    return False

def najdi_prostredni_bod(b1, b2, b3):
    """Najde prostřední bod mezi třemi kolineárními body."""
    body = sorted([b1, b2, b3])
    return body[1]

def body_splyvaji(body):
    return len(set(body)) != len(body)

cesta_adresar = 'test_cases_2/CZE/'

for nazev_souboru in os.listdir(cesta_adresar):
    if nazev_souboru.endswith("_in.txt"):
        cesta_k_souboru = os.path.join(cesta_adresar, nazev_souboru)
        try:
            body = precti_body(cesta_k_souboru)
            if len(body) != 3:
                print(f"Soubor {nazev_souboru} neobsahuje přesně tři body.")
                continue
            if body_splyvaji(body):
                print(f"{nazev_souboru} Body splývají.")
                continue
            if jsou_kolinearni(*body):
                prostredni_bod = najdi_prostredni_bod(*body)
                prostredni_bod = "ABC"[body.index(prostredni_bod)]
                print(f"{nazev_souboru}: Body leží na stejné přímce. Prostřední bod je {prostredni_bod}.")
            else:
                print(f"{nazev_souboru}: Body neleží na stejné přímce.")

        except ValueError as e:
            print(f"Chyba v souboru {nazev_souboru}: {e}")