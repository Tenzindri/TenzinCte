def create_index_table(arr, block_size):
    index_table = []
    print("\nIndex table created:")
    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))
        print(f"{arr[i]} -> {i}")
    return index_table
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
b_size = 3
idx_table = create_index_table(data, b_size)

