"""
This scraper scrapes the summary precip data from the Walnut Gulch
Experimental Watershed Data Access Portal (dap).  The site is run
by the Southwest Watershed Research Center, part of the USDA's Agricultural
Research Service (ARS).
"""

from bs4 import BeautifulSoup
import requests

gage_loc_url = "https://www.tucson.ars.ag.gov/dap/gage_locations.asp"
precip_event_base_url = "https://www.tucson.ars.ag.gov/dap/eventh.asp"
raw_precipt_data_header = "Gage|Date|Time|Duration|Depth|Time_Est"

# Get the list of raingage ids
resp = requests.get(gage_loc_url)
soup = BeautifulSoup(resp.text, "html.parser")
gage_table = soup.findAll("table", attrs={"border": "0", "cellpadding": "0", "cellspacing": "10"})[0]
rows = gage_table.findAll("tr")

row_count = 0
gage_data = []
for row in rows:
    tds = row.findAll("td")
    values = [td.text for td in tds]
    if len(values) > 0:
        gage_data.append([item for item in values])

# This mimicks the form at https://www.tucson.ars.ag.gov/dap/event.asp
PRECIP_FORM = {
    'hiddenStartYear': '1953',
    'hiddenEndYear': '1999',
    'Watershed': '63',
    'gages': '1',
    'StartMonth': '1',
    'StartDay': '1',
    'StartYear': '1953',
    'EndMonth': '12',
    'EndDay': '31',
    'EndYear': '1999',
    'all': 'ON',
    'type': 'summary',
    'format': 'text',
    'sortby': 'sortby_gage',
    'units': 'inches',
    'MinDepth': '',
    'MaxDepth': '',
    'MinDuration': '',
    'MaxDuration': '',
    'submit': 'Submit'
}

# With the list of raingage ids and the html form template, run a post request against
# the DAP form link stored in precip_event_base_url.
#
# Save the resulting data to a text file.
if gage_data and len(gage_data) > 0:
    with open("rawprecip.csv", "w") as f:
        for gage in gage_data:
            ws = gage[0]
            rg = gage[1]
            if ws == '63':
                PRECIP_FORM['gages'] = rg
                resp = requests.post(precip_event_base_url, data=PRECIP_FORM)
                if resp.status_code == 200:
                    if "there was some error <br>No valid gages selected <br>" not in resp.text:
                        f.write(resp.text)

# The resulting precip.csv file comes with some header output and blank lines.
# Need to do some post-processing.
with open("rawprecip.csv", "r") as rpf:
    with open('precip.csv', 'w') as pf:
        pf.write(raw_precipt_data_header + "\n")
        data = rpf.readlines()
        for r in data:
            l = r.strip()
            if len(l) > 0:
                if l.startswith("SELECT") != True and l.startswith("#") != True and l.startswith("there was some error") != True:
                    l = l.replace(',', '|')
                    pf.write(l[0:-1] + "\n")