# 🏢 Interactive Elevator System Simulator

An interactive, terminal-based simulation of an elevator system built in Python. This project demonstrates advanced algorithmic problem-solving by moving beyond basic First-In-First-Out (FIFO) queues to implement a dynamic **SCAN Scheduling Algorithm** using dual priority queues.

## 🚀 Features

*   **SCAN Scheduling Algorithm:** The elevator intelligently processes requests in its current direction of travel before reversing, preventing inefficient backtracking.
*   **Dual Priority Queues (Min/Max Heaps):** Utilizes Python's `heapq` module. The `up_queue` utilizes a Min-Heap, while the `down_queue` leverages a mathematical inversion trick to act as a Max-Heap.
*   **Real-Time Tick System:** A custom event-driven time loop allows users to inject new floor requests while the elevator is in transit, triggering on-the-fly route recalculations.
*   **Clean OOP Architecture:** High cohesion and encapsulation of state management, movement logic, and terminal rendering within an extensible `Elevator` class.

## 🛠️ Tech Stack

*   **Language:** Python 3.x
*   **Libraries:** `heapq` (Standard Library)
*   **Concepts:** Object-Oriented Programming, Heaps/Priority Queues, Event-Driven Loops.

## 💻 How to Run Locally

Because this project relies entirely on Python's standard library, there are no external dependencies or virtual environments required.

1. Clone the repository:
    git clone https://github.com/talhanadeem512/elevator-system-simulator.git

2. Navigate to the project directory:
    cd elevator-system-simulator

3. Run the master script:
    python3 main.py

## 🎮 How to Use the Simulation

The simulation runs on a "Tick-Based" time loop. Time is frozen until you explicitly advance it, allowing you to queue up multiple requests or interrupt the elevator mid-route.

*   **Request a floor:** Type a floor number (e.g., `8`) and press `ENTER`.
*   **Advance Time (Tick):** Leave the prompt blank and press `ENTER` to step the simulation forward by one move.
*   **Interrupt the Elevator:** While the elevator is moving to floor 8, type `4` and press `ENTER`. Advance time again to watch the priority queue intercept the new floor on the way!
*   **Exit:** Type `quit` and press `ENTER`.

## 🧠 Under the Hood: The Priority Queue Trick

By default, Python's `heapq` only creates **Min-Heaps** (popping the smallest number first). This works perfectly for an elevator going UP (e.g., stopping at 3 before 7). 

However, when the elevator goes DOWN, it needs to stop at the highest requested floors first (e.g., stopping at 7 before 3). To achieve this without writing a custom sorting algorithm, this engine multiplies down-requests by `-1` before pushing them to the heap, effectively turning the Min-Heap into a **Max-Heap**. The value is then multiplied by `-1` again upon popping to restore the true floor number.

## 🗺️ Future Roadmap

- [ ] **ElevatorController Class:** Implement a central load-balancing brain to manage multiple elevator shafts simultaneously.
- [ ] **Distance-Based Assignment:** Upgrade the multi-elevator assignment algorithm to dispatch the elevator physically closest to the requested floor.

---
*Developed by Talha Nadeem*
