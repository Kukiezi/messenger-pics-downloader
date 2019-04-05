import requests


def downloadImages(directory, folder_name, image):
    img_data = requests.get(
        image.src).content
    with open(f"{directory}/{folder_name}/{image.name}.jpg", "wb") as handler:
        handler.write(img_data)
    print(f"Downloaded image: {image.name}")
