import random

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Randomizes the block_map
ran_blocks = []
ran_blocks2 = []

for i in range(6):
    nums = random.randint(111111111111, 888888888888)
    ran_blocks.append(str(nums))

for i in range(len(ran_blocks)):
    single_num = [x.replace('0', '1').replace('9', '8') for x in ran_blocks[i]]
    ran_blocks2.append(''.join(single_num))

BLOCK_MAP = [
    f'{ran_blocks2[0]}',
    f'{ran_blocks2[1]}',
    f'{ran_blocks2[2]}',
    f'{ran_blocks2[3]}',
    f'{ran_blocks2[4]}',
    f'{ran_blocks2[5]}',
    '                ',
    '                ',
    '                '
]

COLOR_LEGEND = {
    '1': 'blue',
    '2': 'green',
    '3': 'red',
    '4': 'orange',
    '5': 'purple',
    '6': 'bronce',
    '7': 'grey',
    '8': 'black'
}

GAP_SIZE = 2
BLOCK_HEIGHT = WINDOW_HEIGHT / len(BLOCK_MAP) - GAP_SIZE
BLOCK_WIDTH = WINDOW_WIDTH / len(BLOCK_MAP[0]) - GAP_SIZE
TOP_OFFSET = WINDOW_HEIGHT // 30

UPGRADES = ['speed', 'laser', 'heart', 'size']
