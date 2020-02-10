# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:50:41 2020

@author: WaterschootJB
"""
import preprocess as pp
import runSENNA as rs
import fqg
import os 
import random

#Network stuff
import hug
import json
from hug_middleware_cors import CORSMiddleware

workPath = os.getcwd()
sennaPath = "/senna/"
input_file = 'input.txt'
input_path = workPath + sennaPath + input_file
senna_input_file = 'input_preprocess.txt' 
senna_input_path = workPath + sennaPath + senna_input_file
workPath = os.getcwd()
starter_questions = workPath+'/starters.txt'
with open(starter_questions, encoding='utf-8') as f:
    dlines = f.read().splitlines() #reading a file without newlines
starterQuestions = dlines

@hug.get("/openquestions")
def getStarterQuestions(lang: str):
    """Retrieve the open questions"""
    root = {}       
    root['openquestions'] = json.dumps(starterQuestions)  
    return root

@hug.get("/followupquestions")
def getFollowUpQuestions(text: str, lang: str):
    """Retrieve the follow-up questions for a sentence"""
    with open(input_path, 'w', encoding='utf-8') as f:
        f.write("%s\n" % text)
    pp.preprocess_senna_input (input_path, senna_input_path) # input is transformed into senna_input (preprocessed & tokenized)
    rs.runSENNA(senna_input_file)
    sentenceList, original = fqg.create_SR(senna_input_path)
    generatedQuestions = fqg.generate_questions(sentenceList, original)
    root = {}
    root['followupquestions'] = json.dumps(generatedQuestions)  
    return root
    
@hug.get("/topicalquestions")    
def getTopicalQuestions(topic: str, lang: str):
    questions = []
    root = {}
    root['topicalquestions'] = json.dumps(questions)
    return root
            
def testQuestions():        
    followUpQuestions = getFollowUpQuestions("I like movies and action comics.")    
    print(followUpQuestions)
    start = True
    answer = ""
    while answer != "exit":
        if start:
            print(random.choice(starterQuestions))
            start = False
        else:
            questions = getFollowUpQuestions(answer)
            print(questions)
            followUpQuestions = json.loads(questions['followupquestions'])            
            print(followUpQuestions)
            print(rs.ranking(followUpQuestions))  
            start = True
        answer = input("Answer: \n")

def server():
    if __name__ == "__main__":
        import waitress
        app = hug.API(__name__)
        app.http.add_middleware(CORSMiddleware(app))
        waitress.serve(__hug_wsgi__, host='0.0.0.0', port=8190)

# testQuestions()
server()

