# user input
crews = int(input())

# logic
total = 0
musala_crew = 0
monblan_crew = 0
kilimanjaro_crew = 0
k2_crew = 0
everest_crew = 0

for i in range(crews):
    crew = int(input())
    if crew <= 5:
        musala_crew += crew
        total += crew
    elif 6 <= crew <= 12:
        monblan_crew += crew
        total += crew
    elif 13 <= crew <= 25:
        kilimanjaro_crew += crew
        total += crew
    elif 26 <= crew <= 40:
        k2_crew += crew
        total += crew
    else:
        everest_crew += crew
        total += crew

musala_perc = musala_crew / total * 100
monblan_perc = monblan_crew / total * 100
kilimanjaro_perc = kilimanjaro_crew / total * 100
k2_perc = k2_crew / total * 100
everest_perc = everest_crew / total * 100

# code output
print(f"{musala_perc:.2f}%")
print(f"{monblan_perc:.2f}%")
print(f"{kilimanjaro_perc:.2f}%")
print(f"{k2_perc:.2f}%")
print(f"{everest_perc:.2f}%")
