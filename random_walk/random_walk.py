import random
import matplotlib.pyplot as plt
import pandas as pd



walkers = int(input("Please enter number of walkers: "))
assert walkers > 0, "Enter positive number"
dims = int(input("Please enter number of dimensions: "))
assert dims > 0, "Enter positive number"
steps = int(input("Please enter number of steps: "))
assert steps > 0, "Enter positive number"

def display_cordinates(cordinates):
    walkers= len(cordinates)
    dims = len(cordinates[0])
    steps = len(cordinates[0][0])
    for walker in range(walkers):
        match dims:
            case 1:
                plt.plot([_ for _ in range(steps)] ,cordinates[walker][0])
            case 2:
                plt.plot(cordinates[walker][1] ,cordinates[walker][0])
            case 3:
                if walker == 0:
                    ax = plt.axes(projection= "3d")
                ax.plot(cordinates[walker][0], cordinates[walker][1], cordinates[walker][2])
            case _:
                data = {f"dim {i}": cordinates[walker][i] for i in range(dims)}
                print(f"walker: {walker+1}")
                print("step", end=" ")
                print(pd.DataFrame(data,index=[i for i in range(steps)]))
                print()
    if dims < 4:
        plt.show()

    




def random_stape(cordinates,walker):

    dims = len(cordinates[0])
    steps = len(cordinates[0][0])
    for step in range(1,steps):
        for dim in range(dims):
            cordinates[walker][dim][step] = cordinates[walker][dim][step-1]
        rand_dim = random.randint(0,dims-1)
        rand_stape = random.choice([-1,1])
        cordinates[walker][rand_dim][step]+=rand_stape


def random_walk(walkers,dims,steps):

    cordinates= [[[0] * (steps+1) for _ in range(dims)] for _ in range(walkers)] 
    for walker in range(walkers):
        random_stape(cordinates,walker)
    display_cordinates(cordinates)


random_walk(walkers,dims,steps)