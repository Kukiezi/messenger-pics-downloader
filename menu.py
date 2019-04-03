import json


def menu_loader(config):
    menu = True
    data = config
    while menu:
        load_question = input("Do You want to load data from config? (y/n):")
        if load_question == 'y':
            if not data["credentials"]["username"] or not data["credentials"]["password"] or not data["credentials"]["messenger_path"]:
                print("Not all fields in config.json are completed")
            else:
                username = data["credentials"]["username"]
                password = data["credentials"]["password"]
                folder_name = data["credentials"]["folder_name"]
                messenger_path = data["credentials"]["messenger_path"]
                menu = False
        elif load_question == 'n':
            print("Please provide Your facebook credentials and data: ")
            username = input("username: ")
            password = input("password: ")
            folder_name = input("folder to save to (default is images): ")
            messenger_path = input(
                "link to conversation (example: https://www.facebook.com/messages/t/john.smith): ")
            if not username or not password or not messenger_path:
                print("All inputs must be completed!")
            else:
                menu = False
        else:
            print("Only y/n are accepted!")

    ret_data = {"username": username, "password": password,
                "folder_name": folder_name, "messenger_path": messenger_path}
    return ret_data
