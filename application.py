from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# import logging
# import requests
# import pymongo

# def lambda_handler(event, context):
# logging.basicConfig(filename="scrapper.log", level=logging.INFO)

application = Flask(__name__)
app = application


@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
    return render_template("index.html")


# route to show the review comments in a web UI
@app.route('/scrape', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content']
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            browser = webdriver.Chrome(
                options=options, service=Service(ChromeDriverManager().install()))
            browser.get(searchString)
            browser.execute_script("window.scrollTo(0,400)", "")

            youtubePage = browser.page_source
            soup = bs(youtubePage, "html.parser")

            link = []
            thumbnail = []
            title = []
            views = []
            time = []

            soupData = soup.find("div", {"id": "contents"})

            # Link
            try:
                videoSoup = (soupData.find_all(
                    "a", {"class": "yt-simple-endpoint inline-block style-scope ytd-thumbnail"}))[0:5]
                for i in videoSoup:
                    link.append("https://www.youtube.com"+str(i.get("href")))
            except:
                print("Error in Link")
                # logging.info("Error in Link")

            # Thumbnail
            try:
                soupvideoThumb = soup.find_all(
                    "img", {"class": "yt-core-image--fill-parent-height"})[:5]
                for i in soupvideoThumb:
                    thumbnail.append(str(i['src']))
            except:
                print("Error in Thumbnail Link")
                # logging.info("Error in Thumbnail Link")

            # Title
            try:
                soupTitle = (soupData.find_all("a", {
                    "class": "yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media"}))[0:5]
                for i in soupTitle:
                    title.append(str(i.get("title")))
            except:
                print("Error in Title")
                # logging.info("Error in Title")

            # No of views
            try:
                soupViews = (soupData.find_all("div", {"id": "metadata"}))[0:5]
                for i in soupViews:
                    views.append(str(i.find_all("span")[1].text))
            except:
                print("Error in no of views")
                # logging.info("Error in no of views")

            # Time of Posting
            try:
                soupTime = (soupData.find_all("div", {"id": "metadata"}))[0:5]
                for i in soupTime:
                    time.append(str(i.find_all("span")[2].text))
            except:
                print("Error in Time of Posting")
                # logging.info("Error in Time of Posting")

            sc_data = []
            for i in range(5):

                dict = {
                    "link": link[i],
                    "thumbnail": thumbnail[i],
                    "title": title[i],
                    "views": views[i],
                    "time": time[i]
                }

                sc_data.append(dict)
                
            with open("yt.csv", "w") as f:
                for i in sc_data:
                    f.write(str(i)+"\n")

            return render_template('results.html', reviews=sc_data)
        except Exception as e:
            # logging.info(e)
            print(e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)