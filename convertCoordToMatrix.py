import requests
from bs4 import BeautifulSoup

def decode_google_doc(url):
    # Fetch HTML content
    response = requests.get(url) 
    if response.status_code != 200:
        print(f"Failed to fetch the document. Status code: {response.status_code}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')  

    # Extract the table data
    table_data = []
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')  # find all rows in the table
        for row in rows[1:]:  # skip header
            cells = row.find_all('td')  # find cells
            if len(cells) == 3:
                # Get x,char,y
                x = int(cells[0].get_text(strip=True))
                char = cells[1].get_text(strip=True)
                y = int(cells[2].get_text(strip=True))
                table_data.append((x,y,char))  # Store as (x,y,char)
    
    # Grid max size
    max_x = max(data[0] for data in table_data) 
    max_y = max(data[1] for data in table_data)

    # Dictionary for lookup of characters at x,y
    character_positions = {
    (x, y): char
    for x, y, char in table_data
}

    # Iterate over y,x
    for y in range(max_y, -1, -1):
        for x in range(max_x + 1):
            # Print the char at x,y or ' '
            print(character_positions.get((x, y), ' '), end='')
        if y > 0:
            print("")
"""  
    We receive (x,y) coordinate values from the document where: X = columns and Y = rows (grows upwards)
        (0,2) (1,2) (2,2)
        (0,1) (1,1) (2,1)
     y  (0,0) (1,0) (2,0)
        x
    but the computer prints like a matrix where: X = rows (grows downwards) and Y = columns
        y
    x   a00 a01 a02 
        a10 a11 a12
        a20 a21 a22
     ...
     therefore: we must invert rows and columns and invert Y
    """

url2 = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53erafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub"
decode_google_doc(url)
# Fetch and parse HTML content; extract data from the table; create a dictionary with the data; print the chars while inverting rows and columns, and inverting Y.