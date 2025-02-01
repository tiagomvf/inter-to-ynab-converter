# Inter Bank Statement to YNAB Converter

This project converts Inter Bank credit card statements into YNAB-compatible CSV format.

## Requirements
- Python 3.x
- CSV files from Inter Bank

## Usage

1. Place your Inter Bank statement CSV files in the `input-files/` directory
2. Run the conversion script:
```bash
python inter_to_ynab.py
```
3. Converted files will be saved in the `output-files/` directory with prefix `ynab_`

## File Structure

```
.
├── input-files/          # Original Inter Bank statements
│   ├── fatura-YYYY-MM.csv
├── output-files/         # Converted YNAB files
│   ├── ynab_fatura-YYYY-MM.csv
├── inter_to_ynab.py      # Conversion script
├── README.md             # This documentation
└── .gitignore            # Git ignore file
```

## Input File Format

Inter Bank statements should be in CSV format with the following columns:
- Data
- Descrição
- Valor

## Output File Format

YNAB-compatible CSV files will have the following columns:
- Date
- Payee
- Memo
- Amount

## Notes
- The script processes all CSV files in the input-files directory
- Original files remain unchanged
- Each converted file is saved with a `ynab_` prefix
