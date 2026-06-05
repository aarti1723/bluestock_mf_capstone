\# Data Dictionary



\## dim\_fund



| Column | Type | Description |

|----------|----------|----------|

| amfi\_code | Integer | Unique AMFI scheme code |

| fund\_house | Text | Fund house name |

| scheme\_name | Text | Mutual fund scheme name |

| category | Text | Equity or Debt |

| sub\_category | Text | Fund sub-category |



\---



\## fact\_nav



| Column | Type | Description |

|----------|----------|----------|

| amfi\_code | Integer | Scheme code |

| date | Date | NAV date |

| nav | Float | Net Asset Value |



\---



\## fact\_transactions



| Column | Type | Description |

|----------|----------|----------|

| investor\_id | Text | Investor identifier |

| transaction\_date | Date | Transaction date |

| amfi\_code | Integer | Scheme code |

| transaction\_type | Text | SIP, Lumpsum, Redemption |

| amount\_inr | Float | Transaction amount |



\---



\## fact\_performance



| Column | Type | Description |

|----------|----------|----------|

| amfi\_code | Integer | Scheme code |

| return\_1yr\_pct | Float | 1-year return |

| return\_3yr\_pct | Float | 3-year return |

| return\_5yr\_pct | Float | 5-year return |

| expense\_ratio\_pct | Float | Expense ratio |



\---



\## fact\_aum



| Column | Type | Description |

|----------|----------|----------|

| fund\_house | Text | Fund house |

| date | Date | Reporting date |

| aum\_crore | Float | Assets Under Management |

