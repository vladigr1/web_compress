import requests
import json
from PIL import Image
import io

def upload_img(path,api_key):
    data = open(path, 'rb').read()
    response = requests.post('https://api.tinify.com/shrink', data=data, auth=('api', api_key))
    response_dict = json.loads(response.text)
    # print(response_dict['output']['url'])
    return response_dict['output']['url']
def download_img(output_url):
    img_response = requests.get(output_url, auth=('api', api_key))
    return Image.open(io.BytesIO(img_response.content))

api_key='Xq6zc0KTcWQ5JBvZtlfCML4QcgPdNBcl'
path = '1nVUO3N.jpg'
output_url = upload_img(path,api_key)
image = download_img(output_url)
image.show()