# ambiguity

feature with ambigous matches : what if two features match f1,f2 == f1,f3

1. compute distance for all features
2. for each feature f1, find closest match f2
3. find second closest match
4. use distance ratio to find how much better one is than the other
5. if distance ratio is close to 1, both are matches (don't use the match)
6. keep with distance ration < rho where rho is (0,1]

up to 50% matches can be outliers
