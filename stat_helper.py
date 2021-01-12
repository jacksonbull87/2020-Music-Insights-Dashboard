from scipy import stats


#performal normal distribution test
def is_it_normal(array):
    return stats.normaltest(array, nan_policy='omit')

#perform kuriskal-wallis test
def kwtest(array1, array2):
    return stats.kruskal(array1, array2, nan_policy='omit')

#two sample ttest
def ttest(array1, array2):
    return stats.ttest_ind(array1,array2, nan_policy='omit')

#create a function that outputs most time on chart given velocity

def max_toc(velocity, dataframe):
    df1 = dataframe.loc[dataframe['max velocity'] >= velocity]
    df2 = df1.sort_values('time_on_chart', ascending=False).reset_index()
    print("The most time spent on the chart for tracks\nwith a max velocity of at least {} is {} days".format(velocity, df1['time_on_chart'].max()))
    print("\n")
    print("Title: ",df2['title'][0])
    print("Artist: ",df2['primary_artist'][0])
    print("Days on Chart: ",df2['time_on_chart'][0])
    print("Max Velocity: ",df2['max velocity'][0])