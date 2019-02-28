# Author: Branden Kim
# Description: Returns all unique words within a given text
#              normalizing to all lowercase and removing punctuation
# 2a


text="One fish Two fish Red fish Blue fish. Black fish Blue fish Old fish New fish. This one has a little star. This one has a little car. Say! What a lot Of fish there are. Yes. Some are red. And some are blue. Some are old. And some are new. Some are sad. And some are glad. And some are very, very bad. Why are they Sad and glad and bad? I do not know. Go ask your dad. Some are thin. And some are fat. The fat one has A yellow hat. From there to here, from here to there, Funny things Are everywhere. Here are some Who like to run."  

import string

def find_unique(text):
    exclude = set(string.punctuation)
    stripped_text = ''.join(ch for ch in text if ch not in exclude)
    return list({word.lower() for word in stripped_text.split(' ')})


if __name__ == '__main__':
    unique_words = find_unique(text)
    print(unique_words)
    print(len(unique_words))
