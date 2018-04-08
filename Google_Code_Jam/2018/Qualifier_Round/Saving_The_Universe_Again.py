# 01 - Saving The Universe Again

t = int(input())

def laser_strength(instructions):
    strength = 1
    energy   = 0
    for i in range(0, len(instructions)):
        char = instructions[i]
        if (char == "S"):
            energy += strength
        elif (char == "C"):
            strength *= 2
    return energy

for case in range(1, t + 1):
    # Each line contains the shield energy and laser firing sequence.
    energy, instructions = input().strip().split(" ")
    energy = int(energy)
    swaps = 0
    swapped = False
    success = False
    num = len(instructions)
    while True:
        # Stop swapping once the laser energy has been reduced enough to
        # not destroy the shield.
        if (laser_strength(instructions) <= energy):
            success = True
            break
        swapped = False
        # Iterate from the end of the string finding a position to swap,
        # this "strategy" makes it so we focus on the right-most elements,
        # as they are going to have the highest energy.
        for i in range(num - 1, 0, -1):
            pre, pos = instructions[i - 1], instructions[i]
            # In the case of a C(harge) preceding a S(hoot), swap them!
            if (pre == "C" and pos == "S"):
                ins_array = bytearray(instructions, 'utf8')
                ins_array[i - 1] = ord('S')
                ins_array[i]     = ord('C')
                instructions = ins_array.decode('utf8')
                swapped = True
                swaps += 1
                break
        # If nothing was swapped, it means its no longer possible to swap
        # anything, and if it hasn't exited yet it means its impossible
        # to do swaps to prevent the shield being destroyed.
        if (not swapped):
            success = False
            break
    
    result = "Case #%d: " % (case)
    result += str(swaps) if (success) else "IMPOSSIBLE"
    print(result)
