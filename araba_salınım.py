# Bulut Bilişim Günlük Senaryo
# Arabaların Karbondioksit Salınım Tahmini
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from bokeh.plotting import figure, show
from bokeh.io import output_notebook



def veri_duzenle():
  url = "https://raw.githubusercontent.com/egecancevgin/bb_senaryolar/main/C02_emmissions.csv"
  df = pd.read_csv(url)
  df.dropna(inplace=True)
  df.reset_index(drop=True, inplace=True)
  features_to_scale = [
      'Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)', 
      'Fuel Consumption Hwy (L/100 km)'
  ]
  scaler = MinMaxScaler(feature_range=(1, 100))
  df[features_to_scale] = scaler.fit_transform(df[features_to_scale])
  print(df.head())
  return df



def modeli_egit(df):
  X = df[
      [
          'Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)',
          'Fuel Consumption Hwy (L/100 km)'
      ]
  ]
  y = df['CO2 Emissions(g/km)']

  # Veriyi eğitim ve test setlerine ayırma
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
  )

  # Modeli oluşturma ve eğitme
  model = LinearRegression()
  model.fit(X_train, y_train)
  return model, X_train, X_test, y_train, y_test, X


def degerlendirme(model, X_train, X_test, y_train, y_test, X):
  y_pred_train = model.predict(X_train)
  y_pred_test = model.predict(X_test)
  mse_train = mean_squared_error(y_train, y_pred_train)
  mse_test = mean_squared_error(y_test, y_pred_test)

  print('Eğitim seti MSE:', mse_train)
  print('Test seti MSE:', mse_test)

  # Model katsayılarını yazdırma
  print('\nModel Katsayıları:')
  for feature, coef in zip(X.columns, model.coef_):
      print(f'{feature}: {coef}')

  return y_train, y_pred_train, y_test, y_pred_test


def gorsellestir(y_train, y_pred_train, y_test, y_pred_test):
    min_len_train = min(len(y_train), len(y_pred_train), 700)
    min_len_test = min(len(y_test), len(y_pred_test), 700)
    y_train = y_train[:min_len_train]
    y_pred_train = y_pred_train[:min_len_train]
    y_test = y_test[:min_len_test]
    y_pred_test = y_pred_test[:min_len_test]


    # Eğitim seti için görselleştirme
    plt.figure(figsize=(15, 7.5))  # %30 daha büyük boyut
    plt.plot(range(len(y_train)), y_train, label='Gerçek Değerler', color='blue')
    plt.plot(range(len(y_train)), y_pred_train, label='Tahmin Edilen Değerler', color='red')
    plt.title('Eğitim Seti Gerçek vs Tahmin')
    plt.xlabel('Örnekler')
    plt.ylabel('CO2 Emisyonları')
    plt.legend()
    plt.show()

    # Test seti için görselleştirme
    plt.figure(figsize=(15, 7.5))  # %30 daha büyük boyut
    plt.plot(range(len(y_test)), y_test, label='Gerçek Değerler', color='blue')
    plt.plot(range(len(y_test)), y_pred_test, label='Tahmin Edilen Değerler', color='red')
    plt.title('Test Seti Gerçek vs Tahmin')
    plt.xlabel('Örnekler')
    plt.ylabel('CO2 Emisyonları')
    plt.legend()
    plt.show()


def main():
  df = veri_duzenle()
  model, xtr, xts, ytr, yts, X = modeli_egit(df)
  ytr, yptr, yt, yptr = degerlendirme(model, xtr, xts, ytr, yts, X)
  gorsellestir(ytr, yptr, yt, yptr)

if __name__ == '__main__':
  main()

