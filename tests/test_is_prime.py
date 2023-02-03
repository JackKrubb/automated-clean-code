import prime_printer


def test_is_prime():
    assert prime_printer.is_prime(1) is False
    assert prime_printer.is_prime(4) is False
    assert prime_printer.is_prime(5) is True
