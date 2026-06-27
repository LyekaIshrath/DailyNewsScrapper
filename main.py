import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage


url = "https://news.ycombinator.com/"


try:
    response = requests.get(url)
    response.raise_for_status()
    print("Website connected successfully!")
except Exception as e:
    print("Error connecting to website:")
    print(e)
    exit()


soup = BeautifulSoup(response.text, "html.parser")


titles = soup.select(".titleline")

headlines = []

for title in titles[:10]:

    headline = title.get_text(strip=True)

    link = title.find("a")["href"]
    
    if link.startswith("item?"):
        link = "https://news.ycombinator.com/" + link

    headlines.append((headline, link))


print("\nTop 10 Hacker News Headlines\n")

for i, (headline, link) in enumerate(headlines, start=1):

    print(f"{i}. {headline}")
    print(link)
    print("-" * 60)


sender = "lyeka016@gmail.com"
app_password = "ixhx yask zvfw ngci"

receivers = [
    "lyekaishrath123@gmail.com",
    "lyekaishrath06@gmail.com"
   
    
]


email = EmailMessage()

email["Subject"] = "Daily Tech Headlines"

email["From"] = sender

email["To"] = receivers

body = """
Hello,

Here are today's Top 10 Hacker News Headlines.

"""

for i, (headline, link) in enumerate(headlines, start=1):

    body += f"{i}. {headline}\n"
    body += f"{link}\n\n"

body += "Regards,\nDaily News Scraper"

email.set_content(body)


try:

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, app_password)

    server.send_message(email)
    print(f"Email sent successfully to {receivers}")

    server.quit()

except Exception as e:

    print("\nError Sending Email")

    print(e)
