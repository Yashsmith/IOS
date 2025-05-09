def fifo_page_replacement(pages, frame_size):
    memory = []
    page_faults = 0
    page_hits = 0
    next_to_replace = 0

    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) < frame_size:
                memory.append(page)
            else:
                memory[next_to_replace] = page
                next_to_replace = (next_to_replace + 1) % frame_size
        print(f"Page: {page} -> Memory: {memory} | {'' if page in memory else ''}")
    
    print(f"\nFIFO - Page Faults: {page_faults}, Page Hits: {page_hits}\n")


def lru_page_replacement(pages, frame_size):
    memory = []
    page_faults = 0
    page_hits = 0

    for page in pages:
        if page in memory:
            page_hits += 1
            memory.remove(page)
            memory.append(page)
        else:
            page_faults += 1
            if len(memory) < frame_size:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        print(f"Page: {page} -> Memory: {memory} | {'' if page in memory else ''}")
    
    print(f"\nLRU - Page Faults: {page_faults}, Page Hits: {page_hits}\n")


def optimal_page_replacement(pages, frame_size):
    memory = []
    page_faults = 0
    page_hits = 0

    for i in range(len(pages)):
        current_page = pages[i]
        if current_page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) < frame_size:
                memory.append(current_page)
            else:
                # Predict future use
                future_indices = []
                for page in memory:
                    if page in pages[i+1:]:
                        future_indices.append(pages[i+1:].index(page))
                    else:
                        future_indices.append(float('inf'))
                index_to_replace = future_indices.index(max(future_indices))
                memory[index_to_replace] = current_page
        print(f"Page: {current_page} -> Memory: {memory} | {'' if current_page in memory else ''}")
    
    print(f"\nOptimal - Page Faults: {page_faults}, Page Hits: {page_hits}\n")


# ----------------------------
# 📥 User Input
# ----------------------------
pages_input = input("Enter page reference string (space-separated): ")
pages = list(map(int, pages_input.strip().split()))
frame_size = int(input("Enter number of memory frames: "))

print("\n--- FIFO ---")
fifo_page_replacement(pages, frame_size)

print("--- LRU ---")
lru_page_replacement(pages, frame_size)

print("--- Optimal ---")
optimal_page_replacement(pages, frame_size)