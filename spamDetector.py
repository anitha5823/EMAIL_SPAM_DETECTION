import pickle
import streamlit as st


model = pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))

def main():
	st.title("Email spam classifier")
	#st.subheader("build with streamlit and python")
	msg=st.text_input("Enter text:")
	if st.button("predict"):
		data=[msg]
		vect=cv.transform(data).toarray()
		prediction=model.predict(vect)
		result=prediction[0]
		if result==1:
			st.error("This is a SPAM mail")
		else:
			st.error("This is a HAM mail")


main()