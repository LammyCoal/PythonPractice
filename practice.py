#How to write to a file

liked_songs = {
    'wizkid': 'caro',
    'davido': 'Aye',
    'runtown': 'mad over you',
    'olamide': 'illuminati'
}

def write_liked_songs_to_file(liked_songs, filename):
    with open(filename,'w') as file:
        file.write('liked_songs:\n')
        for artists, songs in liked_songs.items():
            contents = f" {artists} by {songs}\n"
            answer = file.write(contents)



write_liked_songs_to_file(liked_songs, 'FileIO song')



# How to seek and truncate messages in a file
sent_message = 'Hey there!, This is a secret message'
with open('secret','r+') as file:
    file.write(sent_message)

with open('secret', 'r+') as file:
    original_message = file.read()
    file.seek(0)
    # Modify the message to simulate unsending
    unsent_message = 'This message has been unsent.'
    file.truncate(len(unsent_message))
    file.write(unsent_message)
print(f'Original message is:- ( {sent_message})')
print(f'deleted message is:- ({unsent_message})')

