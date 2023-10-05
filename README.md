# Audio To Text

This service allows users to create transcipt from audio file. It runs as a Docker container with Python/Flask and Nginx.

### Endpoints

Uploads an audio file.

```shell
POST /upload-audio
```

## Docker Configuration

The Dockerfile installs Python with Flask and Nginx. Nginx handles proxying requests to the Flask application running with Gunicorn.

Build the image:

```yml
docker build -t audio-upload .
Run the container:

Copy code

docker run -p 80:80 audio-upload
The service will be available on port 80.

Local Development
Install dependencies:

Copy code

pip install -r requirements.txt
Run the app:

Copy code

flask run
The app will be available on http://localhost:5000.

Let me know if you would like me to explain or expand on any part of this README!
```
