from flask import Flask, Response, render_template_string
import requests

app = Flask(__name__)

# The link to your JSON file
FILE_URL = "https://dhruvmirrorpremiumftl-ab750004632b.herokuapp.com/55825/Instagram.json?hash=AgADiB"

# This HTML is now inside the Python script
HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head><title>Download Data</title></head>
<body style="font-family: sans-serif; text-align: center; padding: 50px;">
    <h1>Instagram Data Downloader</h1>
    <p>Click below to stream the download directly to your device.</p>
    <a href="/stream-file" style="padding: 15px 25px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Download File</a>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_CONTENT)

@app.route('/stream-file')
def stream_file():
    # Use streaming to prevent memory crash
    req = requests.get(FILE_URL, stream=True)
    
    return Response(
        req.iter_content(chunk_size=1024*1024), 
        content_type='application/json',
        headers={'Content-Disposition': 'attachment; filename=Instagram.json'}
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
