import requests
from bs4 import BeautifulSoup

## Parse content
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

## Extract content 
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

## Extract job postings 
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()