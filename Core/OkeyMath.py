import random

def shuffle(vec:list):
    random.seed(125)
    vec_new=random.sample(vec, len(vec))
    return vec_new

def random_int(lim:int):
    return random.randint(0,lim-1)