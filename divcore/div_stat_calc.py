import logging

from collections import defaultdict


def build_total_stats(payments):
    total_pay_sum = 0.0
    total_paid_tax_sum = 0.0
    total_final_sum = 0.0
    for pay in payments:
        total_pay_sum += pay.pay_sum
        total_paid_tax_sum += pay.paid_tax_sum
        total_final_sum += pay.final_sum
    logging.info("total pay_sum: %.2f", total_pay_sum)
    logging.info("total paid_tax_sum: %.2f", total_paid_tax_sum)
    logging.info("total final_sum: %.2f", total_final_sum)


def build_div_stats(payments):
    payments_by_isin = defaultdict(float)
    for pay in payments:
        payments_by_isin[pay.isin] += pay.final_sum

    logging.info("overall dividend stats (by final payment, top-10):")
    for isin, final_sum in sorted(payments_by_isin.items(), key=lambda x: -x[1])[:10]:
        logging.info("isin %s total sum: %.2f", isin, final_sum)
