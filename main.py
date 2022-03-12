from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.kabum.com.br/produto/113405/monitor-gamer-lg-25-ips-ultra-wide-75-hz-full-hd-99-srgb-hdmi-vesa-25um58-g?gclid=CjwKCAiAprGRBhBgEiwANJEY7OYrrg2_AvfSHZrC1rOEnu1bbV4HvC59usmTerlTAfz_uncvCPbRNRoCEusQAvD_BwE"
headers = {
    "User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64; rv:98.0)Gecko/20100101 Firefox/98.0",
    "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3"
}
response = requests.get(url=URL, headers=headers)
response.raise_for_status()
data_site = response.text

soup = BeautifulSoup(data_site, "html.parser")

#getting the price
price = soup.select("h4.sc-jWaEpP")
price_text = []
for text in price:
    pt = str(text.get_text())
    price_text.append(pt)
pricet = (price_text[0])
formated_price = float(pricet.split("$")[1].replace("\xa0","").replace(",",""))

#getting the name of the product
name_product = soup.select("h1.sc-hmvnCu")
name_text = ""
for text in name_product:
    pt = str(text.get_text())
    name_text = pt

# send a email when the price is below the target
if formated_price < 1.000:
    email = "xxxxxxxxx"
    password = "xxxxxxxxx"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="",
                            msg=f"Subject:{name_text} is chearp \n\n"
                                f"The product is below you price targe {formated_price}"
                            )

