# https://app.codesignal.com/company-challenges/uber/HNQwGHfKAoYsz9KX6
def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    # For all available cars, calculate the fares according to estimated
    # time, estimated distance, and the costs per time/distance per car.
    total_cars = len(cost_per_minute)
    total_fares = [0 for _ in range(total_cars)]
    for i in range(total_cars):
        time_cost = ride_time * cost_per_minute[i]
        dist_cost = ride_distance * cost_per_mile[i]
        total_fares[i] = time_cost + dist_cost

    return total_fares
