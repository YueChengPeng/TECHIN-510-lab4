# TECHIN 510 Lab 4

## Getting Started
Open the terminal and run the following commands:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## What's Included
- app.py: The Time App. Functions include:
    - A world clock that displays time in different locations around the world.
    - Users can select to display time of up to 4 locations using the drop down menu.
    - The time is updated every second.
    - (bonus): UNIX timestamp display and a function that converts UNIX timestamp to Human time.
    - (bonus): Fetch real-time hourly weather data based on the current time and display the weather.
- hello.py: use GitHub Actions to print "hello world" every 15 minutes.
    - P.S. The GitHub Actions deployment for the Web Scraper can be found in my [Lab2 repo](https://github.com/YueChengPeng/TECHIN510-lab2), and the data is pushed to the `data_actions` folder inside the repo.

## Lessions Learned
- How to use re Python package to get desired sub-string using pattern identification out of raw strings.
- How to use datetime and pytz Python packages to get current time from diverse time zones.
- If you use venv Python environment on VS Code and run "streamlit run app.py", sometimes it'll say "no such command". Just run "source venv/bin/activate" to activate the virtual environment.

## Questions/Uncertainties
- Not sure yet how to use PostgreSQL with Python.
- Not sure why we need to use PostgreSQL given that we can also upload data in csv format directly to GitHub. (Does GitHub also provide SQL functions?)
- Is it possible not to display the time via text (e.g. 15:00), but in the physical form of actual clocks (with hands)? What Python Libraries can directly be called to simplify this? 