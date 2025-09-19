from WordCounter import WordCounter

try:
    print("***** Word Counter Program *****")
    print()
    
    sent = "the quick brown fox jumps over the lazy dog the dog was not amused"
    
    counter = WordCounter(sent)
    
    counter.count_word()
    counter.show_count()
        
    
except TypeError as e:
    print("Error: ", e)
except ValueError as e:
    print("Error: ", e)
except Exception:
    print("An Error Occured")
finally:
    print()
    print("******* Program End ********")