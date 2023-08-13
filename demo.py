import json
from bs4 import BeautifulSoup

with open('Amazon.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with the specified class
divs = soup.find_all('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')

# Initialize a list to store the data
data_list = []

# Process each div
for div in divs:
    link = title = rating = None

    # Find img with class="s-image"
    img_tag = div.find('img', class_='s-image')
    if img_tag:
        link = img_tag.get('src')

    # Find span with class="a-size-base-plus a-color-base a-text-normal"
    span_tag = div.find('span', class_='a-size-base-plus a-color-base a-text-normal')
    if span_tag:
        title = span_tag.text.strip()

    # Append the data to the list
    data_list.append({'link': link, 'title': title})

# Write the data to data.json
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

print("Data has been written to data.json successfully.")
