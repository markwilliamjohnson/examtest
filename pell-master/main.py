from flask import Flask
from flask import request, render_template
from flask import send_from_directory

import urllib
import pandas as pd
import random 


app = Flask(__name__)

@app.route ('/test')
def test():
    return ("hello")


@app.route ('/template')
def template():
#     myprompt = request.args.get('prompt')
#     response = openai.Completion.create(
#       engine="davinci",
#       prompt=myprompt,
#       temperature=0.7,
#       max_tokens=100,
#       top_p=1.0,
#       frequency_penalty=0.2,
#       presence_penalty=0.0,
# #       stop=["\n"]
#     )

#     responsetext = urllib.parse.quote (response.choices[0].text)
    return render_template ("testme.html", mytext = responsetext)

maindf = pd.DataFrame()
optionlist = list()
choicelist = list()
datelist = list()
sessionvar = ""

@app.route('/download', methods=['POST'])
def download():

    sessionvar = request.form ["postdata"]
    mydf = pd.read_json (sessionvar)    
    mydf1 = mydf.transpose()
    mydf1.to_excel ("datadownload.xlsx", index=False)

    return send_from_directory("./", "datadownload.xlsx", as_attachment=True)

@app.route('/')
def start():
    # sessionvar = "teststore" + str(random.randrange (0,10000000)) 
    myfile = open ("test.html", "r", encoding="utf-8")
    mytext = myfile.read()
    bigtext = mytext
    

    # output = "<center><h1>Meta-discipline Toolkit</h1>"
    # output = output + "<font style='font-size:20px'>Enter search: <input style='font-size:20px' type=text id='myinput' size=80></input><br></center>"
    # output = output + "\n<script>function submit() {window.location.href = './respond?sess=" + str(sessionvar) + "&prompt=' + document.getElementById('myinput').value}"
    # output = output + "document.getElementById('myinput').addEventListener('keyup', function(event) {event.preventDefault(); if (event.keyCode === 13) {submit();}});"
    # output = output + "</script>"
    starttext = urllib.parse.quote (bigtext)
    return (render_template ("examtest.html", startdoc=starttext))

@app.route('/respond')
def process_prompt():

    sessionvar = request.args.get ("sess")
    # myfile = open (sessionvar, "a")
    # output = "<center><h1>Meta-discipline Toolkit</h1></center>"
    # myprompt = request.args.get('prompt')
    # choice = request.args.get ('choice')
    # myfile.write ("*****" + str (choice))
    # myfile.write ("\n*****" + str(myprompt))
    # output = output + "<h2>" + str(myprompt) +"</h2><br><font style='font-size:20px'>"
    # for t in range (0, 4):

    #     response = openai.Completion.create(
    #       engine="davinci",
    #       prompt=myprompt,
    #       temperature=0.7,
    #       max_tokens=100,
    #       top_p=1.0,
    #       frequency_penalty=0.2,
    #       presence_penalty=0.0,
    # #       stop=["\n"]
    #     )
    #     optionlist.append (response.choices[0].text)
    #     # response = "test" + str(t)
    #     # optionlist.append ("test" + str(t))
    #     myfile.write ("\n*****" + str(response.choices[0].text))
    #     # myfile.write ("\n*****" + str(response))
    #     output = output + "<div><input name='group1' type=radio id='" + str(t) + "' onclick='setselect()'><label for='" + str(t) + "'><b>Option " + str(t+1) + ":</b>..." + response.choices[0].text + "</label></input></div><p>"
    #     # output = output + "<div><input name='group1' type=radio id='" + str(t) + "' onclick='setselect()'><label for='" + str(t) + "'><b>Option " + str(t+1) + ":</b>..." + str(response) + "</label></input></div><p>"

    # output = output + "<center><h3>Select which option you are most interested in...<p>"
    # output = output + "Why are you interested?: <input style='font-size:20px' type=text id='myinput' size=80></input><br></center>"
    # output = output + "<button onclick='download_result()'>Download Results</button>"
    # output = output + "\n<script>"
    # output = output + "document.getElementById('myinput').addEventListener('keyup', function(event) {event.preventDefault(); if (event.keyCode === 13) {submit();}});"
    # output = output + "\nmyselect='';\nfunction submit() {if (myselect == '') {alert ('You must select an option')} else window.location.href = './respond?sess=" + str(sessionvar) + "&prompt=' + document.getElementById('myinput').value + '&choice=' + myselect}"
    # output = output + "\nfunction setselect() {myselect = document.querySelector('input[name=\"group1\"]:checked').id; document.getElementById ('myinput').value = document.getElementsByName('group1')[myselect].labels[0].innerText.substr(9) }"
    # output = output + "\nfunction download_result() { window.location.href = './download?sess=" + str(sessionvar) + "&prompt=' + document.getElementById('myinput').value + '&choice=-1'}"
    # output = output + "\n</script>"

    # myfile.close()

    return (output)

if __name__ == "__main__":
  app.run()