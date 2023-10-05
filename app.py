from flask import Flask, request
import whisper
from pprint import pprint
import os

app = Flask(__name__)


@app.route("/upload-audio", methods=["POST"])
def upload_audio():
    if "file" not in request.files:
        return "No file found", 400

    audio_file = request.files["file"]
    filename = audio_file.filename
    audio_file.save("./calls/" + filename)

    # Process the audio file here (e.g., save it to a specific location, perform some operations)
    try:
        model = whisper.load_model("medium")
        result = model.transcribe("./calls/" + filename)
        os.remove("./calls/" + filename)

        pprint(result)
        return result, 200
    except Exception as e:
        print(f"Error occured {str(e)}")
        return "Internal Server Error", 500


if __name__ == "__main__":
    app.run()
