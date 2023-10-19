# user input
capacity = int(input())
fans = int(input())

# logic
total_fans = 0
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
for i in range(fans):
    sector = input()
    total_fans += 1
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

sector_a_perc = sector_a / total_fans * 100
sector_b_perc = sector_b / total_fans * 100
sector_v_perc = sector_v / total_fans * 100
sector_g_perc = sector_g / total_fans * 100
fans_perc = total_fans / capacity * 100

# code output
print(f"{sector_a_perc:.2f}%")
print(f"{sector_b_perc:.2f}%")
print(f"{sector_v_perc:.2f}%")
print(f"{sector_g_perc:.2f}%")
print(f"{fans_perc:.2f}%")
