import requests
import pandas as pd
import numpy as np
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

confirmed_df.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_4/confirmed_cases.csv')
recovered_df.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_4/recovered_cases.csv')
death_df.to_csv('/Users/glen/Desktop/Glen_Chue_Govtech_Submission/Section_4/death_cases.csv')

# Plot
plt.figure()
plt.plot(recovered_df['Date'], recovered_df['Cases'])
plt.xlabel('Date')
plt.ylabel('Number of Recoveries')
plt.title('Confirmed COVID-19 Recoveries in Singapore')
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.gcf().autofmt_xdate() # Rotation


plt.savefig('covid_deaths.png')
print("done")