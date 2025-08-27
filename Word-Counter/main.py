from WordCounter import WordCounter

try:
    print("***** Word Counter Program *****")
    
    sent = "apple apple apple"
    
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
    print("******* Program End ********")