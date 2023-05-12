import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

#Plot Charts 
plt.plot(confirmed_df['Date'], confirmed_df['Cases'])
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('Confirmed COVID-19 Cases in Singapore')

# Set the x-axis tick frequency to show every 6 months
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Get the x-axis tick positions and labels
x_ticks = plt.gca().get_xticks()
x_tick_labels = [pd.to_datetime(tm, unit='ms').strftime('%Y-%m') for tm in x_ticks]

# Set the modified x-axis tick labels
plt.gca().set_xticks(x_ticks)
plt.gca().set_xticklabels(x_tick_labels, rotation=45)

# Save the graph as an image
plt.savefig('covid_cases.png')
print("done")