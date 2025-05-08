import requests

def get_news():
    api_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY"
    response = requests.get(api_url)
    data = response.json()
    headlines = [article['title'] for article in data['articles']]
    return "\n".join(headlines[:5])  # Return the top 5 headlines