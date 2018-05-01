# records
packaged for querying GBIF for taxon occurrence records within a range of years
version 0.2

### Information below copied from https://github.com/programming-for-bio/records/blob/master/README.md

The `records` library provides tools for querying the GBIF database using 
its public REST API, and to efficiently collect large numbers of records 
while following limitations on queries. Results are returned as Pandas 
dataframes.

### Installation
```bash
git clone https://github.com/programming-for-bio/records
cd records/
pip install .
```

### Dependencies
```bash
conda install requests pandas numpy
```


### Example usage

There are two main class objects, the `Records` class and the `Epochs` class. 
The `Records` class performs query searches to download data from GBIF, the 
`Epochs` class is used to concatenate records from many `Records` searches, and 
to calculate summary statistics.  


```python
import records
```

##### The Records class
```python
# make a single records search
rec = records.Records("Bombus", interval=(1900, 1905))

# make a records search with additional arguments
kwargs = {"country": "CA", }
rec = records.Records("Bombus", (1900, 1905), **kwargs)

# access dataframe of results
rec.df.shape

# or a simpler view of the dataframe
rec.sdf.head()
```

```parsed-literal
 	species 		year 	stateProvince
0 	Bombus vagans 		1905 	Illinois
1 	Bombus centralis 	1902 	Washington
2 	Bombus vagans 		1905 	Illinois
3 	Bombus nevadensis 	1905 	Washington
4 	Bombus impatiens 	1905 	Illinois
```

##### The Epochs class
```python
# collect all records from 1900 to 1921 in 3 year intervals from Canada
ep = records.Epoch("Bombus", 1900, 1960, 3, **{"country": "CA"})

# show first 10 records
ep.sdf.head()

# calculate simpson's diversity (a measure of species diversity) for each state
ep.simpsons_diversity(by="stateProvince")
```

```parsed-literal
stateProvince
Alberta                      0.923426
British Columbia             0.892504
Manitoba                     0.863905
New Brunswick                0.793618
Newfoundland                      NaN
Newfoundland and Labrador    0.897924
Northwest Territories        0.864266
Nova Scotia                  0.777940
Nunavut                      0.606157
Ontario                      0.890607
Prince Edward Island         0.444444
Quebec                       0.846009
Sakatchewan                       NaN
Saskatchewan                 0.814708
Vancouver Island                  NaN
Yukon                        0.641975
Yukon Territory              0.873724
Name: species, dtype: float64
```


##### Saving/loading data
```python
# for large downloads you may want to save the dataframe to CSV.
ep.df.to_csv("data/Bombus-1900-1960-CA.csv")

# you can later reload it as an Epochs instance like the following.
ep = records.load_epochs_from_csv("data/Bombus-1900-1960-CA.csv")

```
