from typing import List


class CountryReportDetail:
    """
    Tax report detailed data (calc explaination)
    """

    def __init__(self, isin: str, pay_date: str, currency: str, pay_sum: float, is_fully_paid: bool,
                 paid_tax_sum: float, rest_sum: float):
        self.isin = isin
        self.pay_date = pay_date
        self.currency = currency
        self.pay_sum = pay_sum
        self.is_fully_paid = is_fully_paid
        self.paid_tax_sum = paid_tax_sum
        self.rest_sum = rest_sum

    @staticmethod
    def dump_header_to_string():
        return f"\n\tВ частности:\n\tISIN\tСумма выплаты\tУплаченный налог\tДоплата в ФНС РФ\tДата выплаты\tВалюта"

    def dump_to_string(self):
        return f"\t{self.isin}\t{self.pay_sum:.2f}\t{self.paid_tax_sum:.2f}\t{self.rest_sum:.2f}\t{self.pay_date}\t{self.currency}"


class CountryReport:
    """
    Tax report data for one country
    """

    def __init__(self, country: str, already_paid_count: int, total_pay_sum: float,
                 total_rest_sum: float, total_paid_tax_sum: float, details: List[CountryReportDetail]):
        assert country
        self.country = country
        self.already_paid_count = already_paid_count
        self.total_pay_sum = total_pay_sum
        self.total_paid_tax_sum = total_paid_tax_sum
        self.total_rest_sum = total_rest_sum
        self.details = details

    @staticmethod
    def dump_header_to_string():
        return "\t\tСумма выплат (всего)\tУплаченный налог (всего)\tДоплата в ФНС РФ (всего)"

    def dump_summary_to_string(self) -> str:
        return f"\t\t{self.total_pay_sum:.2f}\t{self.total_paid_tax_sum:.2f}\t{self.total_rest_sum:.2f}"
