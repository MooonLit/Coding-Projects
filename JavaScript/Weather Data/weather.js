async function getWeather() {
    const cityName = document.getElementById('cityName').value;
    const apiKey = 'YOUR_API_KEY'; // Replace with your OpenWeatherMap API Key
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        if(response.status === 200) {
            displayWeather(data);
        } else {
            document.getElementById('weatherData').innerHTML = 'Weather data not found!';
        }
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}

function displayWeather(data) {
    const weatherDataDiv = document.getElementById('weatherData');
    weatherDataDiv.innerHTML = `
        <h2>Weather in ${data.name}</h2>
        <p>Temperature: ${data.main.temp}°C</p>
        <p>Weather: ${data.weather[0].main}</p>
        <p>Wind Speed: ${data.wind.speed} m/s</p>
    `;
}
