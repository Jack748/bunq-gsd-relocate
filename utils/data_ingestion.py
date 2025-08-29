import requests
from bs4 import BeautifulSoup

def get_country_specific_info(country):
    """
    Fetch country-specific information based on the provided country name.

    Args:
        country (str): The name of the country.

    Returns:
        dict: A dictionary containing information about health insurance, bank accounts, and housing.
    """
    if country.lower() == "netherlands":
        return fetch_netherlands_info()
    else:
        return {
            "health_insurance": "No information available",
            "bank_account": "No information available",
            "housing": "No information available"
        }

def fetch_netherlands_info():
    """
    Fetch information specific to the Netherlands from government websites.

    Returns:
        dict: A dictionary containing information about health insurance, bank accounts, and housing.
    """
    try:
        # Fetch health insurance information
        health_insurance_url = "https://www.government.nl/topics/health-insurance"
        health_insurance_info = fetch_information(health_insurance_url)

        # Fetch bank account information
        bank_account_url = "https://www.government.nl/topics/identification-documents"
        bank_account_info = fetch_information(bank_account_url)

        # Fetch housing information
        housing_url = "https://www.government.nl/topics/housing"
        housing_info = fetch_information(housing_url)

        return {
            "health_insurance": health_insurance_info,
            "bank_account": bank_account_info,
            "housing": housing_info
        }
    except requests.RequestException as e:
        print(f"Error fetching Netherlands information: {e}")
        return {
            "health_insurance": "No information available",
            "bank_account": "No information available",
            "housing": "No information available"
        }

def fetch_information(url):
    """
    Fetch information from a given URL using BeautifulSoup.

    Args:
        url (str): The URL to fetch information from.

    Returns:
        str: The fetched information.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('div', class_='content').text.strip()

if __name__ == "__main__":
    # Test the function
    country_info = get_country_specific_info("Netherlands")
    print(country_info)