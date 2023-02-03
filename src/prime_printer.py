import math
from typing import List


def calculate_page(row_num: int, col_num: int, total_prime_num: int) -> int:
    prime_num_in_page = row_num * col_num
    number_of_pages = math.ceil(total_prime_num / prime_num_in_page)
    return number_of_pages


def is_prime(total_prime_num: int) -> bool:
    if total_prime_num <= 1:
        return False
    for i in range(2, total_prime_num):
        if total_prime_num % i == 0:
            return False
    return True


def generate_prime_num(total_prime_num: int) -> List[int]:
    list_of_prime = list()
    i = 0

    while len(list_of_prime) != total_prime_num:
        if len(list_of_prime) == total_prime_num:
            break
        if is_prime(i):
            list_of_prime.append(i)
        i += 1

    return list_of_prime


def gen_2d_array(num_row: int, num_col: int, list_of_prime: List[int]) -> List[List[int]]:
    test = [[] * num_col for _ in range(num_row)]
    k = 0
    for i in range(num_row):
        for _ in range(num_col):
            if k >= len(list_of_prime):
                break
            test[i].append(list_of_prime[k])
            k += 1
    return test


def print_page(row_num: int, col_num: int, total_prime_num: int):
    number_of_pages = calculate_page(row_num, col_num, total_prime_num)
    all_prime = generate_prime_num(total_prime_num)
    for page in range(number_of_pages):
        print("===Page ", page + 1, "===")
        num_of_prime_per_page = row_num * col_num
        prime_in_page = all_prime[:num_of_prime_per_page]
        twod_array = gen_2d_array(row_num, col_num, prime_in_page)
        for row in range(row_num):
            for num in twod_array[row]:
                print(f"{num}".rjust(5), end=" ")
                all_prime.remove(num)
            print()


print_page(5, 8, 50)
