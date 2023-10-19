from collections import deque

pump_stations = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
pump_stations_copy = pump_stations.copy()
gas = 0
index = 0

while pump_stations_copy:
    gas_station, distance = pump_stations_copy.popleft()

    gas += gas_station

    if gas >= distance:
        gas -= distance
    else:
        pump_stations.rotate(-1)
        pump_stations_copy = pump_stations.copy()
        gas = 0
        index += 1

else:
    print(index)
