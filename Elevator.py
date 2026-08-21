import heapq
class Elevator:
    """
    Represents a single elevator car.
    Uses Min-Heap and Max-Heap priority queues to implement SCAN algorithm, ensuring efficient movement wihtout backtracking.
    """
    def __init__(self, total_floors=10, current_floor=0):
        self.total_floors = total_floors
        self.current_floor = current_floor
        self.direction = "IDLE"
        self.up_queue = []
        self.down_queue = []

    def add_request(self, dest_floor):
        # Validation checks for given floor.
        if dest_floor < 0:
            print("The destination floor should be greater than 0")
            return
            
        elif dest_floor == self.current_floor:
            print(f"Elevator is {self.direction}")

        # Uses default Min-Heap behaviour to stop at lowest floor first.
        elif dest_floor > self.current_floor:
            heapq.heappush(self.up_queue, dest_floor)
        # Multiplies by -1 to trick heapq into acting as Max-heap.
        # This ensures the elavator stops at highest floor first when descending.
        else:
            heapq.heappush(self.down_queue, -dest_floor)

    def move(self):
        # Validation check for IDLE elevator.
        if self.direction == "IDLE":
            if len(self.up_queue) > 0:
                self.direction = "UP"

            elif len(self.down_queue) > 0:
                self.direction = "DOWN"

        if self.direction == "UP":
            self.current_floor = heapq.heappop(self.up_queue)
            self.display_building()

            # SCAN Algorithm: Continue UP until queue is empty, then evaluate next direction.
            if not len(self.up_queue):
                if not len(self.down_queue):
                    self.direction = "IDLE"
                else:
                    self.direction = "DOWN"

        elif self.direction == "DOWN":
            self.current_floor = heapq.heappop(self.down_queue) * -1
            self.display_building()
            if not len(self.down_queue):
                if not len(self.up_queue):
                    self.direction = "IDLE"
                else:
                    self.direction = "UP"


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