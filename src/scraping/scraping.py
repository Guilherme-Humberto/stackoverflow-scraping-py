import requests
from bs4 import BeautifulSoup

def getHtmlStruct(url: str):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')

    questions = []

    for question in html.select('.s-post-summary--content'):
        questionTitle = question.select_one('.s-post-summary--content-title .s-link')
        questionExcerpt = question.select_one('.s-post-summary--content-excerpt')

        questions.append({
            'title': questionTitle.text.strip(),
            'excerpt': questionExcerpt.text.strip(),
        })
    
    return questions