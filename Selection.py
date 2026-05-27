import random

# Roulette Wheel Selection
def roulette_wheel_selection(populasi, fitness_populasi):

    total_fitness = sum(fitness_populasi)

    if total_fitness == 0:
        return random.choice(populasi)

    probabilitas = []

    for fitness in fitness_populasi:
        probabilitas.append(fitness / total_fitness)

    r = random.random()

    total = 0

    for i in range(len(populasi)):

        total += probabilitas[i]

        if r <= total:
            return populasi[i]

    return populasi[-1]


if __name__ == "__main__":

    populasi = [
        "Individu1",
        "Individu2",
        "Individu3",
        "Individu4"
    ]

    fitness = [10, 20, 30, 40]

    parent = roulette_wheel_selection(
        populasi,
        fitness
    )

    print("Parent Terpilih :", parent)