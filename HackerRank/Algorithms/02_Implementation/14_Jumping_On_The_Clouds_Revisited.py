# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
# Aerith will jump around circularly aligned clouds,
# with k-length jumps, until reaching position 0 again.
n, k = map(int, raw_input().split())
# Clouds are normal (0) or thunderclouds (1)
clouds = map(int, raw_input().split())
# The initial position is 0, and energy is 100.
pos, energy = 0, 100
while True:
    # Clouds are circular, so it will keep wrapping around.
    pos = (pos + k) % n
    # Jumping clouds takes 1 energy, but landing on a thundercloud
    # takes extra 2 energy.
    energy -= (1 + clouds[pos]*2)
    # When it reaches position 0 again, it exits.
    if pos == 0:
        break
# Print the final energy amount.
print energy
