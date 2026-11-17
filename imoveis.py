import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

dados = pd.read_csv("imoveis.csv")
cinco_primeiras_linha = dados.head(5)
resumo_estatico = dados.describe()

x = dados[["Area_M2"]]
y = dados["Preço"]
modelo = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
modelo.fit(X_train, y_train)
previsoes = modelo.predict(X_test)
previsoes_grafico = modelo.predict(x)
mae = mean_absolute_error(y_test, previsoes)
mse = mean_squared_error(y_test, previsoes)
rmse = mse ** 0.5
plt.scatter(X_train, y_train, label="Dados de treino")
plt.scatter(X_test, y_test, label="Dados de teste")
plt.plot(x, previsoes_grafico, color="red", label="Regressão Linear")
plt.xlabel("Área (m²)")
plt.ylabel("Preço (R$)")
plt.title("Regressão Linear - Preço de Imóveis")
plt.legend()
plt.show()


print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
