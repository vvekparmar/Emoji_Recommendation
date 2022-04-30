import sys
import joblib 
model = joblib.load(open("model/emojiClassifier.pkl","rb"))

def predict_emotions(sentence):
    results = model.predict([sentence])
    return results[0]

emotions_emoji_dict = {"anger":"😠😡🤬", "disgust":"🤮🤢😒", "fear":"😨😱😰", "joy":"😂😀😁", "neutral":"😐😑", "sadness":"😔😢😒", "shame":"😳😨", "surprise":"😮😯😲"}

def main():
        prediction = predict_emotions(sys.argv[1])
        emoji_icon = emotions_emoji_dict[prediction]
        print(emoji_icon)
    
if __name__ == '__main__':
    main()
