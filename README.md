# YouTube Scraper

This is a Python Flask web application that extracts data from the first 5 videos on a YouTube search page.

The application extracts the following data for each of the 5 videos:

- Link to the video
- Thumbnail image URL
- Title of the video
- Number of views
- Time of posting

The extracted data is then saved in a CSV file named youtube_scrap.csv.

## Deployment

The project has been deployed on AWS successfully with all the above mentioned functionalities.

Project Github Repo Link - https://github.com/adityaazad79/Youtube_Channel_Scraping_with_AWS_Deployment

Deployment link - http://youtubescraper-env.eba-pi3d5tup.ap-northeast-1.elasticbeanstalk.com

## Screenshots
Screenshot 1

![Home Page Loading...](Screenshots/ss1.png"Home Page")

Screenshot 2

![Scraped Result Loading...](Screenshots/ss2.png"Scraped Result")


## Requirements

This application requires the following Python libraries:

- Flask
- Flask-Cors
- BeautifulSoup
- Selenium
- ChromeDriver Manager

## Technologies Used

- Python 3.7
- AWS - Elastic Beanstalk
- AWS - CodePipeline

## Installation

1. Clone this repository.
2. Install the dependencies.
    'pip install -r requirements.txt'
3. Download the Chrome driver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system path.
4. Run the application:
    'python app.py'
5. Open your web browser and go to http://127.0.0.1:8000 to see the application running.


## Usage

1. Input a search query in the text box and click the "Search" button.

2. The application will scrape YouTube for the top 5 videos related to the search query, and display their links, titles, thumbnails, views and posting times.

3. The scraped data will also be saved in a CSV file named youtube_scrap.csv in the same directory as the app.py file.

## Contributing

Aditya Azad - Initial work

This program was created as a learning exercise, and contributions are not currently being accepted. However, you are welcome to use and modify the code for your own purposes.

## Acknowledgments

This project was a part of the Data Science course provided by [PW Skills](https://pwskills.com/).
