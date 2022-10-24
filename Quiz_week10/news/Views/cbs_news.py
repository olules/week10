import dataclasses
from flask import Blueprint, request, redirect, render_template
from bs4 import BeautifulSoup
import requests
import lxml
from news.models import CbsNews
from news import db
from sqlalchemy import text

hviews = Blueprint('hviews', __name__)

def get_cbs_news():
    url = "https://www.cbsnews.com/latest/rss/main"
    response = requests.get(url)
  
    data = []

    soup = BeautifulSoup(response.text, 'lxml')



    for dat in soup:

        title = dat.find('title')
   
        link = dat.find('link')

        # if link:
        #         link = link.text
        # else:
        #         link = "Not available"
        
        image = dat.find('image')

        # if image:
        #         image = image.text
        # else:
        #         image = "No Image found"
        
        description = dat.find('description')

        data.append({
            'title': title,
            'link': link,
            'image': image,
            'description': description,
        })

    return data


@hviews.route('/cbs_news', methods=['GET', 'POST'])
def cbs_news():
    if request.method == 'POST':
        return redirect('/')

    # new data from cbs news
    data = get_cbs_news()

    hnews = CbsNews.get_all_news()

    return render_template('cbs_news.html', data=hnews)

    # # loop through data
    # for news in data:
    #     # check if news already exists in database
    #     # news['title'] is the title of the news
    #     if news.get('title').lower() not in [hn.title.lower() for hn in hnews]:
    #         hnew = CbsNews(title=news['title'], link=news['link'])
    #         hnew.save()
    #     else:
    #         continue

    # return render_template('cbs_news.html', data=hnews)



