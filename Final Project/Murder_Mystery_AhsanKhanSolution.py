#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 18:33:37 2019

@author: Ahsan
"""

murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."

lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"
 
myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a 'walk'. A 'walk' with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."
 
gregg_t_fishy_intro = "A good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young. An adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might ask? Why, fishing for compliments of course! I have a stunning pair of radiant blue eyes. They will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television. I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life. Every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on A Brand New Jay. It certainly seems like a grand time to explore life and love."
 


def get_average_sentence_length(text):
    text_without_questionmark = text.replace('?','.')
    text_without_exclamation = text_without_questionmark.replace('!','.')
    #Next line corrects the length of sentences_in_text
    text_without_last_fullstop = text_without_exclamation[:-1]
    sentences_in_text = text_without_last_fullstop.split('.')
    #Next is to join 2 sentences if they were seperated by '.' in case of a middle name. 
    #Ex: Michael B. Jordan
    i = 0
    while i < len(sentences_in_text):
        if sentences_in_text[i][-1].islower() == False and \
           sentences_in_text[i][-2].isalpha() == False:
               sentences_in_text[i] = sentences_in_text[i] + sentences_in_text[i+1]
               sentences_in_text.pop(i+1)
        i += 1
    words_in_sentences = [i.split() for i in sentences_in_text]
    sentence_lengths = [len(j) for j in words_in_sentences]
    average = (sum(sentence_lengths))/(len(sentences_in_text))
    return average
    
def prepare_text(text):
    text1 = text.lower()
    to_replace = [".", ",", "?", "!", "\"","\'"]
    for i in to_replace:
        if i in text1:
            text1 = text1.replace(i,'')
    text1 = text1.split()
    return text1
    
print(prepare_text("Where did you go, friend?! We nearly saw each other. I'm new!"))

def build_frequency_table(corpus):
    frequency_table = {}
    for i in corpus:
        frequency_table[i] = corpus.count(i)
    return frequency_table

print(build_frequency_table(['do', 'you', 'see', 'what', 'i', 'see']))

def ngram_creator(text_list):
    final = []
    i = 0
    while i < len(text_list):
        if i == range(len(text_list))[-1]:
            break
        else:
            final.append(text_list[i] + ' ' + text_list[i+1])
        i+= 1
    return final

ex = ['what', 'in', 'the', 'world', 'is', 'going', 'on']
print(ngram_creator(ex))
    
def frequency_comparison(table1, table2):
    appearances = 0
    mutual_appearances = 0
    for i in table1.keys():
        if i in table2.keys():
            if table1.get(i) < table2.get(i):
                mutual_appearances += table1.get(i)
                appearances += table2.get(i)
            elif table1.get(i) == table2.get(i):
                mutual_appearances += table1.get(i)
                appearances += table1.get(i)
            else:
                mutual_appearances += table2.get(i)
                appearances += table1.get(i)
        else:
            appearances += table1.get(i)
    for j in table2.keys():
        if j not in table1.keys():
            appearances += table2.get(j)
    score = mutual_appearances/appearances
    return score
                
    
def percent_difference(classobject1, classobject2):
    if type(classobject1) is TextSample and type(classobject2) is TextSample:
        value1 = classobject1.average_sentence_length
        value2 = classobject2.average_sentence_length
        num = abs(value1-value2)
        den = (value1+value2)/2
        percentdiff = num/den
    return percentdiff

def find_text_similarity(classobject1, classobject2):
    if type(classobject1) is TextSample and type(classobject2) is TextSample:
        sentence_length_difference = percent_difference(classobject1, classobject2)
        sentence_length_similarity = abs(1 - sentence_length_difference)
        word_count_similarity = frequency_comparison(classobject1.word_count_frequency, classobject2.word_count_frequency)
        ngram_similarity = frequency_comparison(classobject1.ngram_frequency, classobject2.ngram_frequency)
        final_answer = (sentence_length_similarity + word_count_similarity + ngram_similarity)/3
    return final_answer
        
    
class TextSample:
    def __init__(self, text, author):
        self.raw_text = text
        self.average_sentence_length = get_average_sentence_length(text)
        self.author = author
        self.prepared_text = prepare_text(text)
        self.word_count_frequency = build_frequency_table(self.prepared_text)
        self.ngram_frequency = build_frequency_table(ngram_creator(self.prepared_text))
    def __repr__(self):
        who_is_author = "The Author's name is {Auth}".format(Auth=self.author)
        what_is_length = "The average sentence length is {Leng}".format(Leng=self.average_sentence_length)
        Answer = [who_is_author, what_is_length]
        return ('\n'.join(Answer))
    
murderer_sample = TextSample(murder_note, 'Murderer')
print(murderer_sample)
lily_sample = TextSample(lily_trebuchet_intro, 'Lily Trebuchet')
print(lily_sample)
myrtle_sample = TextSample(myrtle_beech_intro, 'Myrtle Beech')
print(myrtle_sample)
gregg_sample = TextSample(gregg_t_fishy_intro, 'Gregg T Fishy')
print(gregg_sample)

#Rendering the Results
contestants = [lily_sample.author,
               myrtle_sample.author,
               gregg_sample.author
        ]
similarity_scores = [find_text_similarity(murderer_sample, lily_sample), 
               find_text_similarity(murderer_sample, myrtle_sample), 
               find_text_similarity(murderer_sample, gregg_sample)
               ]

for i in range(3):
    print("The Author's name is: {a}".format(a=contestants[i]))
    print("Their similarity score to the murder letter is: {s}".format(s=similarity_scores[i]))
    
#Who Dunnit?
def WhoDunnit():
    results = {key:value for key,value in zip(contestants, similarity_scores)}
    top_score = 0
    for score in results.values():
        if score > top_score:
            top_score = score
    for contestant, score1 in results.items():
        if top_score == score1:
            return contestant
           
print(WhoDunnit())

    
    
    
   


    



    
    
    
    
     
 
 
 
 
 
 
 