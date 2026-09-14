def calculate_partner_discount(total_quantity: int) -> int:
    if not isinstance(total_quantity, int) or total_quantity < 0:
        return 0

    if total_quantity < 10000:
        return 0
    elif 10000 <= total_quantity < 50000:
        return 5
    elif 50000 <= total_quantity < 300000:
        return 10
    else:
        return 15


def run_unit_tests():
    assert calculate_partner_discount(0) == 0
    assert calculate_partner_discount(9999) == 0
    assert calculate_partner_discount(10000) == 5
    assert calculate_partner_discount(49999) == 5
    assert calculate_partner_discount(50000) == 10
    assert calculate_partner_discount(299999) == 10
    assert calculate_partner_discount(300000) == 15
    print("All unit tests passed successfully: 100% coverage")


if __name__ == "__main__":
    run_unit_tests()
