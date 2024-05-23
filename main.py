import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = 'https://www.amazon.com/Instant-Pot-Electric-Sterilizer-Stainless/dp/B09MZTSSR2/ref=dp_fod_1?pd_rd_w=18bA5&content-id=amzn1.sym.68174014-ed7a-4e35-badd-6d3576b85c0b&pf_rd_p=68174014-ed7a-4e35-badd-6d3576b85c0b&pf_rd_r=PWK77FA0T57HPV6VVG94&pd_rd_wg=xB5CT&pd_rd_r=a43c717b-7ca5-4b04-b59d-6432dbc3968a&pd_rd_i=B09MZTSSR2&th=1'
HEADER = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
my_email = 'email@gmail.com'
password = 'qwerty'
to_email = ''

response = requests.get(url=AMAZON_URL, headers=HEADER)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
item_price = float(soup.find(name='span', class_='a-offscreen').text.lstrip('$'))
item_name = soup.find(name='span', id='productTitle').text.strip()

if item_price <= 100:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f'{item_name} is now ${item_price}\n{AMAZON_URL}'
        )


