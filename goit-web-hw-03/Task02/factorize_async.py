from time import time
import multiprocessing

def factorize(number):
    """Finds all factors of a given number."""
    factors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    return sorted(factors)

def process_number(number, result_queue):
    """Processes a number and puts the result in a queue."""
    result = factorize(number)
    result_queue.put(result)

def main():
    numbers = [128, 255, 99999, 10651060,20000000000000]
    result_queue = multiprocessing.Queue()
    processes = []

    # Create 4 processes
    for number in numbers:
        p = multiprocessing.Process(target=process_number, args=(number, result_queue))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    # Get the results from the queue
    results = [result_queue.get() for _ in range(len(numbers))]

    # print(results)...

if __name__ == "__main__":
    timer = time()
    main()
    print(f'Done bin async mode: {round(time() - timer, 8)}')