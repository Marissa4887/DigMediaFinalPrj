# Who Wants to be a Millionare?
# By Marissa Salas for Programming Digital Media
# creation of classes game, player, question.

# version 1: list of titles, player selects author
# version 2: list of paragraph, player selects title and author

# test dataset dictionary - a collection which is unordered, changeable and does not allow duplicates.
books = {
    1: {'title': 'The river and the source',
        'author': "Margaret Okoth",
        'paragraphs': ["Here I am ", "Second paragraph"]},
    2: {'title': 'Romeo and Juliet',
        'author': "Shakespeare",
        'paragraphs': ["Shakespear paragraph1 ", "Second shakes paragraph"]},
    3: {'title': 'The Alchemist',
        'author': "Paulo Coelho",
        'paragraphs': ["Alchemist paragraph1 ", "Alchemist shakes paragraph"]},
    4: {'title': 'Enemy of the People',
        'author': "Ibsen",
        'paragraphs': ["Enemy paragraph1 ", "Second Enemy paragraph"]},
    5: {'title': 'Things Fall Apart',
        'author': "Chinua Achebe",
        'paragraphs': ["But the young lad calls you father ", "Second thins fall apart paragraph"]}
}

#"Who wants to play, Who Wants to be a Millionare? "

#%%
import random
# import os.path
# booklist_FILENAME = "words.txt"

# def load_book(silent=False):
#     """
#     Returns a list of valid words. Words are strings of lowercase letters.
    
#     Depending on the size of the word list, this function may
#     take a while to finish.
#     """
#     if(not silent):
#       print("Loading list from file...")
#     global booklist_FILENAME
#     # inFile: filek
#     if os.path.exists("psets/4/words.txt"):
#       booklist_FILENAME = "psets/4/"+booklist_FILENAME
#     inFile = open(booklist_FILENAME, 'r')

#     # line: string
#     line = inFile.readline()
#     # booklist: list of strings
#     booklist = line.split()
#     print("  ", len(booklist), "words loaded.")
#     return booklist




# def choose_book(booklist):
#     """
#     booklist (list): paragraph (strings)
    
#     Returns a paragraph from booklist at random
#     """
#     return random.choice(booklist)

#%%
rules = "\nEnter your name to start. You start with $100. For each correct answer you double your money. \nAfter 15 correct guesses you win, one Million dollars!" 


# A Class is "blueprint" (ie Car) for creating objects like a cookie cutter to make cookies (many objects)
# think of the __init__ assigns properties (ie color)and the functions inside are like the behaviors (ie speed)
# this gets the players name
class Player:
    def __init__(self, name):
        self.name = name
        print(f"{name} are you ready to play Who wants to be a Millionare?")

#this selects the questions
class Question:
    def __init__(self, quizID, random1, random2, random3):
        self.quizID = quizID
        my_list = [quizID, random1, random2, random3]

        a = random.choice(my_list)
        my_list.remove(a)

        b = random.choice(my_list)
        my_list.remove(b)

        c = random.choice(my_list)
        my_list.remove(c)

        d = random.choice(my_list)
        my_list.remove(d)

        # print("Choice C is: ", c)

        # self.options = {
        #     a: "Romeo and Juliet",
        #     b: "The river and the source",
        #     c: "The Alchemist",
        #     d: "Enemy of the People"
        # }
        self.options = {
            a: books[a]['author'],
            b: books[b]['author'],
            c: books[c]['author'],
            d: books[d]['author']
        }
        # self.options = {
        #     a: "Shkespear",
        #     b: "The river and the source",
        #     c: "The Alchemist",
        #     d: "Enemy of the People"
        # }
        self.answer = quizID
        
class Game:
    # def __init__(self, rules, users_choice, correct_answer): handles the basics of the game
    def __init__(self):
        # self.rules = rules
        # self.users_choice = users_choice
        # self.correct_answer = correct_answer
        self.level = 0
        self.player = None
        self.prize = ["$100","$200","$300"] #, "$500", "$1,000", "$2,000", "$4,000","$8,000","$16,000","$32,000", "$64,000", "$125,000", "$250,000", "$500,000", "$1 Million"]

    def start(self):
        print(rules)
        players_name = input("Enter your name: ")
        self.player = Player(players_name)

    def end_game(self):
        print("The Game has ended")
        print(f"You got to level {self.level}")

    def process_answer(self, question, a, b, c, d):
        choices = {
            'A': a,
            'B': b,
            'C': c,
            'D': d
        }
        user_answer = input("What's your final answer? (ABCD): ")
        user_answer = str.lower(books[choices[user_answer]]['author'])
        correct_answer = books[question.answer]['author']
        # print("Correct answer ", correct_answer)
        correct_answer = str.lower(correct_answer)

        if(user_answer == correct_answer):
            self.level += 1
            print("Congratulations, you moved to next level!")
        else:
            print("Sorry that was incorrect.")
            self.end_game()


        
    def process_question(self):
        a = 1
        b = 3
        c = 4
        d = 2

        question = Question(1, 3, 4, 2)
        print(f"Who is the author of the book: {books[question.quizID]['title']}")
        print(f"Is it: \nA: {books[a]['author']}\nB: {books[b]['author']}\nC: {books[c]['author']}\nD: {books[d]['author']}")
        self.process_answer(question, a, b, c, d)
        
    

    # def winner_loser(self):
    #     pass

    # def score(self):
    #     pass

    # def award(self):
    #     pass





# question = Question(3, 2, 4, 1)

game = Game()
game.start()
game.process_question()



# class Player:
#     def __init__(self, name):
#         self.name = name

#     def pick_answer(self):


    
