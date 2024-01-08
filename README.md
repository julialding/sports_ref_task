# Solution Overview
This solution uses Python to read in a json file (called "data.json"), which is conveniently formatted as a nested dictionary/hash map. Upon doing so, it records a list of teams by extracting the keys from the data. It then creates a matrix (essentially a 2D list) and records the win count for each respective cell. If the row and column value pertaining to a specific cell is equal, we record a dash instead.

Next, the solution prints out the table. It does so through first formatting the header and then the matrix, adding spaces between each cell for readability.

The output for the example data is as follows:

    **BRO BSN CHC CIN NYG PHI PIT STL**

BRO -  10  15  15  14  14  15  11

BSN 12  -  13  13  13  14  12  9

CHC 7  9  -  12  7  16  8  10

CIN 7  9  10  -  13  13  13  8

NYG 8  9  15  9  -  12  15  13

PHI 8  8  6  9  10  -  13  8

PIT 7  10  14  9  7  9  -  6

STL 11  13  12  14  9  14  16  -

Note that improvements can be made to account for formatting spaces between cells, but this can also be targeted during the development of the frontend if one were actually to display this table on a website.
