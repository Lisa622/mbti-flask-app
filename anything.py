import flask
import random

#---------------------Python function----------------------------#
# Initialize the app
app = flask.Flask(__name__)

#loads the page
@app.route("/")
def viz_page():
    with open("index.html", 'r') as viz_file:
        return viz_file.read()
    
#listens
@app.route("/gof", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this url,
    Read the grid from the json, update and send it back
    """
    #html "posts" a request and python gets the json  from that request 
    data = flask.request.json
    types = ['INTJ', 'ENTP', 'ISTP', 'ENFJ', 'ISFJ', 'INFP', 'ENTJ', 'ESFJ', 'INFJ', 'ISTJ', 'ESTJ', 'ISFP', 'ESTP', 'ESFP', 'INTP', 'ENFP',\
           'You have zero personality','You have no personality']
    string = ['I guess.','Sure. Why not?','Possibly.','Maybe.','Why are you still doing this?','Go outside.']
    a2 = random.sample(types,1)
    b=random.sample(string,1)
    c=''.join(a2)
    d =' '.join(b)
    a = data['grid']
    result= [c+'.'+'\n'+d]
    return flask.jsonify({'words': result})







#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0', port=8004)