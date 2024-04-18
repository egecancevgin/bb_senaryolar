# Problem – Machine Learning Fundamentals

Machine Learning is the technology that allows computers to learn by looking at data and make predictions on data they do not know.
For example, it can be used to recognize a dog in a photo and spot it when dogs are seen in subsequent photos, to predict emotion in a text, to detect fraud in a bank transaction.

![Object-Detection](https://raw.githubusercontent.com/egecancevgin/bb_senaryolar/main/makine_ogrenimi_temelleri/obje_tespiti.png)


When machines learn, the data they receive as input are called independent variables, and various algorithms are used to reveal the patterns in them.

All of these algorithms and mathematical techniques are called models, and we need to train the model to make predictions. After training the model with some of the data, we need to test some of it.

It's like putting the model to a test to which we know the answers. For example, if we have 10 solved exam questions, we teach 6 questions to the model with their answers. We can expect him to solve the remaining 4 questions without giving answers. These two sets of questions are called training and test sets.

![Egitim-Test](https://raw.githubusercontent.com/egecancevgin/bb_senaryolar/main/makine_ogrenimi_temelleri/egitim_tst.png)


Independent variables are usually represented by 'X'. The variables that the model tries to predict are called dependent variables and are represented by 'y'.

'Loss' is the difference between the value predicted by the machine and the actual value, and we want to minimize this. For example, in the image below, the yellow circles represent the actual data points, the blue line represents our prediction, and the red arrows represent the loss.

![Kayıp](https://raw.githubusercontent.com/egecancevgin/bb_senaryolar/main/makine_ogrenimi_temelleri/kayıp.png)


During training, the model gives weight to the columns that are independent variables and learns patterns according to these weights.
For example, in ice cream sales data, the season and current temperature column will often be more important than other columns.

The label is the dependent variable data for which we know the answer. For example, we know that some e-mails in an e-mail data are spam. The column that indicates that the email is spam is called a label, and the machine uses this label for training.

Machine learning done using labeled data is called 'Supervised Machine Learning'. The most basic algorithm of supervised machine learning is 'Linear Regression'.

The Linear Regression algorithm tries to create the line that best fits the data we have. In this way, we can predict the course of data with certain characteristics. For example, in the graph below, the red dots are the actual data points, while the blue line is our estimated mathematical linear regression line.

![Lineer-Reg](https://raw.githubusercontent.com/egecancevgin/bb_senaryolar/main/makine_ogrenimi_temelleri/linreg.png)


The Linear Regression equation is as follows: 'Y = β₀ + W₁X₁ + W₂X₂ + ... + WₙXₙ' where W's are the weights of the respective columns, X's are the data points i.e. rows, and β₀ is the distance of the equation from the x-axis.

Machine Learning can be examined in three main stages: Representation, Evaluation and Optimization. In the representation stage, mathematical modeling is carried out with data processing and this is the stage where the model is trained. In the evaluation phase, the prediction and training success of the model is examined. In the optimization phase, improvements are made to improve the training of the model.

Data processing is important to bring our data into the appropriate format. For example, some columns may have missing or incorrect values, some columns may be numeric, some columns may be text, some columns may have values between 0-10000 and some columns may have values between 0-10.

As we mentioned in the learning equation, learning was done by multiplying the data points of each column by the weight value. However, if there is a mismatch in the range of data points between these columns, the machine may conclude that the higher value data point will be more important during learning. For example, if the area of ​​the house in one column is 150 square meters and the age of the house in another column is 3 years, the area value of the house in the equation will be much more impressive.

To solve this problem, we can scale the columns. For example, in Min-Max Scaling, each value is rescaled by dividing by the smallest value in the data set and then dividing by the largest value in the data set based on the result of this division.

As a loss function, the most suitable one for this problem will be 'Mean Squared Error'. This metric takes the sum of the squares of the differences between the actual values and the predicted values in the data set and then averages all these terms.

In addition, we must write all our machine learning projects in accordance with PEP 8 standards so that automation tests can be carried out easily during the deployment phase and we can write them in a more understandable order.

In today's scenario, we will use a car data set to have the machine predict the carbon dioxide emissions of cars. First we need to download the necessary modules from the terminal and update our installation tool:
``` sh
sudo apt update
sudo apt install python3-pip
pip install pandas
pip install scikit-learn
pip install matplotlib
```

Let's create our project file:
``` sh
touch araba_salinim.py
```

Our file will be created under the 'WORKSPACE' section at the top left of our screen. Let's click on this file and write the following directives at the top of the file:
``` py
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
```

After making the necessary library calls, we can now create our data editing function. Let's write the 'data_edit()' function two lines below our library directives.

In this function, let's first read this '.csv' extension file in DataFrame format using the location where our data is located. Afterwards, let's assign NaN values and reset the indices.

Let's not forget to scale so that the training takes place properly. Let's include the engine volume, number of cylinders, urban and extra-urban gasoline usage columns in the scaling. Afterwards, let's set MinMaxScaler, which we will use from the Scikit-learn library, equal to the scaler variable and scale these four columns of the DataFrame with the 'fit_transform' method:
``` python
def veri_duzenle():
  """ It cleans and scales the data, displays it on the screen, and then rotates."""
  url = "https://raw.githubusercontent.com/egecancevgin/bb_senaryolar/main/C02_emmissions.csv"
  df = pd.read_csv(url)
  df.dropna(inplace=True)
  df.reset_index(drop=True, inplace=True)
  features_to_scale = [
      'Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)', 
      'Fuel Consumption Hwy (L/100 km)'
  ]

  # You will perform the scaling process.
  # Use MinMaxScaler and give between feature_range(1, 100):
  scaler = ...

  # Call the fit_transform method of the scaling object, the scaler.
  # Give 'df['features_to_scale'] as argument:
  df[features_to_scale] = ...

  print(df.head())
  return df
```

After this method is completed, we will create a model_egit() method that takes the data set (df) as input. At this stage, let's first set the independent variables equal to the X variable and the dependent variable to the y variable. Then, let's divide it by 4 using the train_test_split() method of the scikit-learn library.

X training and y training data will be used in the training phase, and X test and y test data will be used in the testing phase. In this example, we will split the data as 80% training - 20% testing.

Afterwards, we will create our model using the 'LinearRegression' class of the 'scikit-learn' library. To train the model, let's give 'X_train' and y_train' training data as input and perform the training with the '.fit()' method. Then return the model and data:
``` python
def modeli_egit(df):
  """ It performs model training and returns the trained model with the fragmented data."""
  X = df[
      [
          'Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)',
          'Fuel Consumption Hwy (L/100 km)'
      ]
  ]
  y = df['CO2 Emissions(g/km)']

  # Let's make the training-test distinction we mentioned.
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
  )

  # You do the model training.
  # Call 'LinearRegression' and then do model.fit():
  model = ...
  ...

  return model, X_train, X_test, y_train, y_test, X
```

Next is the evaluation phase, we will make our prediction and evaluate the results. Let's create an 'evaluate()' function that takes six parameters as input. Let's make a prediction using the dependent variables of the test set. Then, to measure the success of our prediction, let's use scikit-learn's 'mean_squared_error' method for our inputs and return the output:
``` python
def degerlendirme(model, X_train, X_test, y_train, y_test, X):
  """ It makes a prediction with the test data and prints the MSE value on the screen and returns."""
  y_pred_test = model.predict(X_test)

  # You must find the test MSE value, use 'mean_squared_error'.
  # Give 'y_pred_test' with 'y_test' as arguments:
  mse_test = ...

  print('Test set MSE:', mse_test)
  return mse_test
```

Finally, let's create and call our 'main()' function. At the end of the method, let's write the 'evaluation' function output to a file:
``` python
def main():
  df = veri_duzenle()
  model, xtr, xts, ytr, yts, X = modeli_egit(df)
  cikti = degerlendirme(model, xtr, xts, ytr, yts, X)

  with open("cikti.txt", "w") as dosya:
    dosya.write(str(int(cikti)))

main()
```

Now let's run the code from the terminal. If the MSE value is around 200, we can say that the process is complete:
``` sh
python3 araba_salinim.py
```

### Tiny Scikit-learn Tips:
1- Scaling is done as follows, for example:
``` python
olcek = StandartScaler(feature_range=(1, 50))
df[sutunlar] = olcek.fit_transform(df[sutunlar])
```

2- The model is trained as follows:
``` python
model = LogisticRegression()
model.fit(X_train, y_train)
```

3- For example, a similar loss function is used as follows:
``` python
mae_test = mean_absoulute_error(y_test, y_pred_test)
```

