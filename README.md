# pyBenchChart
 A companion tool for CSS-Benchmark

# Requirements

1. Python 3.x
2. `matplotlib`

# Usage
 Place benchmark json in .py directory

 `python .\pyBenchChart.py -b .\benchmark-[currentTime].json -l [0/1]`

 `-l` defines wheter to use log scale on y-axis, where 1 is true, 0 is false

 This is useful for datasets with large differences in y-axis values

# Images
## Linear (-l 0)
![l0](https://github.com/rcnoob/pyBenchChart/blob/main/l0.png)
## Logarithmic (-l 1)
![l1](https://github.com/rcnoob/pyBenchChart/blob/main/l1.png)
