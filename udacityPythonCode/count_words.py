#!/usr/bin/python
#
# udacity.com Machine Learning readiness assesment assignment
 
print ("\nBegin count_words python module\n")

# initialize python module variables

wordCount = 0

# declare initialize myListOfTuples variable 
myListOfTuples = []
# myTuple = tuple()

def processTuple(word, count, truncatorInteger):
    print ("Begin processTuple function *****")
    print ("\t word passed in is -> %s" % word)
    print ("\t count passed in is -> %s" % count)

    # tuple variable declaration and initialization
    myTuple = tuple()

    # populate the tuple 
    myTuple = (word, count)
    # print(myTuple)    

    # populate list of tuples
    myListOfTuples.append(myTuple)
    # print(myListOfTuples)

    # at this point we have the list of tuples
    # requirements compliance - sort the list desending based on word occurrence count
    # second value in tuple

    # myListOfTuples.sort(key=lambda x: x[1])
    # [('mat', 1), ('bat', 2), ('cat', 3)] - requirents complinace - not sorted descending

    # now descending - note the "-x[1]" replaced "x[1]"
    myListOfTuples.sort(key=lambda x: -x[1])
    # [('cat', 3), ('bat', 2), ('mat', 1)]

    # requirement complinace - truncate the list 
    del myListOfTuples[truncatorInteger:]
    
    print ("End processTuple function\n")


def count_words(s, n):
    print ("\tBegin count_words function")

    # udacity.com directions
    # Return the n most frequently occuring words in s.
    # TODO: Count the number of occurences of each word in s
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)

    saveWord = "" # used to determine if we have a new word - reset word counter
    wordForTuple = "" # word loaded into tuple
    countForTuple = 0 # integer - word count loaded into tuple
    lengthOfString = 0 # how many words were in the data string - used to manage last word use case 
    iterationsThroughLoop = 0 # how many times have we looped - used to manage last word use case

    # save off length of final list
    truncatorInteger = n

    # Echo the passed in string of words 
    print ("\t\t string passed in is -> %s" % s)
    
    # Echo the passed in integer
    print ("\t\t integer passed in is -> %s" % n)

    # split up the string - get the individual words - create the list
    # space argument ' ' passed to split method not needed - it is the default 
    # wordsInString = s.split(' ')
    wordsInString = s.split()
    print ("\t\t wordsInString is -> %s" % wordsInString)

    # Alphabetically sort the words 
    sortedWordsInString = sorted(wordsInString) 
    print ("\t\t sortedWordsInString is -> %s\n" % sortedWordsInString)

    lengthOfString = len(sortedWordsInString)
    print ("\t\t lengthOfString is -> %s\n" % lengthOfString)


    for index, wordInString in enumerate(sortedWordsInString):
        print("\t\t Begin for loop")
        iterationsThroughLoop += 1 
        print ("\t\t\t index is -> %s" % index)
        print ("\t\t\t wordInString is -> %s" % wordInString)
        print ("\t\t\t saveWord is -> %s\n" % saveWord)
        print ("\t\t\t iterationsThroughLoop is -> %s" % iterationsThroughLoop)
        print ("\t\t\t lengthOfString is -> %s" % lengthOfString)
 
        if index == 0:
            print("\t\t Begin if index == 0:")
            print ("\t\t\t wordInString is -> %s" % wordInString)
            saveWord = wordInString
            print ("\t\t\t saveWord is -> %s" % saveWord)
            
            wordCount = 1
            print ("\t\t\t wordCount is -> %s\n" % wordCount)
 

        elif saveWord == wordInString:
            print("\t\t Words the same")
            # print ("\t\t\t wordInString is -> %s" % wordInString)
            # print ("\t\t\t saveWord is -> %s" % saveWord)

            wordCount += 1
            print ("\t\t\t wordCount is -> %s\n" % wordCount)

            # use case - last word is the same as the next to last word
            if iterationsThroughLoop == lengthOfString:
                print("\t\t\t words different, last word")
                processTuple(wordInString, wordCount, truncatorInteger)

        else:
            print("\t\t Words NOT the same")
            # print ("\t\t\t wordInString is -> %s" % wordInString)
            # print ("\t\t\t iterationsThroughLoop is -> %s" % iterationsThroughLoop)
            # print ("\t\t\t lengthOfString is -> %s" % lengthOfString)
            
            # print ("\t\t\t saveWord is -> %s" % saveWord)
            # print ("\t\t\t wordCount is -> %s\n" % wordCount)

            wordForTuple = saveWord
            print ("\t\t\t wordForTuple is -> %s" % wordForTuple)

            countForTuple = wordCount
            print ("\t\t\t countForTuple is -> %s\n" % countForTuple)

            processTuple(wordForTuple, countForTuple, truncatorInteger)

            # reset saveWord for new word 
            saveWord = wordInString
            print ("\t\t\t saveWord is -> %s" % saveWord)

            # reset wordCount for new word
            wordCount = 1
            print ("\t\t\t wordCount is -> %s" % wordCount)

            # use case - last word is different than the next to last word
            if iterationsThroughLoop == lengthOfString:
                print("\t\t\t words different, last word")
                processTuple(wordInString, wordCount, truncatorInteger)
             

#   sortedWordsInString[0]
#   print ("\n\t\t sortedWordsInString[0] is -> %s\n" % sortedWordsInString[0])

#   for word in sortedWordsInString:
#       print ("\t\t word is -> %s" % word)
 
    top_n = myListOfTuples

    print ("\n\tEnd count_words function\n");

    return top_n


def test_run():
    # Call the count_words function of count_words.py python module
    #
    # two arguments passed
    # the string of words
    # integer - how many tuples in returned list
    #
    # Test count_words() with examples
    #
    # print count_words("cat bat mat cat bat cat", 3)
    # count_words_return = count_words("cat bat mat cat bat cat", 3)
    # count_words_return = count_words("cat bat mat", 3)

    # count_words_return = count_words("cat bat mat cat bat cat", 3)
    # [('bat', 2), ('cat', 3), ('mat', 1)]
    
    count_words_return = count_words("betty bought a bit of butter but the butter was bitter", 3)
    # iterative approach - first get the list
    # [('a', 1), ('betty', 1), ('bit', 1), ('bitter', 1), ('bought', 1), ('but', 1), ('butter', 2), ('of', 1), ('the', 1), ('was', 1)]

    # list sorted by word occurence integer
    # [('butter', 2), ('a', 1), ('betty', 1), ('bit', 1), ('bitter', 1), ('bought', 1), ('but', 1), ('of', 1), ('the', 1), ('was', 1)]

    # requirements fully implemented - truncate based on integer - 3
    # [('butter', 2), ('a', 1), ('betty', 1)]

    # use case - last word (was) matched prvious word 
    # count_words_return = count_words("betty bought a bit of butter but the butter was bitter was", 3)
    # [('a', 1), ('betty', 1), ('bit', 1), ('bitter', 1), ('bought', 1), ('but', 1), ('butter', 2), ('of', 1), ('the', 1), ('was', 2)]

    print ("count_words return value is -> %s\n" % count_words_return);

 
# udacity syntax
#if __name__ == '__main__':
#    test_run()

# customary invoke of function within this module
# invoke, call the test_run function
# no arguments passed to the test_run function
test_run()

print ("End count_words python module\n\n\n\n")

 
##Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
##[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
## 
##Begin count_words python module
##
##	Begin count_words function
##		 string passed in is -> betty bought a bit of butter but the butter was bitter
##		 integer passed in is -> 3
##		 wordsInString is -> ['betty', 'bought', 'a', 'bit', 'of', 'butter', 'but', 'the', 'butter', 'was', 'bitter']
##		 sortedWordsInString is -> ['a', 'betty', 'bit', 'bitter', 'bought', 'but', 'butter', 'butter', 'of', 'the', 'was']
##
##		 lengthOfString is -> 11
##
##		 Begin for loop
##			 index is -> 0
##			 wordInString is -> a
##			 saveWord is -> 
##
##			 iterationsThroughLoop is -> 1
##			 lengthOfString is -> 11
##		 Begin if index == 0:
##			 wordInString is -> a
##			 saveWord is -> a
##			 wordCount is -> 1
##
##		 Begin for loop
##			 index is -> 1
##			 wordInString is -> betty
##			 saveWord is -> a
##
##			 iterationsThroughLoop is -> 2
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> a
##			 countForTuple is -> 1
##
##Begin processTuple function *****
##	 word passed in is -> a
##	 count passed in is -> 1
##End processTuple function
##
##			 saveWord is -> betty
##			 wordCount is -> 1
##		 Begin for loop
##			 index is -> 2
##			 wordInString is -> bit
##			 saveWord is -> betty
##
##			 iterationsThroughLoop is -> 3
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> betty
##			 countForTuple is -> 1
##
##Begin processTuple function *****
##	 word passed in is -> betty
##	 count passed in is -> 1
##End processTuple function
##
##			 saveWord is -> bit
##			 wordCount is -> 1
##		 Begin for loop
##			 index is -> 3
##			 wordInString is -> bitter
##			 saveWord is -> bit
##
##			 iterationsThroughLoop is -> 4
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> bit
##			 countForTuple is -> 1
##
##Begin processTuple function *****
##	 word passed in is -> bit
##	 count passed in is -> 1
##End processTuple function
##
##			 saveWord is -> bitter
##			 wordCount is -> 1
##		 Begin for loop
##			 index is -> 4
##			 wordInString is -> bought
##			 saveWord is -> bitter
##
##			 iterationsThroughLoop is -> 5
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> bitter
##			 countForTuple is -> 1
##
##Begin processTuple function *****
##	 word passed in is -> bitter
##	 count passed in is -> 1
##End processTuple function
##
##			 saveWord is -> bought
##			 wordCount is -> 1
##		 Begin for loop
##			 index is -> 5
##			 wordInString is -> but
##			 saveWord is -> bought
##
##			 iterationsThroughLoop is -> 6
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> bought
##			 countForTuple is -> 1
##
##Begin processTuple function *****
##	 word passed in is -> bought
##	 count passed in is -> 1
##End processTuple function
##
##			 saveWord is -> but
##			 wordCount is -> 1
##		 Begin for loop
##			 index is -> 6
##			 wordInString is -> butter
##			 saveWord is -> but
##
##			 iterationsThroughLoop is -> 7
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> but
##			 countForTuple is -> 1
##
##Begin processTuple function *****
##	 word passed in is -> but
##	 count passed in is -> 1
##End processTuple function
##
##			 saveWord is -> butter
##			 wordCount is -> 1
##		 Begin for loop
##			 index is -> 7
##			 wordInString is -> butter
##			 saveWord is -> butter
##
##			 iterationsThroughLoop is -> 8
##			 lengthOfString is -> 11
##		 Words the same
##			 wordCount is -> 2
##
##		 Begin for loop
##			 index is -> 8
##			 wordInString is -> of
##			 saveWord is -> butter
##
##			 iterationsThroughLoop is -> 9
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> butter
##			 countForTuple is -> 2
##
##Begin processTuple function *****
##	 word passed in is -> butter
##	 count passed in is -> 2
##End processTuple function
##
##			 saveWord is -> of
##			 wordCount is -> 1
##		 Begin for loop
##			 index is -> 9
##			 wordInString is -> the
##			 saveWord is -> of
##
##			 iterationsThroughLoop is -> 10
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> of
##			 countForTuple is -> 1
##
##Begin processTuple function *****
##	 word passed in is -> of
##	 count passed in is -> 1
##End processTuple function
##
##			 saveWord is -> the
##			 wordCount is -> 1
##		 Begin for loop
##			 index is -> 10
##			 wordInString is -> was
##			 saveWord is -> the
##
##			 iterationsThroughLoop is -> 11
##			 lengthOfString is -> 11
##		 Words NOT the same
##			 wordForTuple is -> the
##			 countForTuple is -> 1
##
##Begin processTuple function *****
##	 word passed in is -> the
##	 count passed in is -> 1
##End processTuple function
##
##			 saveWord is -> was
##			 wordCount is -> 1
##			 words different, last word
##Begin processTuple function *****
##	 word passed in is -> was
##	 count passed in is -> 1
##End processTuple function
##
##
##	End count_words function
##
##count_words return value is -> [('butter', 2), ('a', 1), ('betty', 1)]
##
##End count_words python module
