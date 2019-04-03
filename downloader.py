import requests


def downloadImages(directory, folder_name, image_name, src):
    img_data = requests.get(
        src).content
    with open(f'{directory}/{folder_name}/{image_name}.jpg', 'wb') as handler:
        handler.write(img_data)
