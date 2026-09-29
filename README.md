Iran Store Map Extractor
A Python-based data extraction workflow for collecting province-level retail and store location data in Iran from OpenStreetMap-compatible map sources.
This repository is a public portfolio version of the project. The full extraction logic is kept private because it may include operational scraping details, data-cleaning rules, and platform-sensitive implementation choices.
Project Overview
Iran Store Map Extractor helps collect structured store data by city, province, or national scope. The workflow is designed for market research, sales intelligence, retail coverage analysis, and province-level business mapping.
The tool extracts publicly available map records and prepares them in analysis-ready Excel or CSV format.
Key Features
- Province-based and city-based store extraction
- Support for all 31 provinces of Iran
- Extraction of store names, store categories, addresses, coordinates, brand fields, contact fields, and source links
- Persian-friendly output columns
- Excel and CSV export
- Duplicate handling based on map object IDs and location fields
- Suitable for business intelligence, sales territory mapping, and retail market research
Example Use Cases
- Building a retail store database by province
- Estimating market coverage in a selected city or region
- Preparing store lists for sales teams
- Mapping supermarkets, convenience stores, bakeries, dairies, wholesalers, malls, and similar retail categories
- Creating structured datasets for Power BI, Excel dashboards, or Python analysis
Data Fields
Field	Description
Store Name	Name of the store, when available
Store Type	Persian store category label
Shop Tag	Original OpenStreetMap shop category
Search Area	Selected city, province, or custom area
Province	Province field when available in source data
City	City field when available in source data
Address	Structured address assembled from available map tags
Phone	Public phone/contact field, when available
Website	Public website/contact field, when available
Brand	Store or product brand field, when available
Latitude	Geographic latitude
Longitude	Geographic longitude
OSM URL	Link to the original OpenStreetMap object
Source	Data source label
Scraped At	Extraction timestamp


Tech Stack
- Python
- Pandas
- Requests
- OpenPyXL
- OpenStreetMap / Overpass API
- Nominatim geocoding
Public Repository Contents
This public version includes:
- Project documentation
- Required Python packages
- Example output schema
- GitHub safety files
This public version does not include:
- Full extraction source code
- Private operational logic
- Large raw datasets
- API credentials, cookies, proxies, or local environment settings
Sample Output
A small synthetic sample is included in sample_output_schema.csv to show the output structure. It is not real scraped business data.
Installation
pip install -r requirements.txt
Usage
The private version supports workflows such as:
python iran_store_map_extractor.py --city "Tehran" --output tehran_stores.xlsx
python iran_store_map_extractor.py --province "East Azerbaijan" --output east_azerbaijan_stores.xlsx
python iran_store_map_extractor.py --iran --output iran_stores.xlsx
Privacy and Responsible Use
This project is intended for research, analytics, and business intelligence using publicly available map data. Users should respect the terms of service of data providers, avoid excessive automated requests, and verify important records before operational use.
OpenStreetMap is crowd-sourced, so coverage may be incomplete or inconsistent across regions.
Portfolio Note
I developed this workflow as part of my data collection, web scraping, and business analytics work. The project connects geospatial data extraction with practical market research needs, including province-level retail mapping and structured Excel outputs for analysis.
Author
Mona Faghfouri Azar
Data Analyst | Python Developer | Computational Social Science / NLP Researcher
