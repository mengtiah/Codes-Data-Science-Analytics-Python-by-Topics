## 2. Introduction to the data ##

import pandas as pd
dc_listings=pd.read_csv('dc_airbnb.csv')
print(dc_listings)

## 4. Euclidean distance ##

import numpy as np
first_distance=np.abs(dc_listings['accommodates'][0]-3)
print(first_distance)

## 5. Calculate distance for all observations ##

dc_listings['distance']=dc_listings['accommodates'].apply(lambda x: np.abs(x-3))
print(dc_listings['distance'].value_counts())

## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
dc_listings = dc_listings.sort_values('distance')
print(dc_listings['price'][0:10])

## 7. Average price ##

stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars=stripped_commas.str.replace('$','')
dc_listings['price']=stripped_dollars.astype('float')
mean_price=dc_listings['price'][0:5].mean()
print(mean_price)


## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()    
    temp_df['distance']=temp_df['accommodates'].apply(lambda x: np.abs(x-new_listing))
    temp_df=temp_df.sort_values('distance')
    nearest_neighbors=temp_df[0:5]['price']
    predict_price=nearest_neighbors.mean()
    return(predict_price)

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)
