import random

# Swap Mutation
def swap_mutation(kromosom):

    kromosom = kromosom.copy()

    posisi1, posisi2 = random.sample(
        range(len(kromosom)),
        2
    )

    kromosom[posisi1], kromosom[posisi2] = (
        kromosom[posisi2],
        kromosom[posisi1]
    )

    return kromosom


if __name__ == "__main__":

    kromosom = [1, 0, 1, 1, 0]

    hasil = swap_mutation(kromosom)

    print("Sebelum :", kromosom)
    print("Sesudah :", hasil)