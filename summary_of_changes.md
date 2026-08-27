# Summary of Changes — Data Cleaning

**Dataset:** Sales Data (raw, synthetic — messy on purpose to practice cleaning)
**Rows before cleaning:** 128
**Rows after cleaning:** 120

## Steps performed

1. **Column headers** — renamed to lowercase, spaces replaced with underscores
   (e.g. `Order ID` → `order_id`).
2. **Duplicate rows** — 8 exact duplicate rows found and removed using
   `drop_duplicates()`.
3. **Missing values**
   - `age` (12 missing) → filled with the median age
   - `price` (3 missing) → filled with the median price
   - `gender` (5 missing) → filled with `"Unknown"`
   - `country` (7 missing) → filled with `"Unknown"`
4. **Standardizing text values**
   - `gender` — collapsed spellings like `M`, `male`, `MALE` → `Male`
     (same for Female)
   - `country` — collapsed spellings like `india`, `INDIA`, `Bharat` → `India`
     (same pattern for USA, UK, Australia)
5. **Date formatting** — `order_date` had mixed formats
   (`dd-mm-yyyy` and `mm/dd/yyyy`); all converted to one consistent
   `dd-mm-yyyy` format.
6. **Data types fixed**
   - `age`, `quantity`, `order_id` → converted to whole numbers (int)
   - `order_date` → parsed as a real date before being written back out
     as text in the standard format

## Result

A clean dataset (`cleaned_sales_data.csv`) with no missing values,
no duplicate rows, consistent text values, and one consistent date format —
ready for analysis or visualization.
