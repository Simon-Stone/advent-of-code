from itertools import batched

import numpy as np
from tqdm import tqdm


def defrag(disk):
    defrag_disk = []
    file_blocks = list(disk[~np.isnan(disk)])
    for block in disk:
        if np.isnan(block):
            defrag_disk.append(file_blocks.pop())
        else:
            defrag_disk.append(block)
        if len(defrag_disk) == len(disk[~np.isnan(disk)]):
            return np.array(defrag_disk)


def defrag_whole(disk_map):
    file_blocks, free_blocks = disk_map[::2], disk_map[1::2]
    defrag_file_blocks = [(idx, n_blocks) for idx, n_blocks in enumerate(file_blocks)]
    for idx, n_blocks in tqdm(enumerate(file_blocks[::-1]), total=len(file_blocks)):
        file_id = len(file_blocks) - 1 - idx
        for insert_idx, n_free in enumerate(free_blocks):
            file_pos = defrag_file_blocks.index((file_id, n_blocks))
            if insert_idx >= file_pos:
                break
            if n_free >= n_blocks:
                defrag_file_blocks.remove((file_id, n_blocks))
                defrag_file_blocks.insert(insert_idx + 1, (file_id, n_blocks))
                free_blocks[insert_idx] -= n_blocks
                free_blocks[file_pos - 1] += n_blocks
                if file_id < len(free_blocks):
                    free_blocks[file_pos - 1] += free_blocks.pop(file_pos)
                free_blocks.insert(insert_idx, 0)
                break

    disk = []
    for (file_id, n_blocks), *n_free in zip(defrag_file_blocks, free_blocks):
        disk.extend(n_blocks * [file_id])
        if n_free:
            disk.extend(n_free[0] * [np.nan])
    return np.array(disk)


def checksum(disk):
    return np.sum(disk * range(disk.shape[0]), where=~np.isnan(disk))


def map_to_disk(disk_map):
    disk = []
    for file_id, (n_blocks, *n_free) in enumerate(batched(disk_map, n=2)):
        disk.extend(int(n_blocks) * [file_id])
        if n_free:
            disk.extend(int(n_free[0]) * [np.nan])
    return np.array(disk)


def part_01(disk):
    defrag_disk = defrag(disk)
    return checksum(defrag_disk)


def part_02(disk):
    defrag_disk = defrag_whole(disk)
    return checksum(defrag_disk)


if __name__ == "__main__":
    with open("2024/day-09/input.txt") as f:
        disk_map = [int(c) for c in f.read()]

    disk = map_to_disk(disk_map)
    print(part_01(disk))
    print(part_02(disk_map))
