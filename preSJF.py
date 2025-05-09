def sjf_preemptive():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        pid = input(f"Enter Process ID for P{i+1}: ")
        arrival = int(input(f"Enter Arrival Time for P{pid}: "))
        burst = int(input(f"Enter Burst Time for P{pid}: "))
        processes.append((pid, arrival, burst))

    remaining = [bt for _, _, bt in processes]
    complete = 0
    time = 0
    wt = [0] * n
    tat = [0] * n
    start_times = []
    exec_order = []

    print("\n--- Preemptive SJF (SRTF) ---")

    while complete != n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and remaining[i] > 0 and remaining[i] < min_bt:
                min_bt = remaining[i]
                idx = i

        if idx == -1:
            time += 1
            continue

        if not exec_order or exec_order[-1] != processes[idx][0]:
            exec_order.append(processes[idx][0])
            start_times.append(time)

        remaining[idx] -= 1
        time += 1

        if remaining[idx] == 0:
            complete += 1
            finish = time
            at = processes[idx][1]
            bt = processes[idx][2]
            tat[idx] = finish - at
            wt[idx] = tat[idx] - bt

    # Gantt Chart
    print("Gantt Chart:")
    for pid in exec_order:
        print(f"| P{pid} ", end="")
    print("|")
    for t in start_times:
        print(f"{t:<5}", end="")
    print(time)

    print(f"\nAverage Waiting Time: {sum(wt) / n:.2f}")
    print(f"Average Turnaround Time: {sum(tat) / n:.2f}")

sjf_preemptive()