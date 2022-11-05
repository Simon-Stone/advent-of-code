import hashlib

def part_01(seed):
    i = 1
    while True:
        hash = hashlib.md5(bytes(seed + str(i), 'utf-8'))
        if hash.hexdigest().startswith('0'*5):
            return i
        i += 1


def part_02(seed):
    i = 1
    while True:
        hash = hashlib.md5(bytes(seed + str(i), 'utf-8'))
        if hash.hexdigest().startswith('0'*6):
            return i
        i += 1


if __name__ == '__main__':
    seed = 'yzbqklnj'

    print(part_01(seed))
    print(part_02(seed))