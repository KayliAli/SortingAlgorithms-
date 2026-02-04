# Sorting Algorithms

This repository contains implementations of common sorting algorithms written in **Python**.
Each algorithm is implemented for educational purposes to demonstrate different sorting techniques
and their performance characteristics.

## Algorithms Included

- **Selection Sort**  
  Repeatedly selects the minimum element from the unsorted portion and places it at the beginning.

- **Bubble Sort**  
  Repeatedly swaps adjacent elements if they are in the wrong order.

- **Merge Sort**  
  A divide-and-conquer algorithm that splits the array, sorts each half, and merges them back together.

- **Quick Sort**  
  A divide-and-conquer algorithm that selects a pivot and partitions the array around it.

- **Radix Sort**  
  Sorts numbers digit by digit starting from the least significant digit.

- **Heap Sort**  
  Uses a binary heap data structure to repeatedly extract the maximum or minimum element.

- **Bucket Sort**  
  Distributes elements into buckets, sorts each bucket, and then combines them.

- **Bogo Sort**  
  Randomly shuffles the array until it becomes sorted (inefficient and impractical).

- **Insertion Sort**  
  Builds the sorted array one element at a time by inserting elements into their correct position.

- **Counting Sort**  
  Counts occurrences of each value and uses this information to place elements in order.

- **Shake Sort (Cocktail Sort)**  
  A variation of Bubble Sort that traverses the list in both directions.

- **Stooge Sort**  
  A recursive sorting algorithm with extremely poor performance, mainly used for academic interest.

## Time & Space Complexity

| Algorithm       | Best Case | Average Case | Worst Case | Space Complexity |
|-----------------|-----------|--------------|------------|------------------|
| Selection Sort  | O(n²)     | O(n²)        | O(n²)      | O(1)             | 
| Bubble Sort     | O(n)      | O(n²)        | O(n²)      | O(1)             |
| Merge Sort      | O(n log n)| O(n log n)   | O(n log n) | O(n)             | 
| Quick Sort      | O(n log n)| O(n log n)   | O(n²)      | O(log n)         | 
| Radix Sort      | O(nk)     | O(nk)        | O(nk)      | O(n + k)         | 
| Heap Sort       | O(n log n)| O(n log n)   | O(n log n) | O(1)             | 
| Bucket Sort     | O(n + k)  | O(n + k)     | O(n²)     | O(n)              | 
| Bogo Sort       | O(n)      | O((n+1)!)    | O(∞)       | O(1)             | 
| Insertion Sort  | O(n)      | O(n²)        | O(n²)      | O(1)             | 
| Counting Sort   | O(n + k)  | O(n + k)     | O(n + k)  | O(k)              | 
| Shake Sort      | O(n)      | O(n²)        | O(n²)     | O(1)              | 
| Stooge Sort     | O(n^2.7)  | O(n^2.7)     | O(n^2.7)  | O(n)              | 

> n = number of elements  
> k = range of input values or number of digits


## Purpose

This repository is intended for learning and comparing sorting algorithms,
focusing on their logic and time complexity rather than production-level performance.

## How to Run

### Requirements
- Python 3.8 or higher


### Run the Application
All sorting algorithms are executed from a single entry point.

```bash
python main.py
```
### Notes
- Algorithms are implemented as pure functions.
- Each algorithm works on a copy of the input array.
- This project is intended for educational purposes.

