
pointer = 50
password = 0

def doTurn(turnInstruction: str):
    global password
    global pointer

    previousPointer = pointer

    direction = turnInstruction[0].strip()
    distance = int(turnInstruction[1:])

    turnsRemaining = distance
    while turnsRemaining > 0:
        if (direction == 'L'): 
            pointer = pointer - 1
        else:
            pointer = pointer + 1

        pointer = pointer % 100
        if pointer == 0:
            password += 1
        turnsRemaining -= 1

    print(f"The dial is rotated {turnInstruction} to point at {pointer}.")

with open("day-01-input.txt", "r") as file:
    lines = file.readlines()
    print(f"The dial starts by pointing at {pointer}.")
    for line in lines:
        doTurn(line.strip())

    print(f"The password is {password}.")


