##API seems broken

import requests
from datetime import datetime, timedelta

API_KEY = 'hP0BPN1dSJ4PUChECrkaEA6Tk6yOotbPC1PqQf08'  # Replace with your actual API key
ITEMS_PER_PAGE = 50  # Max allowed by API
MAX_NUMBERS = 100
output_file = 'dnc_numbers.txt'

def fetch_complaints(created_date_from, created_date_to):
    url = (
        f"https://api.ftc.gov/v0/hsr-early-termination-notices?api_key="
        f"?api_key={API_KEY}"
        f"&items_per_page={ITEMS_PER_PAGE}"
        f"&created_date_from=\"{created_date_from}\""
        f"&created_date_to=\"{created_date_to}\""
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    # Get complaints from the last 30 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    # Format dates for API
    created_date_from = start_date.strftime("%Y-%m-%d %H:%M:%S")
    created_date_to = end_date.strftime("%Y-%m-%d %H:%M:%S")
    
    phone_numbers = set()  # Use set to avoid duplicates
    
    try:
        data = fetch_complaints(created_date_from, created_date_to)
        complaints = data.get('data', [])
        
        for item in complaints:
            number = item.get('attributes', {}).get('company-phone-number')
            if number and len(phone_numbers) < MAX_NUMBERS:
                phone_numbers.add(number)
                
        # Write numbers to file
        with open(output_file, 'w') as f:
            for number in phone_numbers:
                f.write(number + '\n')
                
        print(f"Done! {len(phone_numbers)} unique phone numbers saved to {output_file}")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == '__main__':
    main()
