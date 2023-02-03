import prime_printer


def test_gen_2d_array():
    assert prime_printer.gen_2d_array(2, 2, [1, 2, 3, 4]) == [[1, 2], [3, 4]]
    assert prime_printer.gen_2d_array(3, 4, [1, 2, 3, 4, 5, 6]) == [[1, 2, 3, 4], [5, 6], []]
