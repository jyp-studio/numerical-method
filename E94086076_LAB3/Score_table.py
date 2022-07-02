import random
import numpy as np


part_1 = []
for i in range(0, 104, 6):
    random.seed(i)
    part_1.append(random.randrange(40, 100, 2))
    np_part_1 = np.array(part_1)

np.random.seed(41)
part_2 = np.random.randint(30, 100, size=(3, 6))
np_part_2 = np.array(part_2)

# calculate each student total scores
reshape_np_part_1 = np.reshape(np_part_1, (3, 6))
total_score = (np.around(reshape_np_part_1 *
               0.4 + np_part_2 * 0.6)).astype(int)

# calculat avg_person
avg_person = np.array([0, 0, 0])
for i in range(len(total_score)):
    for j in range(len(total_score[i])):
        avg_person[i] += total_score[i][j]
avg_person = (np.around(avg_person / 6)).astype(int)

# calculate avg_score
avg_score = np.array([0, 0, 0, 0, 0, 0])
for i in range(len(total_score.T)):
    for j in range(len(total_score.T[i])):
        avg_score[i] += total_score.T[i][j]
avg_score = (np.around(avg_score / 3)).astype(int)

# print all
print("        ", end="")
for i in range(1, 7):
    print(f"Scores{i}  ", end="")
print("AVG_person")
for i in range(len(total_score)):
    print(f"person{i + 1}", end="   ")
    for j in range(len(total_score[i])):
        print(total_score[i][j], end="       ")
    print(avg_person[i], end="")
    print("")
print("------------------------------------------------------------------------")
print("AVG_scr", end="   ")
for i in range(len(avg_score)):
    print(avg_score[i], end="       ")
sum = 0
for i in range(len(avg_person)):
    sum += avg_person[i]
print(int(sum / 3))
