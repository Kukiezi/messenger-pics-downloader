# Messenger Pics Downloader

Messenger Pics Downloader is a python3 application created with requests and selenium to download all images from specifcic conversation on messenger.

## Requirments

* You need to have Python 3.4+
* You need to have [chromedriver] in messenger-pics-downloader folder

## Installation

```sh
git clone https://github.com/Kukiezi/messenger-pics-downloader
```
Go to [chromedriver] and download chromedriver into messenger-pics-downloader. 

To start application:

```sh
python3 messenger-pics-downloader
```
<b>Great, now You should have running application!</b>

## How to use

#### Credentials

Go to <b>config.json</b> and fill in credentials:

  - username - your facebook email
  - password - your facebook password
  - folder_name - folder in which Your images will be saved. If left empty default folder is called <b>images</b>
  - messenger_path - url to conversation You want to download images from (log in to facebook, open everything in messenger, select chat You want images from and copy url)

example:

```json
"credentials": {
    "username": "random@gmail.com",
    "password": "password1234",
    "folder_name": "ImagesFolder",
    "messenger_path": "https://www.facebook.com/messages/t/john_smith
  },
```

#### Settings

Go to <b>config.json</b> and look at settings:

  - check_stop_every_pic - if You download images from conversation where is a lot of them You can set up check point. Program will ask every `x` pictures if You want to stop now and download what You have or continue. To disable leave at 0
  - start_scrapping_at_pic - count of pictures You want to skip before starting scrapping and downloading. Can be useful if for some reason program failed last time and You got 500 images out of 10000 so You restart and skip to 500th image. To disable leave at 0


example:

```json
"settings": {
    "check_stop_every_pic": 50,
    "start_scrapping_at_pic": 200,
  },
```
Above example will skipp to 200th picture and ask You if You want to stop or continue every 50.

#### Usage

After starting You will have option to use either `config.json` or add data manually. For manual You will have to write input in console. I suggest using `config.json` for better experience.

When program will start You can basically leave the desk, but terminal must be kept open. If something unexpected happens You can find more about it in Error Handling section below.

#### Error handling

As it is selenium errors might happen due to slower internet or anything that might happen unexpectly on facebook. More details You will find in `webdriver_error.txt`. 

Before posting any Problems here please try to run a few times to make sure it wasn't just accident.

## TODO

This project was made to learn more about python and I don't have big plans for it, but if You find a good feature to add or You make it Yourself I will be more then happy to check it out!

   [chromedriver]: <https://sites.google.com/a/chromium.org/chromedriver/>

