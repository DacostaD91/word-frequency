
text = "Track your progress with the free "'My Learning'" program here at W3Schools. Log in to your account and start earning points! This is an optional feature. You can study W3Schools without using My Learning."
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", 
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", 
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", 
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", 
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
def remove_non_alpha(textStr):
    newText = ""
    for txt in text:
        if(txt.isalpha() or txt == " "):
            newText += txt.lower()
    return list(newText.split(" "))

def exclude_words(textList, uninteresting_words):
    for uni_txt in uninteresting_words:
        for txtL in textList:
            if txtL == uni_txt:
                textList.remove(uni_txt)
    return textList

def calculate_frequencies(textList):
    textDictionary = {}
    for txtItem in textList:
        if txtItem in textDictionary:
            textDictionary[txtItem] += 1
        else:
            textDictionary[txtItem] = 1
    return textDictionary

textList = remove_non_alpha(text) 

cleaTextList = exclude_words(textList, uninteresting_words)

print(calculate_frequencies(textList))
        

