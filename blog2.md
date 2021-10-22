```python
import pandas as pd
```


```python
# read in results.csv
results = pd.read_csv("results.csv")
```


```python
# count the number of times each movie/TV appears in the dataframe, 
# which is equal to the number of actors in Black Mirror who are also in the movie/TV
shared_actors = pd.DataFrame(results['movie_or_TV_name'].value_counts())
# reset index so that movie/TV names can be treated as a normal column
shared_actors = shared_actors.reset_index()
# rename the columns
shared_actors.columns = ['Movie/TV', 'Number of Shared Actors']
```


```python
# display the first 20 movies/TVs with the most shared actors
shared_actors.head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Movie/TV</th>
      <th>Number of Shared Actors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Black Mirror</td>
      <td>506</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Doctors</td>
      <td>93</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Holby City</td>
      <td>78</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Casualty</td>
      <td>76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The Bill</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>EastEnders</td>
      <td>62</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Midsomer Murders</td>
      <td>59</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Silent Witness</td>
      <td>55</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Entertainment Tonight</td>
      <td>54</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Doctor Who</td>
      <td>50</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Celebrity Page</td>
      <td>47</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Made in Hollywood</td>
      <td>47</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Good Morning America</td>
      <td>38</td>
    </tr>
    <tr>
      <th>13</th>
      <td>The Late Late Show with James Corden</td>
      <td>37</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Death in Paradise</td>
      <td>36</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Lorraine</td>
      <td>33</td>
    </tr>
    <tr>
      <th>16</th>
      <td>New Tricks</td>
      <td>32</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Breakfast</td>
      <td>30</td>
    </tr>
    <tr>
      <th>18</th>
      <td>MI-5</td>
      <td>30</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Inspector Lewis</td>
      <td>28</td>
    </tr>
  </tbody>
</table>
</div>


