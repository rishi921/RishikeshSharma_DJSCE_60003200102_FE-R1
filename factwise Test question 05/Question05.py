def can_complete_circuit(gas, cost):

    n = len(gas)
    starting_station = 0
    tank = 0
    deficit = 0


    for i in range(n):
        tank += gas[i] - cost[i]
        deficit = min(deficit, tank)

        if tank < 0:
            starting_station += 1
            tank = 0

    if deficit <= 0:
        return -1

    return starting_station
    
print(can_complete_circuit([2,3,4], [3,4,3]))