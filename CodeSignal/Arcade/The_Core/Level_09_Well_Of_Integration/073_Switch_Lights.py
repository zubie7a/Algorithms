# https://app.codesignal.com/arcade/code-arcade/well-of-integration/x3ix7CY93z2bwKDtG
def switchLights(lights):
    # After getting a list of on/off lights, an algorithm starts from the left.
    # For each light, if it's on, switch it and all previous ones to opposite.
    # In the end, how many lights remain turned on?

    # If we iterate left-to-right, then at every change we have to recheck
    # the previous ones. If we iterate right-to-left, changes will be propagated
    # to the left hence no need to deal with previously visited from-right lights.
    result = []
    # Every time an on light is found, the flipping switches. A double flip just
    # resets things to original state.
    flip = 0
    for light in reversed(lights):
        # If a light is found on, then flip the switch that propagates changes to left.
        if light == 1:
            flip = 1 if flip == 0 else 0
        # If the flip is on, then switch this light.
        if flip == 1:
            light = 0 if light == 1 else 1
        # Store the state of this light.
        result.append(light)

    # Re-reverse the result.
    return result[::-1]
