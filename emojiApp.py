import streamlit as st 
import joblib 

model = joblib.load(open("model/emojiClassifier.pkl","rb"))

def predict_emotions(sentence):
    results = model.predict([sentence])
    return results[0]

emotions_emoji_dict = {"anger":"😠😡🤬","disgust":"🤮🤢😒", "fear":"😨😱😰", "joy":"😂😀😁", "neutral":"😐😑", "sadness":"😔😢😒", "shame":"😳😨", "surprise":"😮😯😲"}

def main():
    st.title("Emoji Recommendation")
    sentence = st.text_area("Type Sentence Here")
    if st.button('Predict Emoji'):
        prediction = predict_emotions(sentence)
        emoji_icon = emotions_emoji_dict[prediction]
        jsonData = {"predictedEmoji" : emoji_icon}
        st.write(jsonData)

if __name__ == '__main__':
    main()
