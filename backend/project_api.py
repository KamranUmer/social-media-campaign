import os
import requests

url = "https://instagram-statistics-api.p.rapidapi.com/community"

querystring = {"url":"https://www.instagram.com/verve_0304"}

headers = {
	"X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
	"X-RapidAPI-Host": "instagram-statistics-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())