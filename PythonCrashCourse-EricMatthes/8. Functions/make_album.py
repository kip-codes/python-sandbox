# File: make_album.py
# Project: PythonCrashCourse
# Local author: kevinip
# Created on 11/09/2017 at 6:37 PM
#
# For inquiries about the file please contact the author.

# makeAlbum(): Builds a dictionary describing a music album
# Parameters:
#   1. Artist name
#   2. Album title
#   3. Number of tracks (optional)
# Return:
#   dictionary
def makeAlbum(artist, title, numTracks=0):
    if artist == '' or title == '':
        print('Invalid parameters.')
        return None
    return {'artist': artist, 'title': title, 'numTracks': numTracks}

def createAlbum():
    artist = input("Please enter the artist: ")
    title = input("Please enter the title of the album: ")
    try:
        numTracks = int(input("If you know the number of tracks on the album, please enter it now (0 for unknown): "))
        if numTracks < 0:
            raise ValueError
    except ValueError:
        print('Please enter a numerical value for the number of tracks.')
    else:
        if numTracks == 0:
            numTracks = None

    return {'artist': artist, 'title': title, 'numTracks': numTracks}

if __name__ == '__main__':
    print('* ' * 20)
    tiy8_7 = '8-7. User Albums:\nWrite a function called makeAlbum() that builds a dictionary describing a music album.' \
             '\nThe function should take in an artist name and an album title, and it should return a dictionary ' \
             'containing these two pieces of information.\nUse the function to make three dictionaries representing ' \
             'different albums.\nAdd an optional parameter that allows you to store the number of tracks on an album.\n'
    print(tiy8_7)

    print('\n\'albumA\' will be a standard call without the optional parameter.')
    albumA = makeAlbum('Mariah Carey', 'Emotion')
    print('albumA:', albumA)

    print('\n\'albumB\' will be a standard call with a value for the optional parameter.')
    albumB = makeAlbum('Carly Rae Jepsen', 'Emotion Side B', 5)
    print('albumB:', albumB)

    print('\n\'albumC\' will be a call which provides blank parameters for the call.')
    albumC = makeAlbum('noArtist', '')
    print('albumC:', albumC)

    print('\ncreateAlbum() will prompt the user for input.')
    print(createAlbum())