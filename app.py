from flask import Flask, render_template, request, redirect
from api.task import CandidateConstants
import logging as logger
import os

logger.basicConfig(level='DEBUG')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    """
    Render the page, can upload the file and save in proper directory.
    """
    if request.method == 'POST':
        image = request.files["image"]
        #--Only csv file can allow to upload.
        if image.filename.split('.')[-1] == 'csv':
            if image.filename not in os.listdir(CandidateConstants.BASE_FILE):
                image.save(os.path.join(CandidateConstants.BASE_FILE, image.filename))
        
        #-- Render the template with proper message.
        return render_template('index.html', name=CandidateConstants.MESSAGE)

    return render_template('index.html')
#


if __name__ == '__main__':
    logger.debug('server started')
    #-- For accessing the api import the all file 
    from api import *

    app.run(
        port=8000, debug=True
    )


