from img_gen import img_gen
import os

# Calls img gen and starts making poles from the middle
def dataset_gen(PATH, pos_start=(0, 0), pos_mod=(10, 10)):
    if pos_mod[0] <= 0 or posmod[1] <= 0: 
        print('BAD MOD')
        return 'BAD MOD'
    # Get backgrounds
    backgrounds = os.listdir(PATH + '/background')

    # Get poles
    poles = os.listdir(PATH + '/pole')

    # reps
    # Incomplete
    reps = 0
    for b in backgrounds:
        for p in poles:
            # subfolder name
            subfolder = 'b' + b[-2:] 'p' + p[-2:]
            saveName = 'num' + str(reps)

            img_gen(pole=p, background=b, PATH=PATH,\
                saveName=saveName, subfolder=subfolder)


            reps += 1
    pass

# PATH = os.path.abspath(__file__)
# PATH = '/'.join((PATH.split('/')[:-1]))
# dataset_gen(PATH, 10)