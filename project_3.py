import string
punct = string.punctuation.replace("'", "")
translate = str.maketrans("", "", punct)
file_text = "text_for_project_3.txt"
try:
    with open(file_text, "r") as file:
        content = file.read()
        lines = content.count(
            "\n") + (1 if not content.endswith("\n") and content else 0)
        words = lines + content.count(" ")
        characters = len(content)
        cleaned_text = content.lower().translate(translate).split()
        
        text = {}
        for i in cleaned_text:
                    if i not in text:
                        text[i] = 1
                    else:
                        text[i] += 1
        
        most = sorted(text.items(), key=lambda x: x[1], reverse=True)
        top1, value1 = most[0]
        top2, value2 = most[1]
        top3, value3 = most[2]
        top4, value4 = most[3]
        top5, value5 = most[4]
except FileNotFoundError:
    print("file didn't found")
except PermissionError:
    print("permission to that file is denied")
except Exception:
    print("something's wrong with reading file")
    
print(f" lines: {lines}\n words: {words}\n characters: {characters}\n top 5 Most common words:\n {top1} : {value1}\n {top2} : {value2} \n {top3} : {value3}\n {top4} : {value4} \n {top5} : {value5}")