import re

from cyk import Parser


def create_mapping(m, inverse=False):
    mapping = dict()
    for line in m.split("\n"):
        if not inverse:
            key, value = line.split(" => ")
        else:
            value, key = line.split(" => ")
        if not mapping.get(key):
            mapping[key] = [value]
        else:
            mapping[key].append(value)
    return mapping


def parse_input(input, inverse=False):
    mapping, molecule = input.split("\n\n")
    mapping = create_mapping(mapping, inverse)
    return mapping, molecule


def part_01(x):
    mapping, molecule = parse_input(x)
    unique_molecules = set()
    for atom in mapping.keys():
        for match in re.finditer(pattern=atom, string=molecule):
            start, end = match.span()
            for sub in mapping[atom]:
                new_molecule = molecule[:start] + sub + molecule[end:]
                unique_molecules.add(new_molecule)
    return len(unique_molecules)


def cyk_algorithm(I: str, grammar: dict):
    grammar_string = "\n".join([f"{key} -> {value}" for key, value in grammar.items()])
    parser = Parser(grammar_string, I)
    print(parser.parse())


def part_02(x):
    mapping, molecule = parse_input(x, inverse=True)
    cyk_algorithm(molecule, mapping)


if __name__ == "__main__":
    with open("2015/day-19/input.txt") as f:
        input = f.read()
    print(part_01(input))
    print(part_02(input))
