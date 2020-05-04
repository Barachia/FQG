# FQG
Follow-up question generation

Main file to generate questions: `fqg.py`

# Requirements
- SENNA [here](https://ronan.collobert.com/senna/)
- Python 3.7.x

# Installation
- Make sure to have the 'senna' folder in this project's root folder
- Run `python install -r requirements.txt` to install all the packages

# Running
Set `TRAINING = TRUE` to train the dataset

Set `TESTING = TRUE` to answer one question at a time

To run with a user interface: `ui.py` (set both parameters for TRAINING and TESTING to FALSE in fqg.py when running from ui.py)

To run a question server for the follow-up questions, run `python question_server.py`. You should be able to make calls to the server with this:

## Open questions
http://localhost:8190/openquestions?lang=en
## Follow-up questions
http://localhost:8190/followupquestions?text=[TEXT]&lang=en

# References
Mandasari, Y. (2019). Follow-up Question Generation (Master's thesis, University of Twente).

https://essay.utwente.nl/79491/
