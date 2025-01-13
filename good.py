def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, k = map(int, input().split())  # n: total stars, k: threshold
        
        lucky_value = 0  # Initialize the lucky value
        segment_stack = [(1, n)]  # Stack of segments to process
        
        while segment_stack:
            l, r = segment_stack.pop()
            
            # If the segment length is less than k, we stop processing
            if r - l + 1 <= k:
                continue
            
            # Middle of the current segment
            m = (l + r) // 2
            
            # If the segment length is odd, we add m to the lucky value
            if (r - l + 1) % 2 == 1:
                lucky_value += m
            
            # Split the segment into two parts: [l, m-1] and [m+1, r]
            segment_stack.append((l, m - 1))  # Left part
            segment_stack.append((m + 1, r))  # Right part
        
        # Output the lucky value for the current test case
        print(lucky_value)

# Example usage
solve()
