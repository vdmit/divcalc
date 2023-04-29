from divstructs import DivPayment


import divcore.div_tax_calc as dcalc
import divutils.misc_utils as dmisc

class TestDivCalc:
    def test_regular_payments(self):
        # regular payments (10% paid tax in USA, 3% rest to RF)
        pay1 = DivPayment(isin="US100500", country="USA", name="Horns and Hooves, LLC",
                          pay_sum=60.0, paid_tax_sum=6.0, pay_date="2021.05.20", currency="USD", final_sum=54.0)
        pay2 = DivPayment(isin="US9001", country="USA", name="Bells and Whistles Limited",
                          pay_sum=50.0, paid_tax_sum=5.0, pay_date="2021.05.20", currency="USD", final_sum=45.0)

        crep = dcalc.build_country_reports(country="USA", payments=[pay1, pay2])
        assert dmisc.is_equal_money_amount(crep.total_pay_sum, 110.0)
        assert dmisc.is_equal_money_amount(crep.total_rest_sum, 1.8 + 1.5)
        assert dmisc.is_equal_money_amount(crep.total_paid_tax_sum, 11.0)

    def test_reit_payments(self):
        # 30% tax
        pay1 = DivPayment(isin="US111", country="USA", name="Horns and Hooves REIT, LLC",
                          pay_sum=60.0, paid_tax_sum=18.0, final_sum=42.0, pay_date="2021.05.21", currency="USD")
        pay2 = DivPayment(isin="US222", country="USA", name="Bells and Whistles REIT Limited",
                          pay_sum=30.0, paid_tax_sum=9.0, final_sum=21.0, pay_date="2021.05.22", currency="USD")

        crep = dcalc.build_country_reports(country="USA", payments=[pay1, pay2])
        assert dmisc.is_equal_money_amount(crep.total_pay_sum, 90.0)
        assert dmisc.is_equal_money_amount(crep.total_rest_sum, 0.0)
        assert dmisc.is_equal_money_amount(crep.total_paid_tax_sum, 11.70)

    def test_different_payments(self):
        # 30% tax
        pay1 = DivPayment(isin="US111", country="USA", name="Horns and Hooves REIT, LLC",
                          pay_sum=60.0, paid_tax_sum=18.0, final_sum=42.0, pay_date="2021.05.21", currency="USD")

        # 10% tax
        pay2 = DivPayment(isin="US9001", country="USA", name="Bells and Whistles Limited",
                          pay_sum=50.0, paid_tax_sum=5.0, pay_date="2021.05.20", currency="USD", final_sum=45.0)

        crep = dcalc.build_country_reports(country="USA", payments=[pay1, pay2])
        assert dmisc.is_equal_money_amount(crep.total_pay_sum, 110.0)
        assert dmisc.is_equal_money_amount(crep.total_rest_sum, 1.5)
        assert dmisc.is_equal_money_amount(crep.total_paid_tax_sum, 12.80)






