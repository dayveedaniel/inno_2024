# no solution yet just AI generated code

from collections import defaultdict

def read_playlists():
    playlists = defaultdict(list)
    while True:
        line = input().strip()
        if not line:
            break
        playlist_name, _, song_title, length = line.strip('"').split('"')
        playlist_name = playlist_name.strip()
        song_title = song_title.strip()
        minutes, seconds = map(int, length.split(':'))
        duration = minutes * 60 + seconds
        playlists[playlist_name].append((song_title, duration))
    return playlists

def read_songs_played():
    num_songs = int(input())
    songs_played = []
    for _ in range(num_songs):
        line = input().strip()
        count, title = line.rsplit(maxsplit=1)
        count = int(count)
        songs_played.append((title.strip(), count))
    return songs_played

def count_song_plays(playlists, songs_played):
    song_counts = defaultdict(int)
    total_played_duration = sum(count * duration for _, (_, duration) in songs_played)
    
    for playlist in playlists.values():
        playlist_duration = 0
        playlist_pos = 0
        while playlist_duration < total_played_duration:
            song, duration = playlist[playlist_pos]
            song_counts[song] += 1
            playlist_duration += duration
            playlist_pos = (playlist_pos + 1) % len(playlist)
    
    return song_counts

def print_song_counts(songs_played, song_counts):
    for song, _ in songs_played:
        played_count = song_counts[song]
        print(f'"{song}" played {played_count} times')

# Read the input
playlists = read_playlists()
songs_played = read_songs_played()

# Count the song plays
song_counts = count_song_plays(playlists, songs_played)

# Print the output
print_song_counts(songs_played, song_counts)
