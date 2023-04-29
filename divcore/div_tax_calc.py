from typing import List

from divstructs import CountryReportDetail
from divstructs import CountryReport
from divstructs import DivPayment


import logging


def build_country_reports(country: str, payments: List[DivPayment], tax_rate = 0.13) -> CountryReport:
    logging.info("processing payments for %s", country)
    already_paid_count = 0

    total_pay_sum = 0.0

    # not full, but up to 13%
    total_paid_tax_sum = 0.0
    total_rest_sum = 0.0

    details = []

    for pay in payments:
        rus_tax_sum = pay.pay_sum * tax_rate
        paid_tax_sum = pay.paid_tax_sum
        rus_rest_sum = rus_tax_sum - paid_tax_sum

        total_pay_sum += pay.pay_sum
        if rus_rest_sum > 0.0:
            total_rest_sum += rus_rest_sum
            total_paid_tax_sum += paid_tax_sum
            detail = CountryReportDetail(isin=pay.isin, currency=pay.currency, pay_date=pay.pay_date,
                                         paid_tax_sum=paid_tax_sum, rest_sum=rus_tax_sum,
                                         pay_sum=pay.pay_sum, is_fully_paid=False)

        else:
            total_rest_sum += 0.0
            total_paid_tax_sum += rus_tax_sum
            already_paid_count += 1
            paid_perc = paid_tax_sum * 100.0 / pay.pay_sum

            logging.info("payment %s (%s) is already done completely (paid: %.2f%%)", pay.name, pay.isin, paid_perc)
            detail = CountryReportDetail(isin=pay.isin, currency=pay.currency, pay_date=pay.pay_date,
                                         paid_tax_sum=pay.paid_tax_sum, rest_sum=0.0, pay_sum=pay.pay_sum,
                                         is_fully_paid=True)

        details.append(detail)


    country_report = CountryReport(country=country,
                                   already_paid_count=already_paid_count, total_pay_sum=total_pay_sum,
                                   total_paid_tax_sum=total_paid_tax_sum, total_rest_sum=total_rest_sum,
                                   details=details)
    return country_report
