# OOP-Ex1

## Preface:

This is the second assignment in the OOP course. In this task we were tasked to write an offline algorithm that assigns elevator
calls to the most optimal elevator. This is measured by the average waiting time, uncompleted calls, etc. This is a
continuation of the first assignment where we wrote an online algorithm for the same problem.

## 1. Algorithm:

* For each elevator:
    * Calculate the **fraction of speed** by dividing the current elevator speed by the sum of all elevator speeds in
      the building (Normalization).
    * Calculate the **number of calls** that will be assigned to an elevator by multiplying the fraction of speed by the
      total number of calls.
    * Divide the total number of calls by the number of calls assigned to an elevator to determine how many **calls to
      skip** when managing assignments. This provides the elevator time to optimize handling existing calls before
      receiving new ones.
    * **Allocate unassigned calls** to the current elevator with intervals according to calls to skip.
* If there are **unassigned calls left**: Assign one call per elevator, alternate between elevators. Continue until all
  calls are assigned.

## 2. Our Results:

Building | Calls | total waiting time | average waiting time per call | uncompleted calls | certificate |
:---: | :---: | :---: | :---: | :---: | :---: | 
B1 | a |11292.0 |  112.92 |0 | -276569737 |
B2 | a | 6062.0 | 60.62 | 0 | -187183277 |
B3 | a | 3342.0 | 33.42 | 0 | -29052204 |
B3 | b | 539322.251 | 539.322 | 138 | -1774316727 |
B3 | c | 567171.176 | 567.171 |85 | -1942650510 |
B3 | d | 545657.613 | 545.658 | 86 | -2001764854 | 
B4 | a | 2173.0 |  21.73 | 0 |-52641752 |
B4 | b | 209616.179 | 209.616 | 31 |  -745927639 |
B4 | c | 207717.284 | 207.717 | 12 |  -770323363 |
B4 | d | 202338.686 |  202.339 |13 | -786806834 |
B5 | a | 1843.0 | 18.43 | 0 | -80073359 |
B5 | b | 70008.114 | 70.008 | 3 | -152641781 |
B5 | c | 69360.0 | 69.36 | 0 | -155349576 |
B5 | d | 70306.0 | 70.306 | 0 |  -152641771 |

*Values were rounded to 3 digits after the decimal point.*

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

