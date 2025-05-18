import hashlib


def is_interesting(hash: str) -> bool:
    return hash[:5] == "0" * 5


def part_01(door_id: str) -> str:
    target_length = 8
    password = ""
    index = 0
    while len(password) < target_length:
        hash = hashlib.md5((door_id + str(index)).encode()).hexdigest()
        if is_interesting(hash):
            password += hash[5]
        index += 1
    return password


def part_02(door_id: str) -> str:
    password: list[str] = [""] * 8
    index = 0
    while any(p == "" for p in password):
        hash = hashlib.md5((door_id + str(index)).encode()).hexdigest()
        try:
            if is_interesting(hash) and password[int(hash[5])] == "":
                password[int(hash[5])] = hash[6]
        except (IndexError, ValueError):
            pass
        index += 1
    return "".join(password)


if __name__ == "__main__":
    # door_id = "abc"
    door_id = "uqwqemis"

    print(part_01(door_id))
    print(part_02(door_id))
