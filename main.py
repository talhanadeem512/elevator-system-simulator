from elevator import Elevator

def run():
    elevator = Elevator(total_floors=10, current_floor=0)
    elevator.display_building()

    print("\n--- ELEVATOR SIMULATION STARTED ---")
    print("Type a floor number to request a stop.")
    print("Press ENTER to step time forward by one move.")
    print("Type 'quit' to exit.")

    # Implemented Tick-Based Simulation to mimic real-world elevators.
    while True:
        # At this moment, the loop freezes for the user to make a decision.
        user_input = input("\nThe Tick Action (>): ").strip().lower()

        # Escape condition to exit the infinite loop.
        if user_input == 'quit':
            print("Ending simulation...")
            break

        # As users keep adding floors, the program categorizes them into the 
        # suitable Min-Heap or Max-Heap priority queue.
        elif user_input.isdigit():
            dest = int(user_input)
            elevator.add_request(dest)
            
            print(f"Pending UP: {elevator.up_queue}")
            print(f"Pending DOWN: {elevator.down_queue}")

        # Advances time by one tick, executing the next movement.
        elif user_input == "":
            if len(elevator.up_queue) > 0 or len(elevator.down_queue) > 0:
                elevator.move()

            # Handles the idle state when both queues are empty.
            else:
                print("[Elevator] IDLE. Waiting for passengers.")
   
        else:
            print("Invalid command. Enter a number, press ENTER, or type 'quit'.")

if __name__ == "__main__":
    run()