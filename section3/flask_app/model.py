# https://medium.com/clarusway/model-deployment-with-flask-part-1-14a944eb9d49

import pandas as pd
import pickle
import joblib # 안씀..

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from category_encoders import OneHotEncoder, BinaryEncoder

# data

df = pd.read_csv('flask_app/data/top10s_preprocessing.csv')


# 결측값 제거하고 0,1로만 구성된 더미값을 반환해주세요
# df = pd.get_dummies(df, prefix='', prefix_sep='', columns = [['bpm_tempo'],['energy'],['danceability'],['decibel'],['length'],['speechiness']], drop_first=True)
# df = pd.concat([pd.get_dummies(df[col]) for col in df], axis=1, keys=df.columns)

# split data(train,val,test)

train, test = train_test_split(df, test_size=0.2, random_state=2)
train, val = train_test_split(train, test_size=0.2, random_state=2)

# 데이터의 불균형한정도를 보기도 함(긁어온코드 적용되지않음)
'''train = pd.concat([X_train, y_train], axis=1)
scale_weight_0 = int(train[target_col].value_counts()[0])
scale_weight_1 = int(train[target_col].value_counts()[1])'''


# target, features
target = 'positive'
features = ['bpm_tempo','energy','danceability','decibel','length','speechiness']

x = df[features]
# 남겨두는거 : bpm_tempo,energy,danceability,decibel,length,speechiness
# drop : 'id','title','artist','top_genre','year','live','acoustic','popular'
y = df[target]

X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]
X_test = test[features]
y_test = test[target]


# onehot encoder : 범주형이라!! categorycal해서!!
classifier = make_pipeline(
    OneHotEncoder(),
    RandomForestClassifier(random_state=10))

# fitting model with training data
classifier.fit(X_train,y_train)

# pickle = 텍스트가 아닌 파이썬객체자체를저장.

# saving model to disk(피클모듈을 사용하여 문자스트림으로 변경)
pickle.dump(classifier, open('model.pkl','wb'))

# loading model to compare the results
model=pickle.load(open("model.pkl", "rb"))

