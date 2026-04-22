# Task 4 & 5: Implement Indexed Search
def create_index_table(arr, block_size):
    index_table = []
    print("\nIndex table created:")
    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))
        
    return index_table

def indexed_search(arr, index_table, key):
    print(f"\nSearch key: {key}")
    
    imin = 0
    imax = len(arr) - 1
    found_range = False

    # 1. Search index table to determine range
    for i in range(len(index_table)):
        # Check if the key is within the current block or the last block
        current_val, current_idx = index_table[i]
        
        if key >= current_val:
            imin = current_idx
            # Determine imax based on the next entry in the index table
            if i + 1 < len(index_table):
                imax = index_table[i+1][1] - 1
                next_val = index_table[i+1][0]
                if key < next_val:
                    print(f"Index range found:\n{current_val} <= {key} < {next_val}")
                    found_range = True
                    break
            else:
                # We are in the last block
                imax = len(arr) - 1
                print(f"Index range found:\n{current_val} <= {key}")
                found_range = True
                break

    if not found_range and key < index_table[0][0]:
        print(f"Key is smaller than the first element.")
        return -1

    # 2. Search sequentially inside the range
    print(f"Searching from index {imin} to index {imax}:")
    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i
            
    print(f"{key} not found")
    return -1

# --- Testing the Implementation ---


# Testing Tasks 4, & 5
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
b_size = 3
idx_table = create_index_table(data, b_size)

# Task 4: Key exists
indexed_search(data, idx_table, 45)

# Task 5: Key does not exist
indexed_search(data, idx_table, 43)