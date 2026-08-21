from elevator import Elevator

def run():


    elevator = Elevator()
    
    # 1. Show the building before asking for input
    elevator.display_building()

    while true:
        print("Enter the floor you want to go.")
        print("Press enter button or type 'done' if everyone is inside and elevator is ready to move")
        dest = input()
        if dest.isdigit():
            dest = int(dest)

        elif dest == '\n' or dest.lower() == 'done':
            elevator.move()

    # 2. Prompt user for destination
    dest = int(input("\nEnter destination floor (0-10): "))
    elevator.add_request(dest)

if __name__ == "__main__":
    run()