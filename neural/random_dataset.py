import random

dataset = []
for i in range(100):
    dataset.append(random.choice([[str(round(random.uniform(0.5, 1.0), 2)), str(round(random.uniform(0.5, 1.0), 2)), str(round(random.uniform(0.5, 1.0), 2)), str(1)],
                                  [str(round(random.uniform(0.0, 0.5), 2)), str(round(random.uniform(0.0, 0.5), 2)), str(round(random.uniform(0.0, 0.5), 2)), str(0)]]))

with open("random_dataset.csv", "a+") as f:
    for data in dataset:
        f.write(",".join(data) + "\n")
