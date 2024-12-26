import random
import os
import math
# create list for store fruits names
fruit_names = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 
        'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon', 'blueberry', 'cranberry', 'grapefruit', 'lime', 'pear',
        'plum', 'apricot', 'blackberry', 'coconut', 'guava', 'kiwifruit', 'lychee', 'pomegranate', 'tomato', 'avocado', 'boysenberry', 
        'clementine', 'kiwano', 'mangosteen', 'persimmon', 'tamarind', 'bilberry', 'currant', 'loganberry', 'passionfruit', 'rhubarb', 
        'uglifruit', 'cantaloupe', 'dragonfruit', 'elderflower', 'feijoa', 'grapevine']

# create a list for store flowers names
flower_names = ['rose', 'tulip', 'daisy', 'lily', 'sunflower', 'carnation', 'orchid', 'jasmine', 'marigold', 'hibiscus', 'daffodil', 'violet',
        'peony', 'chrysanthemum', 'dahlia', 'zinnia', 'aster', 'gerbera', 'pansy', 'snapdragon', 'cosmos', 'lupine', 'gladiolus', 
        'anemone', 'freesia', 'petunia', 'buttercup', 'larkspur', 'hyacinth', 'narcissus', 'columbine', 'bluebell', 'foxglove', 
        'primrose', 'bougainvillea', 'sweet pea', 'lantana', 'borage', 'lavender', 'iris', 'poppy', 'azalea', 'crocus',
        'geranium', 'hellebore', 'tansy', 'yarrow']

# create a list for storing animals name
animal_names = ['dog', 'cat', 'elephant', 'lion', 'tiger', 'giraffe', 'zebra', 'panda', 'kangaroo', 'koala', 'hippo', 'rhino', 'cheetah',
           'leopard', 'gorilla', 'monkey', 'sloth', 'otter', 'hedgehog', 'chimpanzee', 'penguin', 'dolphin', 'whale', 'seal', 'crocodile',
           'alligator', 'snake', 'lizard', 'turtle', 'octopus', 'jellyfish', 'shark', 'lobster', 'crab', 'starfish', 'seahorse', 'flamingo',
           'ostrich', 'parrot', 'peacock', 'pigeon', 'sparrow', 'butterfly', 'bee', 'ant', 'spider', 'scorpion']

# create a list for store birds name
bird_names = ['sparrow', 'robin', 'hawk', 'dove', 'crow', 'bluejay', 'finch', 'pigeon', 'parrot', 'owl', 'eagle', 'swan', 'peacock', 'woodpecker',
          'canary', 'seagull', 'hummingbird', 'kingfisher', 'raven', 'turkey', 'pelican', 'heron', 'flamingo', 'puffin', 'albatross', 
          'quail', 'magpie', 'vulture', 'stork', 'kiwi', 'cuckoo', 'penguin', 'ostrich', 'cormorant', 'toucan', 'nightingale', 'swallow', 
          'warbler', 'wren', 'grouse', 'gannet', 'shrike', 'oriole', 'bulbul', 'hoopoe', 'kookaburra', 'titmouse', 'goldfinch']

# create a list for store boliwood acters names
bollywood_actors = [
    'shahrukhkhan', 'salmankhan', 'aamirkhan', 'akshaykumar', 'hrithikroshan',
    'ranbirkapoor', 'ranveersingh', 'amitabhbachchan', 'saifali', 'varundhawan',
    'sidharthmalhotra', 'ajaydevgn', 'shahidkapoor', 'arjunkapoor', 'farhanakhtar',
    'ranvirsingh', 'sanjaydutt', 'anilkapoor', 'sunielshetty', 'nawazuddinsiddiqui',
    'irrfankhan', 'naseeruddinsiddiqui', 'pareshrawal', 'ompuri', 'manojbajpayee',
    'abhisbachchan', 'emraanhashmi', 'adityaroy', 'tigerrajput', 'sushantkaushal',
    'vickykhurrana', 'ayushmannaryan', 'kartikabraham', 'johnkapoor', 'rishikumar',
    'dharmendradeol', 'sanjeevkumar', 'rajeshkhanna', 'shaktikumar', 'mohnishkumar',
    'bomankumar', 'nanakumar', 'kunalkumar', 'jackiekumar', 'rishikumar',
    'ranakumar', 'nawazkumar', 'pulkitkumar'
    ]

# create a list for store some cricaters name
cricketer_names = [
    'sachintendulkar', 'viratkohli', 'donbradman', 'vivianrichards',
    'imrankhan', 'wasimakram', 'brianlara', 'kapildev', 'jacqueskallis',
    'shanewarne', 'msdhoni', 'glennmcgrath', 'adamgilchrist',
    'rahuldravid', 'anilkumble', 'allandonald', 'waqaryounis',
    'curtlyambrose', 'rickyponting', 'brettlee', 'sunilgavaskar',
    'richardhadlee', 'graemepollock', 'clivelloyd', 'garysobers',
    'javedmiandad', 'mohammadyousuf', 'michaelholding', 'dennislillee',
    'gordongreenidge', 'ianbotham', 'virendersehwag', 'kevinpietersen',
    'muthiahmuralitharan', 'andyflower', 'abdevilliers', 'hashimaml',
    'kumarsangakkara', 'mohammadamir', 'tamimiqbal', 'rosstaylor',
    'kanewilliamson', 'joeroot', 'stevesmith', 'benstokes',
    'babarazam', 'quintondecock', 'jaspritbumrah', 'kagisorabada'
    ]

# create a list for store asian_countries name
asian_countries = [
    'afghanistan', 'armenia', 'azerbaijan', 'bahrain', 'bangladesh',
    'bhutan', 'brunei', 'cambodia', 'china', 'cyprus', 'georgia',
    'india', 'indonesia', 'iran', 'iraq', 'israel', 'japan', 'jordan',
    'kazakhstan', 'kuwait', 'kyrgyzstan', 'laos', 'lebanon', 'malaysia',
    'maldives', 'mongolia', 'myanmar', 'nepal', 'northkorea', 'oman',
    'pakistan', 'philippines', 'qatar', 'saudiarabia', 'singapore',
    'southkorea', 'srilanka', 'syria', 'taiwan', 'tajikistan',
    'thailand', 'timorleste', 'turkmenistan', 'unitedarabemirates',
    'uzbekistan', 'vietnam', 'yemen'
    ]

# create 5 letters word list
_5letter_words = [
    'apple', 'beach', 'crisp', 'daisy', 'ember',
    'flame', 'grape', 'hazel', 'ivory', 'jolly',
    'karma', 'lemon', 'mango', 'noble', 'ocean',
    'peach', 'quilt', 'raven', 'sunny', 'tiger',
    'ultra', 'vivid', 'waltz', 'xenon', 'yacht',
    'zebra', 'amber', 'blaze', 'coral', 'dwarf',
    'elixir', 'fable', 'globe', 'honey', 'iris',
    'jumbo', 'kudos', 'lunar', 'mirth', 'nexus',
    'opal', 'piano', 'quack', 'risky', 'salsa',
    'tango', 'unity', 'vital', 'witty', 'xerox'
]

# 7 letter words list
_7letter_words = [
    'abandon', 'beneath', 'chimney', 'dazzled', 'eclipse',
    'frosted', 'glimpse', 'humbled', 'inquiry', 'jovial',
    'kernels', 'laziest', 'muffled', 'nourish', 'outpost',
    'plunged', 'quizzes', 'rejoice', 'schemer', 'tangled',
    'unearth', 'vintage', 'whisper', 'xeroxed', 'yielded',
    'zealous', 'allegro', 'brevity', 'cabbage', 'diluted',
    'exclaim', 'florist', 'grumble', 'hazards', 'ignited',
    'jubilee', 'kneecap', 'languid', 'memento', 'nurtured',
    'outlook', 'plaster', 'quaintly', 'renewal', 'scuttle',
    'turbine', 'upright', 'victory', 'whistle', 'xylitol'
]

# 9 letter wods list
_9letter_words = [
    'abandoned', 'butterfly', 'chocolate', 'delicious', 'elephant', 
    'fireplace', 'gratitude', 'happiness', 'incredible', 'jewellery',
    'knowledge', 'landscape', 'mysterious', 'notebook', 'obsession', 
    'paradise', 'question', 'rainbow', 'sunflower', 'treasure',
    'umbrella', 'victorious', 'wonderful', 'xylophone', 'yearning',
    'zeppelin', 'adventure', 'beautiful', 'celebrate', 'dandelion', 
    'enthusiasm', 'fascinate', 'gorgeous', 'harmonize', 'illuminate', 
    'joviality', 'kaleidoscope', 'labyrinth', 'magnificent', 'nourishment', 
    'optimistic', 'passionate', 'quintessence', 'radiance', 'serendipity', 
    'tantalize', 'unforgettable'
    ]

#chose between thos list using a list
list_names = ['_9letter_words','_7letter_words','_5letter_words','asian_countries','cricketer_names','bollywood_actors'
         ,'bird_names','animal_names','flower_names','fruit_names']
list_name = random.choice(list_names)

def cls(): # clear tha screen
    os.system('cls' if os.name == 'nt' else 'clear')

#create a global score for storeing players store
score = 0

# store player name
name = input('Enter Your Name : ')
print(f'Welcome To Cross Word Game {name} \n\t Good Luck!\n')

def game(): # run the game
  global list_name
  #choce a word randomly
  word = random.choice(eval(list_name))
  chences = math.floor(len(word)*1.5)
  print(f'HINT : The word is {list_name} and it has {len(word)} letters And You Have {chences} Chences To Win !')
  print(' ----- Guess the word -----\n')
  guesses = ''
  while chences > 0:
    faild = 0 
    point = 0
    for i in range(len(word)):
        if i%3 == 1:
            guesses+=word[i]
    for char in word: # match all letter in word from guesses
      if char in guesses:
        print(char,end=' ') #if letter match from word then print the letter
        point+=1
      else:
        print('_',end=' ') # or print '_'
        faild += 1

    if faild == 0: # if all letter match then exsecute this section
      global score
      score += (point*2) + (chences *2) # store point in score
      print(f'\n\tCongratulations! {name} You Win The Game Youre Score is {(point * 2) + (chences * 2)}')
      qs = input(f'\n\tDo You Want To Play Next Label {name} (y/n) : ')
      if qs.lower() == 'y':
        list_name = random.choice(list_names)
        cls() # clear screen
        game()
      else:
        print('\n\t-------Thank You For Playing---------')
        print(f'\t-------{name} You Final Score is : {score} ---------')

        ex = input('\nQ to exit : ')
        if ex.lower() == 'q':
          quit() # exit the game
      break
      
    guess = input('\n\nGuess a character : ')
    # check some condition
    if len(guess) > 1: 
      print('\tPlease Enter Only One Character')
      continue
    elif guess in guesses: 
      print('\tYou have already guessed this character! Chose Another Letter')
      continue
    elif not guess.isalpha():
      print('\tPlease Enter Only Alphabets!')
      continue
    else:
      guesses+= guess.lower() # store all letter in a variable

    if guess not in word: # if letter not match then  print this stetment
      chences -= 1
      print('\tWrong Guess')
      print(f'You Have {chences} More Guesses To Win!')

    if chences == 0:        
      print(f'\n\t{name} You Lose The Game Your Point is {point*2}')
      print('The word is:',word)
      qs = input(f'\n\tDo You Want To Play Again {name} (y/n) : ')
      if qs.lower() == 'y':
        cls() # clear screen
        game()
      else:
        print('\n\t-------Thank You For Playing---------')
        score+=(point*2)
        print(f'\t-------{name} You Final Score is : {score} ---------')
        
        ex = input('\nQ to exit : ')
        if ex.lower() == 'q':
          quit() # exit the game
      break
      

if __name__ == "__main__":
    game()

            