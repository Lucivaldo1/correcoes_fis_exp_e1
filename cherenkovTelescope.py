'''
Classificacao entre sinal e bakcground a partir de dados do Cherenkov telescope

link da base de dados: https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope

@author: Lucivaldo Barbosa

'''
from ucimlrepo import fetch_ucirepo 

from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report
# fetch dataset 
magic_gamma_telescope = fetch_ucirepo(id=159) 
  
# data (as pandas dataframes) 
X = magic_gamma_telescope.data.features 
y = magic_gamma_telescope.data.targets 

X_gamma = X.values

y_gamma = y.values.reshape(19020,)

print(X_gamma.shape)

print(y_gamma.shape)

X_gamma_treinamento, X_gamma_teste, y_gamma_treinamento, y_gamma_teste = train_test_split(X_gamma,
                                                                                           y_gamma,
                                                                                           train_size= 0.15,
                                                                                           random_state= 0)

rede_neural = MLPClassifier(activation= 'logistic', solver='adam', hidden_layer_sizes= (15,15),
                            verbose=True, tol=0.0000001, max_iter=1500)


rede_neural.fit(X_gamma_treinamento, y_gamma_treinamento)

previsao = rede_neural.predict(X_gamma_teste)

precisao = accuracy_score(y_gamma_teste, previsao)

print(precisao)

print(classification_report(y_gamma_teste, previsao))