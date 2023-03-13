import traceback
from flask import Flask, render_template
from flask import request

class ML:
    def __init__(self):
        self.avaliable_models = {
            "face_detection": {"route":"/additional_drive/ML/face_detection", "freq":0},
            "car_detection": {"route":"/additional_drive/ML/car_detection", "freq":0},
            "shoe_detection": {"route":"/additional_drive/ML/shoe_detection", "freq":0},
            "cloth_detection": {"route":"/additional_drive/ML/cloth_detection", "freq":0},
            "signal_detection": {"route":"/additional_drive/ML/signal_detection", "freq":0},
            "water_level_detection": {"route":"/additional_drive/ML/water_level_detection", "freq":0},
            "missile_detection": {"route":"/additional_drive/ML/missile_detection", "freq":0}
        }
        self.loaded_models_limit = 2
        self.loaded_models = {
            model: self.load_weights(model)
            for model in list(self.avaliable_models)[:self.loaded_models_limit]
        }
    
    def load_weights(self, model):
        return self.avaliable_models.get(model,None)
        
    def load_balancer(self, new_model):
        frequency_of_loaded_models = []
        for model in self.loaded_models:
            frequency = self.avaliable_models[model]["freq"]
            frequency_of_loaded_models.append((model, frequency))

        def get_frequency(item):
            return item[1]

        frequency_of_sorted_models = sorted(frequency_of_loaded_models, key=get_frequency)
        unload = frequency_of_sorted_models[0][0]

        del self.loaded_models[unload]
        self.loaded_models[new_model] = self.load_weights(new_model)
        
        

app = Flask(__name__)
ml = ML()

@app.route('/')
def get_loaded_models():
    # return ml.loaded_models
    loaded_models = ml.loaded_models.keys()
    return render_template('index.html', loaded_models=loaded_models)

@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    try:
        model = request.form["model"]
        if model not in ml.loaded_models:
            ml.load_balancer(model)
        ml.avaliable_models[model]["freq"] += 1
        return ml.loaded_models[model]
    except:
        return str(traceback.format_exc())

# app.run(host='0.0.0.0', port=5000)
app.run()