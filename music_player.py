from pygame import mixer
import os
import random
from mutagen.mp3 import MP3
import time
from threading import Thread
import webbrowser

# Getting the list of all files present in the directory
print('Path to module:',mixer.__file__)
path = "C:\\Users\\pranav\\Music"
#Here, \U in "C:\Users... 
#starts an eight-character Unicode escape, such as \U00014321. In your code, the escape is followed by the character 's', which is invalid.
#So you can either double the back slash or type an r in front of the string to make it a raw string

os.chdir(path)
choice = 0
run_it_once = 0
all_files = os.listdir() # List of all the files present in this directory
song_list = [] # Stores name of all mp3 extension files
song_dict = {} # Dictionary to store information for all songs , so no need to use mutagen.mp3 again and again

# Making a list and dictionary of songs
for files in all_files:
    if '.mp3' in files:
        song_info = MP3(files).info
        song_list.append(files)
        song_dict[files] = [song_info.length,song_info.sample_rate]


# Defining a function that will randomly choose songs for you
def song_selector():
    print("Song_selector function starts")
    song = random.choice(song_list)
    print("Song_selector function ends")
    return song

# Give a list of song and starts the selected one
def play_selected_song():
    print("Play_selected_song Function starts")
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
    # print("Play_selected_function is sending the song to ask_user")
    print("Play_selected_function is sleeping",str(song_dict[song][0]))
    time.sleep(song_dict[song][0])
    print("Play_selected_function ended")

# Randomly picks a song and play it
def random_play_song():
    global randomly_playing
    print("Random_play_song function starts")
    print("\n\nSelecting a random song")
    # Randomly chooses a song for you
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
    # Removing .mp3 from last
    song.replace('.mp3', '')
    # Printing a message and finally playing the song
    print("Playing", song, ", it is", song_time, "long\n")
    # start_time = time.time()
    mixer.music.load(song)
    mixer.music.play()
    # random_play_song()
    # end_time = time.time()
    # total_time = end_time - start_time
    # print("Total time :", total_time)
    # print("Song length :", song_length)
    if run_it_once == 0:
        Thread(target=ask_user).start()
    # times += 1
    print("while loop will sleep for",song_length)
    print("Random_play_song is sleeping")
    time.sleep(song_length)
    # mixer.music.unload(song)
    print("Random play song sleep finished")
    # random_play_song()
    print("Random_play_song function ends")
    
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

# Ask for a song and open it in webbrowser to furhter download
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

def current_song():
    print("Current_song function ends")
    for song in song_list: 
        fileobj= open(song,"wb+")
        if not fileobj.closed:
            print("file is already opened")
    print("Current song function ends")
# Ask user if wants to cotinue this song , download any other song or play song of his choice
def ask_user():
    while 1:
        run_it_once += 1
        print("ask_user function starts")
        print("\n1. Continue this song")
        print("2. Start another random song")
        print("3. Choose a song")
        print("4. Close Program")
        print("5. Download more song")
        print("6. Pause the song")
        try:
            choice = int(input("Enter your choice :"))
            # time.sleep(3)
            if choice == 1:
                print("Continuing this song..")
                # time.sleep()
                return None
            elif choice == 2:
                # mixer.music.unload()
                mixer.music.stop()
                # Thread(target=random_play_song).
                random_play_song()
            elif choice == 3:
                play_selected_song()
                # mixer.music.unload()
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
        print("ask_user fucntion ends")
    

print("Welcome to your own song player")
Thread(target=random_play_song).start()
# random_play_song()
# Thread(target = ask_user).start()
# mixer.music.set_endevent(random_play_song)
    # print(a,"while loop sleeping for",b)
    # time.sleep(song_dict[randomly_playing][0])
    # ask_user(song_list)
    # if what_next == 2:
    #     break
    # else:
    #     pass
    # if (total_time+1.5) > song_length and song_length > (total_time - 1.5) and what_next == 1 :
    #     play_song()
    # else:
    #     print("Closing Program...")




