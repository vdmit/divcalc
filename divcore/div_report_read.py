from typing import List

import logging

from divstructs import DivPayment


def read_raw_tax_report_data(file_name) -> List[DivPayment]:
    payments = []
    with open(file_name) as report_fd:
        report_lines = report_fd.readlines()
        for index, line in enumerate(report_lines):
            if line.startswith("date") and index == 0:
                logging.info("skipping header")
                continue
            try:
                payment = DivPayment.parse_report_line(line)
                payments.append(payment)
            except Exception as exc:
                logging.error("Cannot parse line #%s: %s", index + 1, exc)
                raise

    logging.info("payments parsed: %s", len(payments))
    return payments
