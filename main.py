from src.scraping import scraping
from src.database import database

questions = scraping.getHtmlStruct(
    url='https://pt.stackoverflow.com/questions/tagged/python'
)

database.createTable()
database.insertQuestions(questions)
questions = database.getQuestions()