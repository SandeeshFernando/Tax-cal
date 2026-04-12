# 🇱🇰 Sri Lankan Tax Calculator

A Python-based income tax calculator built around **Sri Lanka's April 2025 tax reforms**. This project demonstrates the use of **functions, lambdas, and functional programming** concepts (`map`, `filter`, `zip`, `sorted`) to compute progressive income tax across multiple taxpayers.

---

## 📋 Tax Brackets (2025 Reforms)

| Income Range (Rs.)         | Tax Rate |
| -------------------------- | -------- |
| Up to 1,800,000            | 0%       |
| 1,800,001 – 2,800,000     | 6%       |
| 2,800,001 – 3,300,000     | 18%      |
| 3,300,001 – 3,800,000     | 24%      |
| 3,800,001 – 4,300,000     | 30%      |
| Above 4,300,000            | 36%      |

---

## ✨ Features

- **Progressive Tax Calculation** — Accurately computes income tax using Sri Lanka's multi-slab system.
- **Effective Tax Rate** — Shows the actual percentage of income paid as tax.
- **Take-Home Pay** — Calculates annual and monthly take-home income after tax.
- **Taxpayer Ranking** — Ranks multiple taxpayers by total tax paid (highest to lowest).
- **High Earner Detection** — Filters and displays individuals in the top tax bracket (≥ Rs. 4,300,000).
- **Summary Statistics** — Aggregated metrics including total tax revenue, average effective rate, and average monthly take-home pay.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+** (uses f-strings and numeric underscores)

### Run the Calculator

```bash
python tax_calculator.py
```

---

## 📂 Project Structure

```
Tax-cal/
├── tax_calculator.py   # Main application with all tax logic and reporting
└── README.md           # Project documentation
```

---

## 📖 How It Works

The calculator processes a list of sample annual incomes and generates:

1. **Detailed Tax Reports** — Per-taxpayer breakdown of income, tax, effective rate, and take-home pay.
2. **Top Taxpayers** — All taxpayers ranked by tax contribution.
3. **High Earners List** — Taxpayers falling in the highest tax bracket.
4. **Summary Statistics** — Aggregated figures across all taxpayers.

### Sample Output

```
============================================================
SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)
============================================================

============================================================
DETAILED TAX REPORTS
============================================================

Annual Income: Rs. 2,500,000.00
  Income Tax: Rs. 42,000.00 (1.68%)
  Take-Home (Annual): Rs. 2,458,000.00
  Take-Home (Monthly): Rs. 204,833.33
------------------------------------------------------------
...
```

---

## 🧠 Concepts Demonstrated

| Concept              | Usage                                                  |
| -------------------- | ------------------------------------------------------ |
| **Functions**        | Modular tax calculation, reporting, and formatting      |
| **Lambda Functions** | Inline filtering for high earners, sorting by tax paid  |
| **`map()`**          | Applying tax and take-home calculations across incomes  |
| **`filter()`**       | Extracting high earners from the income list            |
| **`zip()`**          | Pairing incomes with their computed taxes               |
| **`sorted()`**       | Ranking taxpayers by tax contribution                   |

---

## 👤 Author

**Sandeesh Fernando**

---

## 📄 License

This project is open source and available for educational use.