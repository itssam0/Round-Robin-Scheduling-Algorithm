import time

# Processes and their burst times
processes = [{'id': 'P1', 'burst': 10},
             {'id': 'P2', 'burst': 4},
             {'id': 'P3', 'burst': 6}]

time_quantum = 2

# Function to simulate round-robin scheduling
def round_robin(processes, time_quantum):
    time_passed = 0
    waiting_times = {}
    turnaround_times = {}
    response_times = {}
    first_response = {}

    while processes:
        for process in list(processes):
            if process['burst'] > 0:
                run_time = min(time_quantum, process['burst'])
                if process['id'] not in first_response:
                    first_response[process['id']] = time_passed
                time_passed += run_time
                process['burst'] -= run_time
                print(f"Process {process['id']} runs from {time_passed - run_time} to {time_passed}")
                time.sleep(run_time * 0.1)
                if process['burst'] <= 0:
                    processes.remove(process)
                    turnaround_times[process['id']] = time_passed
                    print(f"Process {process['id']} finishes at time {time_passed}")
                    waiting_times[process['id']] = turnaround_times[process['id']] - process['burst']

    total_turnaround_time = sum(turnaround_times.values())
    total_response_time = sum(first_response.values())
    avg_turnaround_time = total_turnaround_time / len(turnaround_times)
    avg_response_time = total_response_time / len(first_response)
    
    print(f"Average turnaround time: {avg_turnaround_time}")
    print(f"Average response time: {avg_response_time}")

round_robin(processes, time_quantum)
