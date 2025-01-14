# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:15:51 2017

@author: Shenjunling
"""

from matplotlib import pyplot  
import scipy as sp  
import numpy as np  
from sklearn.datasets import load_files  
from sklearn.cross_validation import train_test_split  
from sklearn.feature_extraction.text import  CountVectorizer  
from sklearn.feature_extraction.text import  TfidfVectorizer  
from sklearn.naive_bayes import MultinomialNB  
from sklearn.metrics import precision_recall_curve  
from sklearn.metrics import classification_report  
  
''''' 
movie_reviews = load_files('G:/data/movie') 
#保存 
sp.save('G:/data/movie/movie_data.npy', movie_reviews.data) 
sp.save('G:/data/movie/movie_target.npy', movie_reviews.target) 
'''  
  
#读取  
movie_data   = sp.load('G:/data/movie/movie_data.npy')  
movie_target = sp.load('G:/data/movie/movie_target.npy')  
x = movie_data  
y = movie_target  
  
#BOOL型特征下的向量空间模型，注意，测试样本调用的是transform接口  
count_vec = TfidfVectorizer(binary = False, decode_error = 'ignore',
                            stop_words = 'english')  
  
  
#加载数据集，切分数据集80%训练，20%测试  
x_train, x_test, y_train, y_test = train_test_split(movie_data, movie_target, test_size = 0.2)  
x_train = count_vec.fit_transform(x_train)  
x_test  = count_vec.transform(x_test)  
  
  
#调用MultinomialNB分类器  
clf = MultinomialNB().fit(x_train, y_train)  
doc_class_predicted = clf.predict(x_test)  
      
#print(doc_class_predicted)  
#print(y)  
print(np.mean(doc_class_predicted == y_test))  
  
#准确率与召回率  
precision, recall, thresholds = precision_recall_curve(y_test, clf.predict(x_test))  
answer = clf.predict_proba(x_test)[:,1]  
report = answer > 0.5  
print(classification_report(y_test, report, target_names = ['neg', 'pos']))  