import requests
import pandas as pd
import matplotlib.pyplot as plt

#Obtain Data from api
live_confirmed_cases = requests.get('https://api.covid19api.com/dayone/country/singapore/status/confirmed/live')
live_recovered_cases = requests.get('https://api.covid19api.com/dayone/country/singapore/status/recovered/live')
live_death_cases = requests.get('https://api.covid19api.com/dayone/country/singapore/status/death/live')

confirmed = live_confirmed_cases.json()
recovered = live_recovered_cases.json()
death = live_death_cases.json()

confirmed_df = pd.DataFrame(confirmed)
recovered_df = pd.DataFrame(recovered)
death_df = pd.DataFrame(death)

print("done")