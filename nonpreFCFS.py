def fcfs():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        pid = input(f"Enter Process ID for P{i+1}: ")
        arrival = int(input(f"Enter Arrival Time for P{pid}: "))
        burst = int(input(f"Enter Burst Time for P{pid}: "))
        processes.append((pid, arrival, burst))

    processes.sort(key=lambda x: x[1])  # sort by arrival time

    current_time = 0
    total_wt = 0
    total_tat = 0
    start_times = []
    exec_order = []

    print("\n--- FCFS Scheduling ---")
    for pid, at, bt in processes:
        if current_time < at:
            current_time = at

        start = current_time
        finish = start + bt
        tat = finish - at
        wt = tat - bt

        total_tat += tat
        total_wt += wt
        exec_order.append(pid)
        start_times.append(start)

        current_time = finish

    # Gantt Chart
    print("Gantt Chart:")
    for pid in exec_order:
        print(f"| P{pid} ", end="")
    print("|")
    for t in start_times:
        print(f"{t:<5}", end="")
    print(current_time)

    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")

fcfs()