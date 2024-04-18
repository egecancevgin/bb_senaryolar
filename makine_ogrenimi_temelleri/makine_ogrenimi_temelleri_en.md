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
