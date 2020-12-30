from scipy import stats


#performal normal distribution test
def is_it_normal(array):
    return stats.normaltest(array, nan_policy='omit')

#perform kuriskal-wallis test
def kwtest(array1, array2, array3):
    return stats.kruskal(array1, array2, array3, nan_policy='omit')

#two sample ttest
def ttest(array1, array2):
    return stats.ttest_ind(array1,array2, nan_policy='omit')