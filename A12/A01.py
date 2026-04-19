import threading
import random

def sum_even(numbers, result_dict):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    result_dict['even'] = even_sum

def sum_odd(numbers, result_dict):
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    result_dict['odd'] = odd_sum

if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Generated numbers = {numbers}")

    results = {}

    thread1 = threading.Thread(target=sum_even, args=(numbers, results))
    thread2 = threading.Thread(target=sum_odd, args=(numbers, results))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    total_sum = results['even'] + results['odd']
    print(f"Even sum = {results['even']}")
    print(f"Odd sum = {results['odd']}")
    print(f"Total sum = {total_sum}")