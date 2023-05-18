import matplotlib.pyplot as plt
import collections
import json
countries = ['EGYPT',
             'UAE',
             'KSA',
             'LEBANON',
             'SUDAN',
             'TUNISIA',
             'JORDAN',
             'TURKEY',
             'KUWAIT',
             'QATAR',
             'IRAN',
             'ALGERIA',
             'BAHRAIN',
             'OMAN',
             'YEMEN',
             'MOROCCO',
             'IRAQ',
             'LIBYA',
             'SYRIA - TERRITORY (A)',
             'PALESTINE']


# Define the path to your JSON file
companies_file_path = 'dataset/companies.json'

# Open the file and load the contents as a Python object
with open(companies_file_path) as f:
    companies = json.load(f)

# Get provinces & cities of companies
company_provinces = []

for company in companies:
    for country in company['countries']:
        if country['name'] == 'EGYPT':
            for province in country['provinces']:
                if province['name'] not in company_provinces:
                    company_provinces.append(province['name'])

cairo_cities = []
alexandria_cities = []
giza_cities = []
dakahlia_cities = []
sharkia_cities = []

for company in companies:
    for country in company['countries']:
        if country['name'] == 'EGYPT':
            for province in country['provinces']:
                if province['name'] == "CAIRO":
                    for city in province['cities']:
                        if city['name'] not in cairo_cities:
                            cairo_cities.append(city['name'])

                if province['name'] == "ALEXANDRIA":
                    for city in province['cities']:
                        if city['name'] not in alexandria_cities:
                            alexandria_cities.append(city['name'])

                if province['name'] == "GIZA":
                    for city in province['cities']:
                        if city['name'] not in giza_cities:
                            giza_cities.append(city['name'])

                if province['name'] == "DAKAHLIA":
                    for city in province['cities']:
                        if city['name'] not in dakahlia_cities:
                            dakahlia_cities.append(city['name'])

                if province['name'] == "SHARKIA":
                    for city in province['cities']:
                        if city['name'] not in sharkia_cities:
                            sharkia_cities.append(city['name'])
