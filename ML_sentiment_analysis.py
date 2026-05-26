import nltk # a library used in programs related to text
nltk.data.path.append("C:\\Users\\Suhana Panda\\AppData\\Roaming\\nltk_data")
nltk.download("movie_reviews")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt")
import random # used for shuffling between values
import string # a module which contains all the function for converting something to string
import pickle # used to store the trained module here
from nltk.corpus import movie_reviews,stopwords # this will load the movie reviews from the dataset and the stopwords(all the punctuations and connectors) 
from nltk.stem import WordNetLemmatizer # this will put every text into it's root word so that they all can be treated the same by the computer
from nltk.tokenize import word_tokenize # this will split a sentence into sepreate words or strings
from sklearn.model_selection import train_test_split # sklearn is the library used to train a model. train_test_split will make two variables one will be to train the model and the other will be to test the model
from sklearn.feature_extraction.text import TfidfVectorizer # the model will extract the text or the movie reviews and then it will convert all of it to numbers(0 & 1) because computers only understand binary data
from sklearn.linear_model import LogisticRegression # it is used to predict the outcome like if yes then it will show 1 and if no it will be 0
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix # it is used to tell the accuracy of the results like how accurate were the scores,how was the report

documents=[] # an empty list where all the data will be stored
for category in movie_reviews.categories(): # creates a variable(category) which contains the data of the categories field in the movie reviews dataset
    for fileid in movie_reviews.fileids(category): # creates a variable(fileid) which will store the ids or reviews(movie1,movie2) of the above categories for the dataset
        documents.append((movie_reviews.raw(fileid),category)) # after the above storing,documents variable will add the fileid and category which were stored from the above lines
random.shuffle(documents) # now the data needed is stored in the variable and it will now be shuffled so that the order of the results is not always in the same sequence
texts=[doc[0] for doc in documents] # it will seperate the first part from the documents list which is the reviews and store it in text variable
labels=[doc[1] for doc in documents] # it will seperate the second part from the documents list which is the label o wheter the movie is good or bad and store it in label variable
lemmatizer=WordNetLemmatizer() # this will put the data ahead(not written yet) in the code in it's root word and save it in this variable
stop_words=set(stopwords.words("english")) # this will remove all the stopwords present in the english language and set is used to remove duplications(no repetition).
def preprocess(text): # this is a function defined which will have a variable as text.
    tokens=word_tokenize(text.lower()) # this will convert all the text into lowercase and save it in the variable tokens.
    cleaned=[] # an empty list which will store all the cleaned data.
    for word in tokens: # a for loop which will run through the text converted to lowercase and saved in the tokens variable.
        if word not in stop_words and word not in string.punctuation: # it will check one by one if the word in the text is a stop word and a punctuations,if yes it will move ahead and check the others.
            word=lemmatizer.lemmatize(word) # if not then it will convert that word into it's root form
            cleaned.append(word) # and save it in the empty list called cleaned. Then the loop continues till the last word in the text.
    return " ".join (cleaned) # it will then join each word in the list by converting into string.
processed_texts=[preprocess(text)for text in texts] # the same thing as above will be again repeated but the data will be taken from the variable etxt in the function and saved it in this variable.
vectorizer=TfidfVectorizer(max_features=5000) # this will convert the data into binary and the text in bracket means it will take the top most important max 5000 words from the data.
X=vectorizer.fit_transform(processed_texts) # once converted into binary it will transform the data into the variable X to check if it is fit and if the data is ok to give outputs.
y=labels # labels will be made in this variable. Thes are the reviews by user,if they say bad then is stored as negative and if good then positive.
print("total samples",X.shape[0])
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42) # this is training the model.X has the data and y has the review labels.They are trained and tested on the data where we know the response,so we can check if the model is getting trained correctly or not(this is train_test_split).Random state means every time it is tested it takens different data,it can shuffle up to 42 times and 0.2 means it is tested 20% and trained 80%. 
model=LogisticRegression() # here the model will learn to predict the outcome and give result. 
model.fit(X_train,y_train) # the model will then be trained on the known  and the new data to give correct results.
y_pred=model.predict(X_test) # the model will now be tested on the known data and will be asked to predict the data to check if it works properly.
print("Accuracy:",accuracy_score(y_test,y_pred)) # it will print how accurately it was tested on the new data and how accurate the results of the old data were.
print("\n classification report: \n",classification_report(y_test,y_pred)) # this will show the overall performance of the new data's tested model and the predictions it showed for the known data.
print("\n confusion matrix: \n",confusion_matrix(y_test,y_pred)) # this will print if the reviews were good or bad using the predictions of the old data and with the new tested model. 
pickle.dump(model,open("model.pkl","wb")) # once this program is runned it will create a file named model.pkl which will have the info of the model and save it in the format of write in binary.
pickle.dump(vectorizer,open("vectorizer.pkl","wb")) # this will create a file vectorizer.pkl which will convert the above file into numbers and save it in this file with the format of write in binary.
def predict_sentiment(review): # here a function is defined to predict and do the analysis of the movie reviews.
    review=preprocess(review) # the top preprocess function is called and the input data is give as the movie reviews.
    review_vector=vectorizer.transform([review]) # it converts the reviews into binary form and stored it in a variable.
    prediction=model.predict(review_vector) # the new model is used to predict the result using the binary data.
    return prediction[0] # first prediction is shown.
print("\n custom prediction:") # prints this text.
print(predict_sentiment("This movie was absolutely amazing and inspiring")) # this is the review given to the model and the above function.
        