import logging


def is_equal_money_amount(a, b) -> bool:
    return round(a, 2) == round(b, 2)


def parse_number(num_str) -> float:
    if num_str.count(",") != 1:
        raise Exception(f"Wrong sum: '{num_str}' (expected US format: 28,70)")
    num_fixed = num_str.replace(",", ".")
    return float(num_fixed)


def configure_logger():
    level = logging.INFO
    logging.basicConfig(format='[%(levelname)s:%(process)d] %(asctime)s - %(message)s', level=level)
