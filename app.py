from flask import Flask, Response, request
import requests

app = Flask(__name__)

# This is the base URL where your file actually lives
SOURCE_BASE = "https://dhruvmirrorpremiumftl-ab750004632b.herokuapp.com"

@app.route('/<path:filename>')
def proxy(filename):
    # Construct the full URL with the hash parameter
    target_url = f"{SOURCE_BASE}/{filename}?hash=AgADiB"
    
    # Stream the response from the source
    req = requests.get(target_url, stream=True)
    
    # Return the stream to the user
    return Response(
        req.iter_content(chunk_size=1024*1024), # 1MB chunks
        status=req.status_code,
        content_type=req.headers.get('Content-Type', 'application/json'),
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
