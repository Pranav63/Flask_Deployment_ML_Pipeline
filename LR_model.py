import pandas as pd
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump

data = pd.read_csv('twitter_sentiments.csv')
print(data.head())

# Divide dataset 80 20
train, test = train_test_split(
    data, test_size=0.2, stratify=data['label'], random_state=33)

print(train.shape, test.shape)

''' tfidf = TfidfVectorizer(lowercase=True, max_features=1000,
                       stop_words=ENGLISH_STOP_WORDS)
 tfidf.fit(train.tweet)
 model = LogisticRegression()
 model.fit(train_idf, train.label)'''

pipeline = Pipeline(steps=[('tfidf', TfidfVectorizer(lowercase=True, max_features=1000,
                                                     stop_words=ENGLISH_STOP_WORDS)), ('model', LogisticRegression())])

pipeline.fit(train.tweet, train.label)

text = ["Fuck off man"]
predict_train = pipeline.predict(text)
print(predict_train)
# predict_test = pipeline.predict(test_idf)

dump(pipeline,filename="Text_classsfier.joblib")
# f1score on train data
# print(f1_score(y_true=train.label, y_pred=predict_train))

# f1 score on test data
# print(f1_score(y_true=test.label, y_pred=predict_test))
