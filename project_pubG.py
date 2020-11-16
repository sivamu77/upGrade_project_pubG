import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
#1 Read the dataset.
data=pd.read_csv("C:\pubg - Dr. Darshan Ingle.csv")

#2 Check the datatype of all the columns.
data.dtypes

#3. Find the summary of all the numerical columns and write your findings about it.
data.describe()
#4. The average person kills how many players?
data['kills'].mean()
#5. 99% of people have how many kills?
np.percentile(data.kills,99)
#6. The most kills ever recorded are how much?

data['kills'].max()

#7. Print all the columns of the dataframe.
data.columns
#8. Comment on distribution of the match's duration. Use seaborn.
sb.distplot(data['matchDuration'])
#9. Comment on distribution of the walk distance. Use seaborn.
sb.distplot(data['walkDistance'])
#10. Plot distribution of the match's duration vs walk distance one below the other.
plt.subplot(2,1,1)
sb.distplot(data['matchDuration'])
plt.subplot(2,1,2)
sb.distplot(data['walkDistance']);
#11. Plot distribution of the match's duration vs walk distance side by side.
plt.subplot(1,2,1)
sb.distplot(data['matchDuration'])
plt.subplot(1,2,2)
sb.distplot(data['walkDistance']);
#12. Pairplot the dataframe. Comment on kills vs damage dealt, Comment on maxPlace vs numGroups.
sb.pairplot(data);

#13. How many unique values are there in 'matchType' and what are their counts?

data['matchType'].value_counts()
#14. Plot a barplot of ‘matchType’ vs 'killPoints'. Write your inferences.

sb.barplot(x='matchType',y='killPoints',data=data)
plt.xticks(rotation=80)
#15. Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’. Write your inferences.
sb.barplot(x='matchType',y='weaponsAcquired',data=data);
plt.xticks(rotation=80);
#16. Find the Categorical columns.
data.select_dtypes(exclude=['number'])
#17. Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’. Write your inferences.
sb.boxplot(x='matchType',y='winPlacePerc',data=data)
plt.xticks(rotation=70);
#18. Plot a boxplot of ‘matchType’ vs ‘matchDuration’. Write your inferences.
sb.boxplot(x='matchType',y='matchDuration',data=data)
plt.xticks(rotation=70);
#19. Change the orientation of the above plot to horizontal.
sb.boxplot(x='matchDuration',y='matchType',data=data)
plt.xticks(rotation=70);
#20. Add a new column called ‘KILL’ which contains the sum of following columns viz. headshotKills,teamKills, roadKills.
data['KILL']=data['headshotKills']+data['teamKills']+data['roadKills']
#21. Round off column ‘winPlacePerc’ to 2 decimals.
data['winPlacePerc']=round(data['winPlacePerc'],2)
data['winPlacePerc']
#22. Take a sample of size 50 from the column damageDealt for 100 times and calculate its mean. Plotit on a histogram and comment on its distribution.
x = []
for i in range(100):
    x.append(data['damageDealt'].sample(50).mean())
m = np.array(x)
sb.distplot(m);