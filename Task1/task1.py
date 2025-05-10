import requests
import matplotlib.pyplot as plt
import seaborn as sns


API_KEY = "861ed05ddf0d2cbd2368b9b79f231614"

city = input("Enter City Name: \n")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()


temp = data['main']['temp']
humidity = data['main']['humidity']
description = data['weather'][0]['description']


print(f"City: {city}")
print(f"Temperature: {temp} °C")
print(f"Humidity: {humidity} %")
print(f"Weather Condition: {description}")


labels = ['Temperature (°C)', 'Humidity (%)']
values = [temp, humidity]

sns.set(style="whitegrid")
plt.figure(figsize=(6,4))
sns.barplot(x=labels, y=values, palette="coolwarm")
plt.title(f"Current Weather in {city}")
plt.ylabel("Values")
plt.tight_layout()
plt.show()
