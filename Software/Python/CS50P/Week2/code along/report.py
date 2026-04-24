def main():
    spacecraft = {"name": "James Webb Space Telescope", "distance": 163}
    spacecraft.update({"distance": 0.01, "orbit": "sun"})
    print(create_report(spacecraft))
    
    
def create_report(spacecraft):
    return f"""
    =======report=======
    
    name: {spacecraft.get("name","unknown")}
    distance: {spacecraft.get("distance", "unknown")} AU
    orbit: {spacecraft.get("orbit", "unknown")}
    
    ====================
    """
    
main()