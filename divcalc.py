#!/usr/bin/env python3

import argparse
import logging
from collections import defaultdict

from divutils.misc_utils import configure_logger

import divcore.div_tax_calc as dcalc
import divcore.div_report_read as dread
import divcore.div_report_write as dwrite
import divcore.div_stat_calc as dstat


def parse_args():
    parser = argparse.ArgumentParser(description="Dividend tax calculator")
    parser.add_argument("-i", "--input", required=True, help="Input report file (.csv)")
    parser.add_argument("-o", "--output", required=True, help="Output report file (.csv)", default="out-tax-report.csv")

    parser.add_argument("-d", "--detailed", action="store_true", help="Add details to output")
    parser.add_argument("-r", "--tax-rate", type=float, help="Tax rate", required=True)

    return parser.parse_args()


# MAX_USD = 77.7730


def main():
    configure_logger()
    cli_args = parse_args()

    in_report_file_name = cli_args.input
    out_report_file_name = cli_args.output

    tax_rate = cli_args.tax_rate

    all_payments = dread.read_raw_tax_report_data(in_report_file_name)

    dstat.build_total_stats(all_payments)
    dstat.build_div_stats(all_payments)

    payments_by_country = defaultdict(list)
    for pay in all_payments:
        payments_by_country[pay.country].append(pay)

    logging.info("countries: %s", len(payments_by_country))

    country_reports = []
    for country, payments in payments_by_country.items():
        logging.info("country: %s", country)

        crep = dcalc.build_country_reports(country=country, payments=payments, tax_rate=tax_rate)
        country_reports.append(crep)

    dwrite.dump_country_reports(country_reports=country_reports, file_name=out_report_file_name,
                                add_details=cli_args.detailed)



if __name__ == "__main__":
    main()
