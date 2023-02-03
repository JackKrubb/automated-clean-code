import prime_printer


def test_calculate_page():
    assert prime_printer.calculate_page(2, 2, 4) == 1
    assert prime_printer.calculate_page(2, 2, 9) == 3
