import divutils.misc_utils as dmisc


class DivPayment:
    def __init__(self, isin: str, pay_date: str, country: str, name: str,
                 currency: str, pay_sum: float, paid_tax_sum: float, final_sum: float):
        assert isin
        assert currency
        assert country
        assert name
        assert currency
        assert country
        self.isin = isin
        self.pay_date = pay_date
        self.currency = currency
        self.name = name
        self.country = country
        self.pay_sum = pay_sum
        self.paid_tax_sum = paid_tax_sum
        self.final_sum = final_sum

    @staticmethod
    def parse_report_line(report_line: str) -> 'DivPayment':
        # Tinkoff's foreign income report (PDF, XLS currently by support request)
        # date1:pay_date:type:name:isin:country:amount:per_one_pap:comission:before_tax:tax_paid:final_sum:currency
        # 0    :1       :2   :3   :4   :5      :6     :7          :8        :9         :10      :11       :12

        tokens = report_line.strip().split(":")
        fields_count = len(tokens)
        assert fields_count == 13, f"wrong tokens count: {fields_count}"

        pay_date = tokens[1]
        name = tokens[3]
        isin = tokens[4]
        country = tokens[5]
        raw_pay_sum = dmisc.parse_number(tokens[9])
        paid_tax_sum = dmisc.parse_number(tokens[10])
        final_sum = dmisc.parse_number(tokens[11])
        currency = tokens[12].upper()
        if currency != "USD":
            raise Exception("Currencies except USD are not currently supported. ")
        return DivPayment(isin=isin, pay_date=pay_date, currency=currency, name=name,
                          country=country, pay_sum=raw_pay_sum, paid_tax_sum=paid_tax_sum,
                          final_sum=final_sum)
