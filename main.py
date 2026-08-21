from elevator import Elevator

def run():


    elevator = Elevator()
    
    # 1. Show the building before asking for input
    elevator.display_building()

    while True:
        print("Enter the floor you want to go.")
        print("Press enter button or type 'done' if everyone is inside and elevator is ready to move")
        dest = input("> ")
        if dest.isdigit():
            dest = int(dest)
            elevator.add_request(dest)

        elif dest == "" or dest.lower() == 'done':
            print("Closing the doors. Preparing to move...")
            break

        else:
            print("Enter a valid floor number.")

        print(f"\nUp Queue: {elevator.up_queue}")
        print(f"Down Queue: {elevator.down_queue}")

    print("\n--- ELEVATOR IS MOVING ---")
    while len(elevator.up_queue) > 0 or len(elevator.down_queue) 0:
        elevator.move()
if __name__ == "__main__":
    run()