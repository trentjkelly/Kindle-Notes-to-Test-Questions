# Copyright (c) 2023, Trent Kelly
# All rights reserved.

# This source code is licensed under the MIT-style license found in the
# LICENSE file in the root directory of this source tree. 

import webscraping
import aiQuestions
import time
import validators

# Quick output to user to explain how it works
def printIntroduction():
    print("Before we begin...")
    time.sleep(1)
    print("Make sure to set your book's Goodreads highlights page to 'visible'")
    time.sleep(2)
    print("Otherwise this software will not work...")
    time.sleep(2)
    print("\nWhen completed, paste the url and hit enter: ")

# Quick output to user if their Goodread's page is not visible
def printNotVisible():
    print("Your Kindle notes for this book are not visible.")
    time.sleep(1)
    print("Please click the 'Make all # visivble' button near the top of the goodreads page")
    time.sleep(2)
    print("\nWhen completed, re-paste the url and hit enter: ")

# Quick output to user after they finished using the software
def printConclusion():
    print("There have been 2 files created/modified:")
    time.sleep(1)
    print("1 for only questions and 1 with questions and answers")
    print("Have fun with your reading! :)")

# Foolproofs user input by checking if url can be used for extracting notes
def validURL(url):
    #Check if URL is even good in the first place
    if not validators.url(url):
        print("Not a valid URL.")
        return False
    #Check if URL comes from Goodreads notes page
    if not goodreadsURL(url):
        print("Not a valid Goodreads highlights page URL")
        return False
    
    return True

# Checks if URL comes from actual Goodreads notes page
def goodreadsURL(url):
    # Check if from goodreads notes page
    if not url[0:32] == "https://www.goodreads.com/notes/":
        return False
    # Check if individual notes page (not just main notes page)
    if not url[-7:] == "ref=abp":
        return False

    return True

# Creates strings for the file names
def titles(soup):
    title = webscraping.getBookTitle(soup)
    title = title.replace(' ', '-').lower()
    questionsTitle = 'questions-' + title + '.txt'
    questionsAnswersTitle = 'questions-answers-' + title + '.txt'
    titles = [questionsTitle, questionsAnswersTitle]
    return titles

# Creates strings that contain questions and question-answer pairs for each file
def fileContents(questions, answers):
    questionsString = ""
    for q in questions:
        questionsString += q

    questionAnswersString = ""
    index = 0
    for q in questions:
        questionAnswersString += "Q: " + q + "\n" + "A: " + answers[index]
        index += 1

    fileStrings = [questionsString, questionAnswersString]
    return fileStrings
    
# Actually creating the files
def createFiles(fileTitles, fileStrings):
    f1 = open(fileTitles[0], 'w')
    f1.write(fileStrings[0])
    f1.close()

    f2 = open(fileTitles[1], 'w')
    f2.write(fileStrings[1])
    f2.close()

# Creating list of questions
def getQuestions(answers):
    questions = []

    for a in answers:
        questions.append(aiQuestions.createQuestion(a))

    return questions

# Used to get proper URL when the Goodreads page is not visible
def notVisible():
    printNotVisible()
    user_url = input()
    while not validURL(user_url):
        print("Enter a valid URL: ")
        user_url = input()
    soup = webscraping.getSoup(user_url)
    return soup

def main():
    # Opening text and getting user_url
    printIntroduction()
    user_url = input()

    # Checking that input url is valid
    while not validURL(user_url):
        print("Enter a valid URL: ")
        user_url = input()

    # HTML elements for webscraping
    soup = webscraping.getSoup(user_url)

    # Making user make highlights visible and re-enter url if not
    while not(webscraping.isVisible(soup)):
        soup = notVisible()

    # Let user know to wait on AI after URLs are validated
    print("Loading...\n")

    # Webscrape the quotes and generate questions from OpenAI
    answers = webscraping.getHighlights(soup)
    questions = getQuestions(answers)

    # Create, add to files, and conclude
    fileStrings = fileContents(questions, answers)
    fileTitles = titles(soup)
    createFiles(fileTitles, fileStrings)
    printConclusion()

if __name__ =="__main__":
    main()