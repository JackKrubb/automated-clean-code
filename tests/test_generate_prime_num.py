import prime_printer


def test_generate_prime_num():
    assert prime_printer.generate_prime_num(5) == [2, 3, 5, 7, 11]
    assert prime_printer.generate_prime_num(6) == [2, 3, 5, 7, 11, 13]
