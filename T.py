import requests
import json

# Function to get current weather based on location
def get_weather(location):
    # API key for OpenWeatherMap
    api_key = "59d3eefaaa37b9aa55f2abe504d9a4f2"

    # API endpoint for current weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    # Send GET request to the API
    response = requests.get(url)

    # Parse the JSON response
    weather_data = json.loads(response.text)

    # Extract relevant information
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]

    # Print the weather information
    print(f"Current weather in {location}:")
    print(f"Temperature: {temperature} K")
    print(f"Description: {description}")


# Get user's current location
def get_location():
    # Use a location API to retrieve the user's location
    # Replace this with your preferred location API or method
    location = "Andhra Pradesh"  # Example location, replace with actual location retrieval logic

    return location


# Main function
def main():
    # Get user's location
    location = get_location()

    # Get current weather based on location
    get_weather(location)


# Run the main function
if __name__ == "__main__":
    main()