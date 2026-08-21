import heapq()
class Elevator:
    def __init__(self, total_floors=10, current_floor=0, dest_floor):
        self.total_floors = total_floors
        self.current_floor = current_floor
        self.direction = "IDLE"
        self.up_queue = []
        self.down_queue = []

        if dest_floor < 0:
            return "The destination floor should be greater than 0"

        elif dest_floor == self.current_floor:
            print(f"Elevator is {self.direction}")

        elif dest_floor > self.current_floor:
            heapq.heappush(self.up_queue, dest_floor)

        else:
            heapq.heappush(self.down_queue, dest_floor)
    

    def display_building(self):
        """Draws a vertical shaft showing all floors and the elevator's current position."""
        width = 24
        border = "+" + "-" * width + "+"

        # A display for users before they enter their destination floor.
        print("\n" + border)
        print("|{:^24}|".format("BUILDING SHAFT"))
        print(border)

        
        for floor in range(self.total_floors, -1, -1):
            if floor == self.current_floor:
                row_content = f" [Floor {floor:02d}] <== [ELEVATOR]"
            else:
                row_content = f" [Floor {floor:02d}] |"
            
            print(f"| {row_content:<{width - 1}}|")

            if floor > 0:
                print("|" + " " * width + "|")

        print(border)