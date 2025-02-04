# Use gtts to convert text to audio
from gtts import gTTS
import sqlite3
import os
import sys
import subprocess


class TextToSpeech:
    def __init__(self):
        super().__init__()
        # Due to the lack of audio and data folders, the folders are created when the program starts.
        if not os.path.exists("Data"):
            os.mkdir("Data")

        if not os.path.exists("Voice"):
            os.mkdir("Voice")

        # A database where we can recall recorded sounds
        self.conn = sqlite3.connect("Data\\voicelist.db")
        self.cursor = self.conn.cursor()
        self.setup_data_base()

    def setup_data_base(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS voicelist(
            save_name STRING PRIMARY KEY,
            text_to_speech TEXT NOT NULL,
            lang TEXT NOT NULL
            )
        """)

        self.conn.commit()

    def Additem(self):
        text_menu_lang = ("English = en, \n"
                          "Turkish = tr, \n"
                          "Please choose one of the languages and write it like this, for example (en or english): ")
        # The user enters their desired language and it is sent to the function for review.
        lang = self.langchoice(text_menu_lang)

        if not lang:
            print("Invalid language selection. Please try again.")
            return

        # It takes some text from the user and stops the function if the text is empty.
        text_to_speech = input("Write your text in the selected language:\n")

        if not text_to_speech.strip():
            print("Text cannot be empty!")
            return

        tts = gTTS(text=text_to_speech, lang=lang)

        # It stores the sound name in the data and stops working if it is empty.
        # The naming is so that we can play the sound again whenever we want.
        save_name = input("What name do you want to save it under? ").strip()

        if not save_name:
            print("Please enter a valid name.")
            return

        tts.save(f"Voice/{save_name}.mp3")
        self.cursor.execute("""
            INSERT INTO voicelist (save_name, text_to_speech, lang)
            VALUES (?, ?, ?)
        """, (save_name, text_to_speech, lang))
        self.conn.commit()
        print(f"Saved successfully as {save_name}.mp3")

    def Removeitem(self):
        # To delete a sound, the user first enters its name and deletes it from the Data and Sound folder.
        id_name = input("Enter the voice ID Name to remove: ").strip()
        file_path = f"Voice/{id_name}.mp3"

        self.cursor.execute("DELETE FROM voicelist WHERE save_name = ?", (id_name,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            if os.path.exists(file_path):
                os.remove(file_path)
            print(f"Voice {id_name} removed.")
        else:
            print("Voice ID Name not found.")

    def Displayvoices(self):
        self.cursor.execute("SELECT * FROM voicelist")
        voicelist = self.cursor.fetchall()

        if not voicelist:
            print("No voice available.\n")
        for voice in voicelist:
            self.Displayvoice(voice)

    def Displayvoice(self, voice):
        # show the one voice
        print(f"ID Name: {voice[0]}")
        print(f"  Text: {voice[1]}")
        print(f"  Language: {voice[2]}")
        print("\n")

    def Playvoice(self):

        self.cursor.execute("SELECT * FROM voicelist")
        voicelist = self.cursor.fetchall()
        if not voicelist:
            print("No voice available.\n")
            return
        for voice in voicelist:
            print(f"ID Name: {voice[0]}")


        file_name = input("Enter the name of the voice file to play (without .mp3): ").strip()
        file_path = f"Voice/{file_name}.mp3"

        # To start sound on Mac, Linux, and Windows
        # I used the subprocess library to play audio on Linux and Mac.
        if os.path.exists(file_path):
            if sys.platform == "win32":
                # Windows
                os.system(f"start {file_path}")
            elif sys.platform == "darwin":
                # macOS
                subprocess.call(["afplay", file_path])
            else:
                # Linux
                subprocess.call(["mpg321", file_path])
        else:
            print("File not found!")

    def Quit(self):
        print("Exiting the program...")
        sys.exit()


    def langchoice(self, prompt):
        # To check if the entered language is available in the dict
        lang = input(prompt).strip().lower()
        lang_dict = {
            "english": "en", "en": "en",
            "turkish": "tr", "tr": "tr",
        }
        return lang_dict.get(lang, None)

    def get_valid_int(self, prompt):
        # To check if the entered item is a number or not
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid number.")


def start_program():
    start = TextToSpeech()

    text_menu = ("Menu: \n"
                 "\t1. Add the new voice.\n"
                 "\t2. remove the voice.\n"
                 "\t3. show the all voice.\n"
                 "\t4. play voice.\n"
                 "\t5. quit.\n")

    print(text_menu)
    while True:
        # The infinite loop can run as long as the user wants.
        text_choice = "Enter one of the options: "
        choice = start.get_valid_int(text_choice)

        if choice == 1:
            start.Additem()
        elif choice == 2:
            start.Removeitem()
        elif choice == 3:
            start.Displayvoices()
        elif choice == 4:
            start.Playvoice()
        elif choice == 5:
            start.Quit()
        else:
            print("Choose a number between 1 and 6.\n")

if __name__ == "__main__":
    text = ("\nHello, I am Naeem. This project is a personal project to convert text to voice.\n"
            "In this code, you enter text in your language and convert it to voice.\n\n")
    print(text)

    start_program()