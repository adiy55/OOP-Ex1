# OOP-Ex1

## 1. Algorithm:

* For each elevator:
    * Calculate the **fraction of speed** by dividing the current elevator speed by the sum of all elevator speeds in
      the building.
    * Calculate the **number of calls** that will be assigned to an elevator by multiplying the fraction of speed by the
      total number of calls.
    * Divide the total number of calls by the number of calls assigned to an elevator to determine how many **calls to
      skip** when managing assignments. This provides the elevator time to handle existing calls before receiving new
      ones.
    * **Allocate unassigned calls** to the current elevator with intervals according to calls to skip.
* If there are **unassigned calls left**: Assign one call per elevator, alternate between elevators. Continue until all
  calls are assigned.

## 2. Our Results:
Building/Calls | B1/a | B2/a | B3/b | B3/c | B3/d | B4/b | B4/c | B4/d | B5/b | B5/c | B5/d
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
total waiting time |  |  |  |  |  |  |  |  |  |  | 
average waiting time per call |  |  |  |  |  |  |  |  |  |  | 
uncompleted calls |  |  |  |  |  |  |  |  |  |  | 

## 3. Dependencies:

**`Pandas`** library <a href="https://pandas.pydata.org/docs/getting_started/install.html">Installation Guide</a>

## 4. How to Run from Command Line:

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

