import requests
import csv
import os
import requests

def downloadTLE(NORAD_ID):
    """
    Downloads the Two-Line Elements (TLE) data for a given NORAD ID from Celestrak.
    
    Args:
        NORAD_ID (int): The NORAD ID of the satellite.
    """
    url = f"https://celestrak.org/NORAD/elements/gp.php?CATNR={NORAD_ID}&FORMAT=tle"
    path = "./TLEs/"
    
    os.makedirs(path, exist_ok=True)

    filename = f"{path}{NORAD_ID}.txt"
    response = requests.get(url)
    if response.content.decode("utf-8") == "No GP data found":
        print(f"***** No TLE data found for NORAD ID: {NORAD_ID}")
        return    
    with open(filename, "wb") as file:
        file.write(response.content)

def read_norad_ids_from_csv(file_path):
    """
    Reads NORAD IDs from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        list: A list of NORAD IDs.
    """
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        next(reader, None)
        norad_ids = []
        for row in reader:
            norad_id = int(float(row['NORAD Number']))
            norad_ids.append(norad_id)
    return norad_ids

# Example usage
file_path = './filtered_UCS-Satellite-Database-5-1-2023.csv'
norad_ids = read_norad_ids_from_csv(file_path)

for norad_id in norad_ids[:3]: # test with 3 satellites first.
    print(f"Downloading TLE for NORAD ID: {norad_id}")
    downloadTLE(norad_id)