distance = float(input("distance (km) : "))
if (distance < 1):
    print("Pls, fill you distance more than 1 km")

time =float(input("Time (h) :  "))
if(time < 1):
    print("You time more than 1 Hour")
result = distance / time
print(result, "Km/h")
