import os
import pygame

def play_music():
    # 1. Initialize the mixer
    pygame.mixer.init()

    # 2. Find your music files
    # This looks for a folder named 'music' in your project
    music_dir = "music" 
    
    if not os.path.exists(music_dir):
        print(f"Error: Folder '{music_dir}' not found. Create it and add MP3s!")
        return

    songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

    if not songs:
        print("No MP3 files found in the music folder.")
        return

    # 3. List the songs for the user
    print("\n--- Your Playlist ---")
    for index, song in enumerate(songs):
        print(f"{index + 1}. {song}")

    # 4. User selection
    try:
        choice = int(input("\nEnter the number of the song you want to play: ")) - 1
        selected_song = os.path.join(music_dir, songs[choice])
    except (ValueError, IndexError):
        print("Invalid selection. Try again.")
        return

    # 5. Play the song
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()
    print(f"Now playing: {songs[choice]}")

    # 6. Basic Controls
    while True:
        print("\nControls: p = pause, r = resume, s = stop, q = quit")
        query = input(">> ").lower()

        if query == 'p':
            pygame.mixer.music.pause()
        elif query == 'r':
            pygame.mixer.music.unpause()
        elif query == 's':
            pygame.mixer.music.stop()
            break
        elif query == 'q':
            pygame.mixer.music.stop()
            exit()

if __name__ == "__main__":
    play_music()