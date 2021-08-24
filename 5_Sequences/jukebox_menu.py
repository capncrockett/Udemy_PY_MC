from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

choice = 0

while True:
    if 1 <= choice <= len(albums):
        print("Please choose your song: ")
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
        for index, (track_number, song) in enumerate(songs_list):
            print("{}: {}".format(index + 1, song))

        song_choice = None  # any value that can't be a valid song
        while True:
            song_choice = int(input())
            if 1 <= song_choice <= len(songs_list):
                title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
                print("Playing {}".format(title))
                print("=" * 40)
            else:
                break
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    choice = int(input())
    if choice == 0:
        break

# while True:
#     if choice != valid_album_choice:
#         if choice == valid_album_choice:
#             print("Please choose your song: ")
#             songs_list = albums[valid_album_choice - 1][SONGS_LIST_INDEX]
#             for index, (track_number, song) in enumerate(songs_list):
#                 print("{}: {}".format(index + 1, song))
#
#             song_choice = int(input())
#             if 1 <= song_choice <= len(songs_list):
#                 title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
#                 print("Playing {}".format(title))
#                 print("=" * 40)
#     else:
#         print("Please choose your album (invalid choice exits): ")
#         for index, (title, artist, year, songs) in enumerate(albums):
#             print("{}: {}".format(index + 1, title))
#     choice = int(input())


# while True:
#     print("Please choose your album (invalid choice exits): ")
#     for index, (title, artist, year, songs) in enumerate(albums):
#         print("{}: {}".format(index + 1, title))
#
#     choice = int(input())
#     if 1 <= choice <= len(albums):
#         songs_list = albums[choice - 1][SONGS_LIST_INDEX]
#     else:
#         break
#
#     print("Please choose your song: ")
#     for index, (track_number, song) in enumerate(songs_list):
#         print("{}: {}".format(index + 1, song))
#
#     song_choice = int(input())
#     if 1 <= song_choice <= len(songs_list):
#         print("Playing {}".format(title))
#     title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
#
#     print("=" * 40)
#
#


# while True:
#     print("Please choose your album (invalid choice exits): ")
#     for index, (title, artist, year, songs) in enumerate(albums):
#         print("{}: {}".format(index + 1, title))
#
#     choice = int(input())
#     if 1 <= choice <= len(albums):
#         songs_list = albums[choice - 1][SONGS_LIST_INDEX]
#     else:
#         break
#
#     print("Please choose your song: ")
#     for index, (track_number, song) in enumerate(songs_list):
#         print("{}: {}".format(index + 1, song))
#
#     song_choice = int(input())
#     if 1 <= song_choice <= len(songs_list):
#         title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
#     else:
#         break
#
#     print("Playing {}".format(title))
#     print("=" * 40)
#
