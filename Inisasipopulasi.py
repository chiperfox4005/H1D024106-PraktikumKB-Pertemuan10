import random

def inisialisasi_populasi(jumlah_populasi, jumlah_gen):
    populasi = []

    for i in range(jumlah_populasi):
        kromosom = []

        for j in range(jumlah_gen):
            gen = random.randint(0, 1)
            kromosom.append(gen)

        populasi.append(kromosom)

    return populasi


if __name__ == "__main__":

    populasi_awal = inisialisasi_populasi(10, 5)

    print("Populasi Awal")

    for i, individu in enumerate(populasi_awal):
        print(f"Individu {i+1} : {individu}")