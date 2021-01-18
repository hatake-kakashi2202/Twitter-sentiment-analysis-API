from flask import Flask,render_template, request, redirect, url_for, flash, jsonify
from keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
from bs4 import BeautifulSoup
app = Flask(__name__)
# run_with_ngrok(app)   #starts ngrok when the app is run
def clean_text(text):
    html_text = BeautifulSoup(text,"html.parser").get_text()
    text = re.sub("[^a-zA-Z]", " ", html_text).strip()
    text = re.sub(r'http\S+', '', text)
    text = re.sub('http', ' ', text)
    text = re.sub('com', ' ', text)
    text = re.sub('  +', ' ', text)
    text = re.sub('\n', ' ', text)
    text = text.lower()
    
    return text
@app.route('/')
def home():
    return render_template('app.html',ans="submit to get value here")

@app.route("/",methods=['POST'])
def get_data():
  model = load_model('my_model.h5') 
  with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
  text = request.form['tweet']
  print(text)
  c_text = clean_text(text)
  print(c_text)
  test = pad_sequences(tokenizer.texts_to_sequences(c_text), maxlen=150)
  y_pred = model.predict(test.reshape(1,-1))
  y_pred = y_pred.flatten()
  ans=''
  for i in range(len(y_pred)):
    if y_pred[i]>=0.5:
      ans='positive'
    else:
      ans='negative'
  print(ans)
  return render_template('app.html', ans=ans)
app.run()