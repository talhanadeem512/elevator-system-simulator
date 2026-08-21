class Elevator:
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.move_up_down = move_up_down
        self.doors = ['Closing', 'Opening']

        active_queue = [self.current_floor]
        up_queue = []
        down_queue = []

        def add_request(dest_floor):
            if dest_floor < 0:
                return "Floor must be greater than 0"
            if dest_floor > self.current_floor:
                up_queue.append(dest_floor)

            else:
                down_queue.append(dest_floor)

        def step():
            if self.current_floor in active_queue:
                print('Stopping')
                print(f"{self.doors[1]} the doors")

            else:
                print(f"{self.doors[0]} the doors")




