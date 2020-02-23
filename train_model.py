import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = datasets.load_iris(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
cls=DecisionTreeClassifier()
cls.fit(X, y)

model='model.pkl'
print('model trained.')
pickle.dump(cls, open(model, 'wb'))

