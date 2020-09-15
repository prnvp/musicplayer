import os
import random
import time
import webbrowser
from threading import Thread

from mutagen.mp3 import MP3
from pygame import mixer

# print('Path to module:',mixer.__file__)
path = "C:\\Users\\pranav\\Music"
#Here, \U in "C:\Users... 
#starts an eight-character Unicode escape, such as \U00014321. In your code, the escape is followed by the character 's', which is invalid.
#So you can either double the back slash or type an r in front of the string to make it a raw string

#In this part I have changed the path of the workspace to Music(Directory) and made a list and dictionary with all song name and song infos
os.chdir(path) 
choice = 0
run_it_once = 0
all_files = os.listdir() 
song_list = [] 
song_dict = {} 

# Adding Content in the dictionary(i.e song name and their song infos)
for files in all_files:
    if '.mp3' in files:
        song_info = MP3(files).info
        song_list.append(files)
        song_dict[files] = [song_info.length,song_info.sample_rate]


# Defining a function that will randomly choose songs for you using random module
def song_selector():
    print("Song_selector function starts")
    song = random.choice(song_list)
    print("Song_selector function ends")
    return song

# Give a list of song(like a menu) and starts the selected song input by user
def play_selected_song():
    # Play_selected_song Function starts"
    print("\nPlease select a song :")
    for index,song in enumerate(song_list):
        song_name = song[:len(song)-3]
        print(str(index+1)+")",song_name)
    try:
        print("(If you want to cancel type 0 in choice)")
        choice = int(input("Your choice , type the number of the song : "))
        if choice == 0:
            return 0
            #ask_user()
        else:
            for index,song in enumerate(song_list):
                if choice == index + 1:
                    print("You selected for",song_list[index][:len(song)-3], "Playing starts now...")
                    mixer.init(song_dict[song_list[index]][1])
                    mixer.music.load(song_list[index])
                    mixer.music.play()
                    break
    except Exception as e :
        print("There was some error , please try again")
        print("Error : ",e)
    print("Play_selected_function is sleeping",str(song_dict[song][0]))
    time.sleep(song_dict[song][0])
    # Play_selected_function ended

# Randomly picks a song and play it
def random_play_song():
    global randomly_playing
    
    # Random_play_song function starts
    print("\n\nSelecting a random song")
    song = song_selector()
    randomly_playing = song
    
    # Getting the length and frequency of songs in seconds
    if song in song_dict.keys():
        song_length = song_dict[song][0]
        song_frequency = song_dict[song][1]
    mixer.init(song_frequency)
    
    # Correcting the format of song length (into minutes and seconds)
    ty_res = time.gmtime(song_length)
    song_time = time.strftime("%H:%M:%S", ty_res)
    song.replace('.mp3', '')
    print("Playing", song, ", it is", song_time, "long\n")
    mixer.music.load(song)
    mixer.music.play()
    Thread(target=ask_user).start()
    print("while loop will sleep for",song_length)
    print("Random_play_song is sleeping")
    time.sleep(song_length)
    # Random_play_song function ends
    
# Pauses the song and start the unpause_music function to wait for user input
def pause_song():
    print("Pause function starts")
    mixer.music.pause()
    unpause_music()
    print("Pause function ends")

def unpause_music():
    while 1:
        permission = input("Type C to continue or E to exit : ")
        if permission == 'c' or permission == 'C':
            mixer.music.unpause()
            break
        elif permission == 'e' or permission == "E":
            exit(0)
        else:
            print("Invalid input try again")

# Ask for a song from user and then open it in webbrowser to further download
def download_song():
    print("Download_song function starts")
    count = 0
    search = str(input("Enter the song name you want to download : "))
    try:
        for song in song_list:
            if search.lower() in song.lower():
                count += 1
        if count > 0:
            print("The song is already installed in your computer,found match for",count,"times")
        else:
            print("Opening webbrowser because",search.lower(),"is not in",song.lower())
            url = "https://freemp3downloads.online/download?url=" + search
            webbrowser.open_new(url)
    except Exception as e:
        print("There was an error")
        print("Error:-",e)
    print("Download_song function ends")

# Ask user if wants to cotinue this song , download any other song or play song of his choice
def ask_user():
    while 1:
        # ask_user function starts
        print("\n1. Continue this song") 
        print("2. Start another random song")
        print("3. Choose a song")
        print("4. Close Program")
        print("5. Download more song")
        print("6. Pause the song")
        try:
            choice = int(input("Enter your choice :"))
            if choice == 1:
                print("Continuing this song..")
                time.sleep()
                return None
            elif choice == 2:
                mixer.music.stop()
                random_play_song()
            elif choice == 3:
                play_selected_song()
                mixer.music.stop()
            elif choice == 4:
                mixer.music.stop()
                exit(0)
            elif choice == 5:
                download_song()
            elif choice == 6:
                pause_song()
            else:
                print("Invalid choice")
        except Exception as e:
            print("Error : Input must be a number")
            print("Error -",e)
        # ask_user fucntion ends
    

print("Welcome to your own song player")
Thread(target=random_play_song).start()
