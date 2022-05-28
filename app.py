from flask import Flask, render_template, request

# IMPORT ML MODEL

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    imageFile = request.files['imageFile']
    image_path = './images/' + imageFile.filename
    imageFile.save(image_path)

    # PREDICT USING THE MODEL
    # FOR NOW ASSUME THE PREDICTED RESULT IS OBTAINED

    classification = "Hi there, 90% local data"

    return render_template('index.html', prediction=classification)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
