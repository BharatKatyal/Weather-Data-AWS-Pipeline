# Weather Data Collection System

A Python application that fetches real-time weather data from OpenWeather API and stores it in AWS S3.

## Features

- Fetches weather data for multiple cities (Philadelphia, Seattle, New York)
- Displays temperature, humidity, and weather conditions
- Automatically stores weather data in AWS S3
- Includes timestamp for historical tracking

## Prerequisites

- Python 3.x
- AWS Account
- OpenWeather API key

## Getting Started

### OpenWeather API Setup

1. Sign up at [OpenWeather](https://home.openweathermap.org/users/sign_up)
2. Get your API key from [API Keys page](https://home.openweathermap.org/api_keys)

> **Note**: The API key may take a few minutes to become active. If you're getting a 401 error, this might be the reason, or verify your API key.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BharatKatyal/Weather-Data-AWS-Pipeline.git
   cd Weather-Data-AWS-Pipeline/src
   ```

2. Set up virtual environment:

   **Windows**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **MacOS/Linux**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Rename `.env.example` to `.env`
   - Add your configuration:
     ```
     OPENWEATHER_API_KEY=your_api_key
     AWS_BUCKET_NAME=your_bucket_name
     ```
   > Note: If you specify a new bucket name, the script will create it automatically.

## Usage

Run the application:
```bash
python3 weather_dashboard.py
```

### Sample Output
```
Creating bucket mydevopsdayoneweatherapi
Successfully created bucket mydevopsdayoneweatherapi

Fetching weather for Philadelphia...
Temperature: 30.99°F
Feels like: 24.06°F
Humidity: 54%
Conditions: clear sky
```

### Cleanup

1. Deactivate virtual environment:
   ```bash
   deactivate
   ```

2. Clean up AWS resources:
   ```bash
   python cleanup.py
   ```
   You will be prompted:
   ```
   Are you sure you want to delete the S3 bucket 'mydevopsdayoneweatherapi'? (yes/no):
   ```

## Project Structure
```
weather-dashboard/
├── weather_dashboard.py
├── .env
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- AWS S3
- OpenWeather API
- boto3
- python-dotenv
- requests