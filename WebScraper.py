import requests
from bs4 import BeautifulSoup

## Parse content
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

## Extract content 
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

## Extract job posting information
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

## Isolate for specific jobs (lambda looks at the text of each h2 element, converting it to lowercase and then checking if the substring python is present)
pyth_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

for job_element in pyth_jobs:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()