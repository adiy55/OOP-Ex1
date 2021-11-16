# OOP-Ex1

## 1. Algorithm:

* For each elevator:
    * Calculate the **fraction of speed** by dividing the current elevator speed by the sum of all elevator speeds in
      the building (Normalization).
    * Calculate the **number of calls** that will be assigned to an elevator by multiplying the fraction of speed by the
      total number of calls.
    * Divide the total number of calls by the number of calls assigned to an elevator to determine how many **calls to
      skip** when managing assignments. This provides the elevator time to optimize handling existing calls before receiving new
      ones.
    * **Allocate unassigned calls** to the current elevator with intervals according to calls to skip.
* If there are **unassigned calls left**: Assign one call per elevator, alternate between elevators. Continue until all
  calls are assigned.

## 2. Our Results:
Building/Calls | B1/a | B2/a | B3/a | B3/b | B3/c | B3/d | B4/a | B4/b | B4/c | B4/d | B5/a | B5/b | B5/c | B5/d
--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
total waiting time | 11292.0 | 6062.0 | 3342.0 | 539322.251 | 567171.176 | 545657.613 | 2173.0 | 209616.179 | 207717.284 | 202338.686 | 1843.0 | 70008.114 | 69360.0 | 70306.0
average waiting time per call | 112.92 | 60.62 | 33.42 | 539.322 | 567.171 | 545.658 | 21.73 | 209.616 | 207.717 | 202.339 | 18.43 | 70.008 | 69.36 | 70.306
uncompleted calls | 0 | 0 | 0 | 138 | 85 | 86 | 0 | 31 | 12 | 13 | 0 | 3 | 0 | 0 | 
certificate | -276569737 | -187183277 | -29052204 | -1774316727 | -1942650510 | -2001764854 | -52641752 | -745927639 | -770323363 | -786806834 | -80073359 | -152641781 | -155349576 | -152641771 | 

*Rounded to 3 digits after the decimal point.*

## 3. Dependencies:

**`Pandas`** Library (<a href="https://pandas.pydata.org/docs/getting_started/install.html">Installation Guide</a>)

## 4. How to Run from the Command Line:

**Provide the path in the brackets. There are csv files provided in this repository.**

### Python program:

```
python Ex1.py <Building.json> <Calls.csv> <Output.csv (path to save output)>
```

### Simulator for testing the output:

```
java -jar Ex1_checker_V1.2_obf.jar 1111,2222 <Building.json> <Output.csv> <out.log>
```

* 1111,2222: can add between 1 and 3 ID numbers separated with a comma without whitespaces
* Building.json: same as the one used in the python program
* Output.csv: output file of the python program
* out.log: path to save the simulator log

## 5. UML

