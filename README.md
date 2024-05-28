# Weather app

Displays the weather temperatures in different cities and saves the information.
The user can add and delete cities from the home page.
You can't add cities, which are already in the list or don't exists. A message is displayed, when a city is successfully added and when an error occures.

## Installation

1. **Clone the Repository**

   ```bash
   https://github.com/cristibologa/Project.git
   cd Project
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

   ```

4. **Enter your API in** `Project\the_weather\weather\views.py`

   ```bash
   API_KEY = 'ENTER YOUR API'
   Or use my API_KEY
   ```

## Running the Project

```bash
cd Project\the_weather

python manage.py runserver

```

## Get an API key from:

https://openweathermap.org/
