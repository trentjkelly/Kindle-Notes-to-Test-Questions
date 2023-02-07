# Copyright (c) 2023, Trent Kelly
# All rights reserved.

# This source code is licensed under the MIT-style license found in the
# LICENSE file in the root directory of this source tree. 

import bs4
from bs4 import BeautifulSoup
import requests

# Gets the main content from the page
def getSoup(url):
    html_text = requests.get(url).content
    soup = BeautifulSoup(html_text, 'lxml')
    return soup

# Scans the page to see if the users input is visible
def isVisible(soup):
    div = soup.find('div', class_='readingNotes__infoContainer')
    # This div will only appear when user has not made highlights visible
    if(isinstance(div, bs4.element.Tag)):
        return False
    return True

# Gets the individual quotes from the Goodreads page
def getHighlights(soup):
    divs = soup.find_all('div', class_='noteHighlightTextContainer__highlightText')
    spans = []
    for d in divs:
        spans.append(d.span.text)

    return spans

# Grabbing book title from the site
def getBookTitle(soup):
    div = soup.find('div', class_='readingNotesBookDetailsContainer')
    title = div.div.span.a.text
    return title