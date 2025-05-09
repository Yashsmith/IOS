def first_fit(blocks, processes):
    allocated = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocated[i] = j
                blocks[j] -= processes[i]  # Allocate the block
                break
    print("\n--- First Fit ---")
    for i in range(len(processes)):
        print(f"Process {i+1} (Size {processes[i]}) -> Block {allocated[i] + 1 if allocated[i] != -1 else 'Not Allocated'}")


def best_fit(blocks, processes):
    allocated = [-1] * len(processes)
    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_idx == -1 or blocks[best_idx] > blocks[j]:
                    best_idx = j
        if best_idx != -1:
            allocated[i] = best_idx
            blocks[best_idx] -= processes[i]  # Allocate the block
    print("\n--- Best Fit ---")
    for i in range(len(processes)):
        print(f"Process {i+1} (Size {processes[i]}) -> Block {allocated[i] + 1 if allocated[i] != -1 else 'Not Allocated'}")


def worst_fit(blocks, processes):
    allocated = [-1] * len(processes)
    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_idx == -1 or blocks[worst_idx] < blocks[j]:
                    worst_idx = j
        if worst_idx != -1:
            allocated[i] = worst_idx
            blocks[worst_idx] -= processes[i]  # Allocate the block
    print("\n--- Worst Fit ---")
    for i in range(len(processes)):
        print(f"Process {i+1} (Size {processes[i]}) -> Block {allocated[i] + 1 if allocated[i] != -1 else 'Not Allocated'}")


# ----------------------------
# 📥 User Input
# ----------------------------
blocks_input = input("Enter block sizes (space-separated): ")
blocks = list(map(int, blocks_input.strip().split()))

processes_input = input("Enter process sizes (space-separated): ")
processes = list(map(int, processes_input.strip().split()))

first_fit(blocks.copy(), processes)
best_fit(blocks.copy(), processes)
worst_fit(blocks.copy(), processes)