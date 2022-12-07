with open('2022/day-06/input.txt') as f:
    signal = f.read().strip()


def find_start(string, marker_length):
    for i in range(len(signal) - marker_length):
        substring = signal[i:i+marker_length]
        if len(set(substring)) == marker_length:
            return i + marker_length


print(find_start(signal, 4))
print(find_start(signal, 14))
