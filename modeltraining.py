import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.model_selection import train_test_split
df=pd.read_excel("C:/Users/hi/Desktop/ds intern/project2/abc/Data.xlsx")
df.head()
df.info()
df.columns
#rename the columns
df.rename(columns={'Department ':'Department','Job role':'Jobrole','environment satisifaction':'environmentsatisifaction','Behaviourial Competence':'BehaviourialCompetence','On time Delivery':'OntimeDelivery','Ticket Solving Managements ':'TicketSolvingManagements','Project evlaution /Completeion':'ProjectevlautionorCompleteion','Annual Income':'AnnualIncome','Workign hrs ':'Workinghrs','Working from home or office ':'Workingfromhomeoroffice','Psycho-Social Indicators':'PsychoSocialIndicators','Effected with corona':'Effectedwithcorona','Percent Salary Hike':'PercentSalaryHike','Net connectivity':'Netconnectivity'},inplace=True)
df.rename(columns={'Job Level':'JobLevel','Feedbacks ':'Feedbacks'},inplace=True)
#categorical colunms-mode imputation
from sklearn.impute import SimpleImputer
mode_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
df["Gender"] = pd.DataFrame(mode_imputer.fit_transform(df[["Gender"]]))
df["Department"] = pd.DataFrame(mode_imputer.fit_transform(df[["Department"]]))
df["Jobrole"] = pd.DataFrame(mode_imputer.fit_transform(df[["Jobrole"]]))
#numerical columns-median imputation
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["RelationshipSatisfaction"] = pd.DataFrame(median_imputer.fit_transform(df[["RelationshipSatisfaction"]]))
df["TrainingTime(months)"] = pd.DataFrame(median_imputer.fit_transform(df[["TrainingTime(months)"]]))
df["WorkLifeBalance"] = pd.DataFrame(median_imputer.fit_transform(df[["WorkLifeBalance"]]))
df["Feedbacks"] = pd.DataFrame(median_imputer.fit_transform(df[["Feedbacks"]]))
df["Attendance"] = pd.DataFrame(median_imputer.fit_transform(df[["Attendance"]]))
df["Effectedwithcorona"] = pd.DataFrame(median_imputer.fit_transform(df[["Effectedwithcorona"]]))
df.isna().sum()
#removing ouliers
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method='iqr', # choose  IQR rule boundaries or gaussian for mean and std
                          tail='both', # cap left, right or both tails 
                          fold=1.5,
                          variables=['Performance Rating'])

df['Performance Rating'] = winsor.fit_transform(df[['Performance Rating']])
# lets see boxplot
sns.boxplot(df['Performance Rating'])

# Encoding all the ordinal columns and creating a dummy variable for them to see if there are any effects on Performance Rating
enc = LabelEncoder()
for i in (2,3,4,5):
    df.iloc[:,i] = enc.fit_transform(df.iloc[:,i])
df.head()
# Here we have selected only the important columns
y = df['Performance Rating']
X = df.iloc[:,[6,7,9,11,13,14,15,16,17,18,19,20,22,26]] # Taking only variables with correlation coeffecient greater than 0.1
# Splitting into train and test for calculating the accuracy
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)
# import the regressor
from sklearn.tree import DecisionTreeRegressor 
# create a regressor object
regressor = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,max_depth = 5, alpha = 10, n_estimators = 100) 
regressor.fit(X_train, y_train)
#prediction
y_pred = regressor.predict(X_test)
### Check error rate
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
### Create a Pickle file using serialization 
import pickle
pickle_out = open("regressor.pkl","wb")
pickle.dump(regressor, pickle_out)
pickle_out.close()
features=np.array([[5,1,4,12,1.0,5,1,3.0,3,12,12,12,2,11]])
regressor.predict(features)
