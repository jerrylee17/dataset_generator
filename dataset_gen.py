from img_gen import img_gen
import os

# Calls img gen and starts making poles from the middle
# scaleFactor does not work fully
def dataset_gen(PATH, posStart=(0, 0), posMod=(10, 10), scaleFactor=(3, 7)):
    if posMod[0] <= 0 or posMod[1] <= 0: 
        print('BAD MOD')
        return 'BAD MOD'

    # Get backgrounds
    backgrounds = os.listdir(PATH + '/background')

    # Get poles
    poles = os.listdir(PATH + '/pole')

    reps = 0
    currPos = list(posStart)
    status = ''
    for b in backgrounds:
        for p in poles:
            # subfolder name
            subfolder = 'b' + b.split('.')[0][-2:]\
                + 'p' + p.split('.')[0][-2:]
            
            while True:
                saveName = 'num' + str(reps)

                status = img_gen(pole=p, background=b, PATH=PATH, \
                    saveName=saveName, pos=currPos, scaleFactor=6, \
                    subfolder=subfolder)
                
                print(status)

                if status == 'WIDTH_ERR': 
                    currPos[0] = posStart[0]
                    currPos[1] += posMod[1]
                elif status == 'SAVED': 
                    currPos[0] += posMod[0]
                    reps += 1
                else: break
    print('DATASET GENERATION COMPLETED')
    return True


# PATH = os.path.abspath(__file__)
# PATH = '/'.join((PATH.split('/')[:-1]))
dataset_gen(PATH, posStart=(100, 300), posMod=(100, 100))
