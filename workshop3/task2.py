import heapq

def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  
    return heap[0]


if __name__ == '__main__':
    # Тест 1
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    try:
        assert(findKthLargest(nums, k)) == 5
        print('Тест 1 пройден')
    except:
        print('Тест 1 не пройден')
    
    # Тест 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    try:
        assert(findKthLargest(nums, k)) == 4
        print('Тест 2 пройден')
    except:
        print('Тест 2 не пройден')
        
    # Тест 3
    nums = [7, 10, 4, 3, 20, 15]
    k = 1
    try:
        assert(findKthLargest(nums, k)) == 20
        print('Тест 3 пройден')
    except:
        print('Тест 3 не пройден')