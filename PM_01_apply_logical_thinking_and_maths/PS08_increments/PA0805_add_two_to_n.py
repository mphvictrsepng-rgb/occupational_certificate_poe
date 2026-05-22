# This function returns a valid list of steps
# You can only take 1, 2, or 3 steps
# You cannot repeat the same step twice in a row

def climb_stairs(N, stairs):

    steps = []  # store the steps taken
    last_step = 0
    total = 0

    while total < stairs:

        # try possible step sizes
        for step in [1, 2, 3]:

            # to avoid repeating the same step
            if step != last_step:

                # this ensures we do not go over the staircase
                if total + step <= stairs:

                    steps.append(step)

                    total += step

                    last_step = step

                    break

    return steps


# e.g., 
print(climb_stairs(3, 10))