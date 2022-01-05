from flask import Flask , render_template, request
import numpy as np
import pickle
import joblib

# import librosa
# import soundfile as sf

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    

# prediction function
# def extract_features(file_name):
#     audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
#     mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
#     mfccs_processed = np.mean(mfccs.T,axis=0)
     
#     return mfccs_processed

# def ValuePredictor(to_predict_list):
# 	to_predict = np.array(to_predict_list)
# 	loaded_model = pickle.load(open("knn.pkl", "rb"))
# 	result = loaded_model.predict(to_predict)
# 	return result[0]

# def knn(ff):

@app.route('/results', methods = ['GET','POST'])
def result():
	if request.method == 'GET':
		to_predict_audio = request.form.get("adioPlay")
		to_predict_list = to_predict_audio.values()
		print("done")
		return render_template("index.html")

# @app.route('/result', methods = ['GET','POST'])
# def result():
# 	if request.method == 'POST':
# 		to_predict_audio = request.form.get("adioPlay")
# 		to_predict_list = to_predict_audio.values()
		
# 		features = extract_features(to_predict_list)
# 		result=ValuePredictor(features)
# 		if int(result)== 0:
# 			prediction ='AC'
# 		elif int(result)== 1:
# 			prediction ='light'	
# 		elif int(result)== 2:
# 			prediction ='song'
# 		else:
# 			prediction ='tv'	
# 		return render_template("result.html", prediction = prediction)


if __name__ == "__main__":
    app.run(debug=True)


    