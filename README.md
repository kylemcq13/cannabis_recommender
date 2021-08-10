# cannabis_recommender

Check out the app here --> https://cannabis-recommender.herokuapp.com/

This recommender can take in specific desired effects and recommend cannabis strains based on the user input. The user can enter up to 3 effects from dropdown menus, and cannabis strain matches are displayed with descriptions, type and flavor profiles. 

## Data Exploration
Data was obtained from Kaggle. It contains cannabis strain names along with associated flavors, effects, an average rating, type of strain (indica, sativa or hybrid) and a description of the strain. 



### Flavor
Cannabis is very diverse in flavor profiles. It contains a complex mixture of volatile chemical compounds that is actually similar to hops. Common descriptors include earthy, citrus, flowery and piney. See wordcloud below for reference.

<img src="https://github.com/kylemcq13/cannabis_recommender/blob/main/images/wordcloud.PNG" alt="Flavor WordCloud" width="500" height="500">



### Effects
Cannabis is also diverse in its effects on the body and mind. The most commonly occurring effects in this particular dataset include 'happy', 'relaxed', 'euphoric', and 'uplifted'. 

<img src="https://github.com/kylemcq13/cannabis_recommender/blob/main/images/top_effects_chart.PNG" alt="Top Effects Chart" width="500" height="700">



### Description
The dataset also contains descriptions of the strains. These vary in content but typically discusses the effects, flavor and some notes on growing on the strain. An example output is below:

<img src="https://github.com/kylemcq13/cannabis_recommender/blob/main/images/sample_description.PNG" alt="sample_description" width="800" height="150">


### How it Works
The user inputs three desired effects from three dropdown menus on the homepage. The model will then make suggestions based on this input and the highest rated strains that match the desired effect. 

See exploration notebook for more details.


