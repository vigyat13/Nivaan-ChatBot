from pyngrok import ngrok

# Open a tunnel on port 5000
public_url = ngrok.connect(5000)
print("Your ngrok tunnel URL is:", public_url)