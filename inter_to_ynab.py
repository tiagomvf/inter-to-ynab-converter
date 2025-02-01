import os
import csv
from datetime import datetime

# Create output directory if it doesn't exist
os.makedirs('output-files', exist_ok=True)

def convert_amount(amount_str):
    """Convert R$ 1.234,56 format to 1234.56"""
    # Handle negative amounts with non-breaking space
    amount_str = amount_str.replace('\xa0', ' ')
    amount_str = amount_str.replace('R$ ', '').strip()
    # Remove thousands separator and replace decimal comma
    amount_str = amount_str.replace('.', '').replace(',', '.')
    return float(amount_str)

def convert_date(date_str):
    """Convert DD/MM/YYYY to MM/DD/YYYY"""
    return datetime.strptime(date_str, '%d/%m/%Y').strftime('%m/%d/%Y')

def convert_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8-sig') as infile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile, delimiter=',')
        writer = csv.writer(outfile)
        
        # Write YNAB header
        writer.writerow(['Date', 'Payee', 'Memo', 'Amount'])
        
        for row in reader:
            date = convert_date(row['Data'])
            payee = row['Lançamento'].split('  ')[0]  # Get first part of description
            memo = row['Categoria']
            amount = convert_amount(row['Valor'])
            
            writer.writerow([date, '', payee, -amount])

def main():
    input_dir = 'input-files'
    output_dir = 'output-files'
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f'ynab_{filename}')
            convert_file(input_path, output_path)
            print(f'Converted {filename}')

if __name__ == '__main__':
    main()
