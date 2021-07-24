import os
os.system('pip install telethon')
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("An online StringSession generator Made With ReplRun")
print("\nFire-X...\n     A Dependable Userbot \nhttps://github.com/Chrisdroid1/Fire-X")
APP_ID = int(input("Enter APP ID here: \n"))
API_HASH = input("Enter API HASH here: \n")
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    try:
        session = client.session.save()
        client.send_message("me",
                            f"String Session \nTap To Copy. \n{session}")
        print("String Generated Sucessfully Check Your Saved Message.")
    except Exception as sed:
        print(f"Something Went Wrong While Generating String \nError : {sed}")
