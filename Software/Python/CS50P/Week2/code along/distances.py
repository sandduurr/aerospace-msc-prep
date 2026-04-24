distances = {
    "Voyager 1": 163, 
    "Voyager 2": 136,
    "pioneer 10": 80,
    "New Horizon": 58,
    "Vioneer 11": 44
    
}
def main():
   for distance in distances.values():
       print(f"{distance} AU is {convert(distance)} m")
   

def convert(au):
    return au * 149597870700

main()