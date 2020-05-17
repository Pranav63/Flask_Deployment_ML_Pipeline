from joblib import load

pipe = load("Text_classsfier.joblib")

text = ["You so ugle , spit on you"]

print(pipe.predict(text))
