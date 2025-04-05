import requests
import xml.etree.ElementTree as ET
import xml.dom.minidom

base_url = "https://wits.worldbank.org/API/V1/wits/datasource/trn/country/ALL"


response = requests.get(base_url)


xml_data = response.content

namespace = {'wits': 'http://wits.worldbank.org'}
root = ET.fromstring(xml_data)

# Extracting the countries
for country in root.findall('.//wits:country', namespace):
    country_code = country.attrib['countrycode']
    iso3_code = country.find('wits:iso3Code', namespace).text
    name = country.find('wits:name', namespace).text
    print(f"Country Name: {name}")
    print(f"Country Code: {country_code}")
    print(f"ISO3 Code: {iso3_code}")
    print('-' * 30)
