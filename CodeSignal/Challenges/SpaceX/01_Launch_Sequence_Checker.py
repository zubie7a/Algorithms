# https://app.codesignal.com/company-challenges/spacex/EcQD8xYZotKM77FKM
def launchSequenceChecker(system_names, step_numbers):
    # Check if for each of the system names given, the last step number
    # performed is strictly increasing.
    last_steps = {}
    for idx in range(len(system_names)):
        # Get the system name and the step number to perform at each iteration.
        system_name = system_names[idx]
        step_number = step_numbers[idx]
        # If we had already recorded a previous step for this system name...
        if system_name in last_steps:
            last_step = last_steps[system_name]
            # Check that the steps are strictly increasing, that is, the current
            # step number is not same or lower than previous recorded step.
            if last_step >= step_number:
                return False
        # Now just record the current step as the last one. No need to store
        # all of them, just the last is enough to validate strictly increasing.
        last_steps[system_name] = step_number

    # All elements satisfied the condition so launch sequence is ready!
    return True
