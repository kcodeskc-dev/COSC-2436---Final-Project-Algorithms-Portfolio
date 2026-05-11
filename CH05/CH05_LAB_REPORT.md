# Lab 04: Quicksort

## Student Information
- **Name:** [Karla Cuevas]
- **Date:** [05/07/2026]

## Quicksort Concepts

### Divide and Conquer
[The array is divided into two sub-arrays by choosing a "pivot" element, one group is less than or equal to the pivot and the other is greater than the pivot. With smaller sub-problems it makes it easier to combine with the pivot after sorting.]

### The Three Steps
1. **Choose pivot:**
    [The pivot serves as a reference point to divide the array into smaller sub-arrays.]
2. **Partition:** 
    [The pivot and the other is greater than the pivot. With smaller sub-problems it makes it easier to combine with the pivot after sorting.]
3. **Recurse and combine:** 
    [Once both sub-arrays are sorted, they are combined with the pivot in between, forming a fully sorted array.]

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
[Initial Call: quicksort([3, 5, 2, 1, 4])
Pivot: 3
Less: [2, 1] (elements less than or equal to 3)
Greater: [5, 4] (elements greater than 3)
Recursively Call: quicksort([2, 1])
Pivot: 2
Less: [1] (elements less than or equal to 2)
Greater: [] (no elements greater than 2)
Base Case for quicksort([1])
Returns [1] because it's already sorted.
Result for quicksort([2, 1])
Combine: [1] + [2] + [] = [1, 2]
Recursively Call: quicksort([5, 4])
Pivot: 5
Less: [4] (elements less than or equal to 5)
Greater: [] (no elements greater than 5)
Base Case for quicksort([4])
Returns [4] because it's already sorted.
Result for quicksort([5, 4])
Combine: [4] + [5] + [] = [4, 5]
Final Result for quicksort([3, 5, 2, 1, 4])
Combine: [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | [nearly equal halves.achieving the logarithmic depth of recursive calls needed] |
| Average | O(n log n) | [ reasonably balanced and has same efficient recursive division observed in the best case] |
| Worst | O(n²) | [array is already sorted and the first element is chosen as the pivot every time.resulting in one side having zero elements.] |

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?

    [This would be known as a worst case. This causes one side of the partition to have zero elements, which can lead to linear number of recursive calls with each call processing every remaining element, leading to quadratic time complexity.]

2. How could you improve pivot selection to avoid worst-case performance?
    [using Median of Three rule which helps balancing the partitions and reduces the cance of getting to worse case]

3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?
    [quicksort averages (O(n \log n)) due to its efficient divide-and-conquer approach.]

4. Why do we use `array[1:]` instead of `array` when building the less and greater lists?
    [to exclude the pivot (which is the first element) from the partitioning process. This ensures that comparisons are made only with the elements after the pivot, allowing us to correctly build the sub-arrays of elements]
