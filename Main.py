import random
import matplotlib.pyplot as plt

from InisiasiPopulasi import inisialisasi_populasi
from EvaluasiFitness import hitung_fitness
from selection import roulette_wheel_selection
from crossover import one_point_crossover
from mutation import swap_mutation

# Data Barang
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]

kapasitas_tas = 15


def genetic_algorithm():

    jumlah_generasi = 50
    jumlah_populasi = 10

    crossover_rate = 0.7
    mutation_rate = 0.1

    jumlah_gen = len(barang)

    # Inisialisasi Populasi
    populasi = inisialisasi_populasi(
        jumlah_populasi,
        jumlah_gen
    )

    grafik_fitness = []

    best_individu = None
    best_fitness = 0

    # Proses Generasi
    for generasi in range(jumlah_generasi):

        fitness_populasi = []

        for individu in populasi:

            fitness = hitung_fitness(
                individu,
                barang,
                kapasitas_tas
            )

            fitness_populasi.append(fitness)

        fitness_terbaik = max(fitness_populasi)

        grafik_fitness.append(fitness_terbaik)

        if fitness_terbaik > best_fitness:

            best_fitness = fitness_terbaik

            index = fitness_populasi.index(
                fitness_terbaik
            )

            best_individu = populasi[index]

        populasi_baru = []

        while len(populasi_baru) < jumlah_populasi:

            # Seleksi
            parent1 = roulette_wheel_selection(
                populasi,
                fitness_populasi
            )

            parent2 = roulette_wheel_selection(
                populasi,
                fitness_populasi
            )

            # Crossover
            if random.random() < crossover_rate:

                anak1, anak2 = one_point_crossover(
                    parent1,
                    parent2
                )

            else:

                anak1 = parent1.copy()
                anak2 = parent2.copy()

            # Mutasi
            if random.random() < mutation_rate:
                anak1 = swap_mutation(anak1)

            if random.random() < mutation_rate:
                anak2 = swap_mutation(anak2)

            populasi_baru.extend([anak1, anak2])

        populasi = populasi_baru[:jumlah_populasi]

    # Output Hasil
    print("\nHASIL TERBAIK")
    print("Fitness Terbaik :", best_fitness)

    total_ukuran = 0

    print("\nBarang Yang Dipilih :")

    for i in range(len(best_individu)):

        if best_individu[i] == 1:

            print(
                f"- {barang[i][0]}"
            )

            total_ukuran += barang[i][2]

    print("\nTotal Ukuran :", total_ukuran)

    # Grafik
    plt.plot(grafik_fitness)

    plt.title("Perkembangan Fitness")
    plt.xlabel("Generasi")
    plt.ylabel("Fitness")

    plt.grid(True)

    plt.show()


genetic_algorithm()