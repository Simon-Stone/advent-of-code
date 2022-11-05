import numpy as np
from collections import Counter

if __name__ == '__main__':
    with open('Day3-input.txt') as f:
        numbers = list(map(str.strip, f.readlines()))
       
    numbers = np.array([list(map(int, [*number])) for number in numbers])
    gamma = ""
    epsilon = ""
    oxygen_rating = 0
    co2_scrubber_rating = 0
    for number in numbers.T:
        most_frequent = Counter(number).most_common(1)[0][0]
        gamma += str(most_frequent)
        epsilon += str(1 - most_frequent)
    
    print(int(gamma, 2) * int(epsilon, 2))

    # Oxygen
    for pos, bits in enumerate(numbers.T):
        first, second = Counter(bits).most_common(2)
        if first[1] == second[1]:
            most_frequent = 1
        else:
            most_frequent = first[0]
        candidates = [number for number in numbers if number[pos] == most_frequent]
        if len(candidates) > 1:
            continue
        else:
            oxygen_rating = candidates[0]
            break
      
    
    # co2
    for pos, bits in enumerate(numbers.T):
        most, least = Counter(bits).most_common(2)
        if most[1] == least[1]:
            least_frequent = 0
        else:
            least_frequent = least[0]
        candidates = [number for number in numbers if number[pos] == least_frequent]
        if len(candidates) > 1:
            continue
        else:
            co2_scrubber_rating = candidates[0]
            break

    print(f"{oxygen_rating=}")
    print(f"{co2_scrubber_rating=}")

    life_support_rating = oxygen_rating * co2_scrubber_rating
    print(f"{life_support_rating=}")