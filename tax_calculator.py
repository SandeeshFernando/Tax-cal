# ============================================
# SRI LANKAN TAX CALCULATOR PROJECT
# Session 04: Functions, Lambdas & Functional Programming
# ============================================
# Name: Sandeesh Fernando
# Date: _20 th feb to 25th feb 2026


def calculate_income_tax(annual_income):
    tax = 0

    if annual_income > 1_800_000:
        tax += (min(annual_income, 2_800_000) - 1_800_000) * 0.06

    if annual_income > 2_800_000:
        tax += (min(annual_income, 3_300_000) - 2_800_000) * 0.18

    if annual_income > 3_300_000:
        tax += (min(annual_income, 3_800_000) - 3_300_000) * 0.24

    if annual_income > 3_800_000:
        tax += (min(annual_income, 4_300_000) - 3_800_000) * 0.30

    if annual_income > 4_300_000:
        tax += (annual_income - 4_300_000) * 0.36

    return float(tax)


def calculate_effective_tax_rate(annual_income):
    if annual_income == 0:
        return 0.0
    return (calculate_income_tax(annual_income) / annual_income) * 100


def calculate_take_home(annual_income):
    return float(annual_income - calculate_income_tax(annual_income))


def print_taxpayer_details(income):
    tax = calculate_income_tax(income)
    effective_rate = calculate_effective_tax_rate(income)
    take_home = calculate_take_home(income)
    monthly_take_home = take_home / 12

    print(f"\nAnnual Income: Rs. {income:,.2f}")
    print(f"  Income Tax: Rs. {tax:,.2f} ({effective_rate:.2f}%)")
    print(f"  Take-Home (Annual): Rs. {take_home:,.2f}")
    print(f"  Take-Home (Monthly): Rs. {monthly_take_home:,.2f}")
    print("-" * 60)


def print_ranking(sorted_income_tax_pairs):
    for rank, (income, tax) in enumerate(sorted_income_tax_pairs, start=1):
        print(f"{rank}. Rs. {income:,.2f} - Tax Paid: Rs. {tax:,.2f}")


def print_high_earners(high_earner_incomes):
    for income in high_earner_incomes:
        tax = calculate_income_tax(income)
        print(f"Income: Rs. {income:,.2f} - Tax: Rs. {tax:,.2f}")


def main():
    incomes = [2500000, 4000000, 5000000, 1500000, 3500000]

    print("=" * 60)
    print("SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)")
    print("=" * 60)

    taxes = list(map(calculate_income_tax, incomes))

    high_earners = list(filter(lambda x: x >= 4_300_000, incomes))

    income_tax_pairs = list(zip(incomes, taxes))
    sorted_incomes_taxes = sorted(income_tax_pairs, key=lambda pair: pair[1], reverse=True)

    print("\n" + "=" * 60)
    print("DETAILED TAX REPORTS")
    print("=" * 60)
    for income in incomes:
        print_taxpayer_details(income)

    print("\n" + "=" * 60)
    print("TOP TAXPAYERS (Ranked by Tax Paid)")
    print("=" * 60)
    print_ranking(sorted_incomes_taxes)

    print("\n" + "=" * 60)
    print("HIGH EARNERS (>= Rs. 4,300,000 - Top Tax Bracket)")
    print("=" * 60)
    print_high_earners(high_earners)

    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)

    total_tax_revenue = sum(taxes)
    effective_rates = list(map(calculate_effective_tax_rate, incomes))
    average_effective_rate = sum(effective_rates) / len(effective_rates)
    highest_tax = max(taxes)
    lowest_tax = min(taxes)
    take_homes = list(map(calculate_take_home, incomes))
    avg_monthly_take_home = (sum(take_homes) / len(take_homes)) / 12

    print(f"Total Tax Revenue:        Rs. {total_tax_revenue:,.2f}")
    print(f"Average Effective Rate:   {average_effective_rate:.2f}%")
    print(f"Highest Tax Paid:         Rs. {highest_tax:,.2f}")
    print(f"Lowest Tax Paid:          Rs. {lowest_tax:,.2f}")
    print(f"Avg Monthly Take-Home:    Rs. {avg_monthly_take_home:,.2f}")


if __name__ == "__main__":
    main()
