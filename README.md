# Round-Robin-Scheduling-Algorithm
This repository contains an implementation of the Round Robin scheduling algorithm. The Round Robin algorithm is widely used in operating systems for process scheduling. 

## Overview
The Round Robin (RR) scheduling algorithm is one of the simplest and most commonly used CPU scheduling algorithms. It assigns a fixed time quantum to each process in the queue, allowing the system to switch between processes, ensuring that each one gets a fair share of the CPU time. This approach is particularly effective in time-sharing systems where it is crucial to prevent any single process from monopolizing the CPU.

## How It Works
- **Time Quantum:** A fixed time period, known as the time quantum, is assigned to each process. If a process does not complete within its allocated time quantum, it is preempted and placed at the end of the ready queue, and the CPU moves on to the next process.
- **Cycle:** The CPU cycles through the ready queue, giving each process a chance to execute for one time quantum. This continues until all processes are completed.
- **Fairness:** The algorithm ensures that all processes are treated equally by giving them the same amount of CPU time in a cyclic manner.

## Advantages
- **Fairness:** Each process gets an equal share of the CPU, preventing any process from being starved of CPU time.
- **Simple Implementation:** Round Robin is straightforward to implement and understand.
- **Good Responsiveness:** The algorithm can be tuned to improve response times by adjusting the length of the time quantum.

## Disadvantages
- **High Context Switching Overhead:** Frequent context switches can lead to high overhead, especially with a small time quantum.
- **Poor Turnaround Time for Long Processes:** Processes with longer burst times may experience poor turnaround time, as they are repeatedly preempted and placed back in the queue.
- **Inefficiency with Large Time Quantum:** If the time quantum is too large, Round Robin can behave similarly to First-Come, First-Served (FCFS), losing its advantage of fairness.

## Usage
To run the Round Robin scheduling simulation, clone the repository and execute the Python script:

```bash
git clone https://github.com/yourusername/round-robin-scheduling.git
cd round-robin-scheduling
python round_robin.py
