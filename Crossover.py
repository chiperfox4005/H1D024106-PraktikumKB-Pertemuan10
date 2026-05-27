import random

# One Point Crossover
def one_point_crossover(parent1, parent2):

    titik = random.randint(1, len(parent1)-1)

    anak1 = parent1[:titik] + parent2[titik:]
    anak2 = parent2[:titik] + parent1[titik:]

    return anak1, anak2


if __name__ == "__main__":

    parent1 = [1, 0, 1, 1, 0]
    parent2 = [0, 1, 0, 0, 1]

    anak1, anak2 = one_point_crossover(
        parent1,
        parent2
    )

    print("Hasil Crossover")
    print("Anak 1 :", anak1)
    print("Anak 2 :", anak2)