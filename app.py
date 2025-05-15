from flask import Flask, render_template
from azure.storage.blob import ContainerClient
import os

app = Flask(__name__)

# Set these as environment variables or replace with your values
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=acercornerstorage;AccountKey=OHZ0XFSqiKFJ4F78FE1k7zEKortlcEFOfK6zk3jIeV2I8F82lQcKP+swFw6b2UlUrVmLnUVSId8j+AStEK7G+A==;EndpointSuffix=core.windows.net"
AZURE_CONTAINER_NAME = "photogalery"
AZURE_BLOB_URL = "https://acercornerstorage.blob.core.windows.net"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/acers')
def acers():
    return render_template('acers.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    image_urls = []
    if AZURE_STORAGE_CONNECTION_STRING and AZURE_CONTAINER_NAME:
        container = ContainerClient.from_connection_string(
            AZURE_STORAGE_CONNECTION_STRING, AZURE_CONTAINER_NAME
        )
        blobs = container.list_blobs()
        for blob in blobs:
            # Only include image files (optional: filter by extension)
            if blob.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                image_urls.append(f"{AZURE_BLOB_URL}/{AZURE_CONTAINER_NAME}/{blob.name}")
    return render_template('gallery.html', image_urls=image_urls)

if __name__ == '__main__':
    app.run(debug=True)
