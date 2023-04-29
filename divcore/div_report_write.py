import logging
from typing import List

from divstructs import CountryReport
from divstructs import CountryReportDetail


def dump_country_reports(country_reports: List[CountryReport], file_name: str, add_details: bool):
    logging.info("saving report to %s", file_name)
    with open(file_name, "w+") as out_fd:

        out_fd.write("Выплаты по дивидендам иностранных компаний\n")
        out_fd.write("\n")

        for crep in country_reports:
            out_fd.write(f"Страна: {crep.country}\n")
            out_fd.write(CountryReport.dump_header_to_string() + "\n")
            out_fd.write(crep.dump_summary_to_string() + "\n")
            if add_details:
                out_fd.write(CountryReportDetail.dump_header_to_string() + "\n")
                for detail in sorted(crep.details, key=lambda dt: (dt.isin, dt.pay_date)):
                    out_fd.write(detail.dump_to_string() + "\n")

            out_fd.write("\n")

