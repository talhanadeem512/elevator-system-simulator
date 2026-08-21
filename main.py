from elevator import Elevator

def run():


    elevator = Elevator(current_floor=2)
    
    # 1. Show the building before asking for input
    elevator.display_building()
    
    # 2. Prompt user for destination
    dest = int(input("\nEnter destination floor (0-6): "))
    elevator.add_request(dest)

if __name__ == "__main__":
    run()