# HPC Twitter Processing
COMP90024 Cluster and Cloud Computing Assignment 1

## How to run
1. Run with `run.sh`, it would automately use 4 cores to run the application with `data/smallTwitter.json`.
    ```shell
    ./run.sh
    ```
2. Run with command:
    ```shell
    time mpiexec -n 4 python3 src/twitterAnalysis.py -f <datapath>
    ```
    
## HPC Script Usage
*Use to upload or download files from the HPC server.*
1. Change the  username, password and data path in `pushToSpartan.sh` to your own info
2. Also change the info in `pullOut.sh` to your own info.
3. Install `export` by `brew install export`.
4. Use `export pushToSpartan.sh` to push file to spartan.
5. Use `export pullOut.sh` to pull the output file from spartan.

## Result
### Result of local run:
```shell
Run src/twitterAnalysis with MPI
Running, use core:  4
Data size: 23920179
Each process handle: 5980044
-------------------------------------
Hashtag Rank: 
1. #scottyfrommarketing, 31
1. #auspol, 31
3. #climatechange, 29
4. #australiaburns, 24
5. #australianfires, 22
6. #sydnye, 19
7. #sonicmovie, 17
8. #goavsgo, 13
9. #nswfires, 12
9. #เป๊กผลิตโชค, 12
9. #bushfirecrisis, 12
-------------------------------------
Language Rank: 
1. English (en), 4,127
2. Undefined (und), 302
3. Portuguese (pt), 101
4. French (fr), 92
5. Thai (th), 83
6. Spanish (es), 61
7. Japanese (ja), 32
8. Tagalog (tl), 27
9. Indonesian (in), 22
9. Korean (ko), 22

real    0m0.471s
user    0m0.819s
sys     0m0.237s
```
### Result of HPC run(1n8c):
```
Running, use core:  8
Data size: 20761096558
Each process handle: 2595137069
-------------------------------------
Hashtag Rank: 
1. #auspol, 19,878
2. #coronavirus, 10,110
3. #มาพ่องเพิ่งอะไร, 7,531
4. #firefightaustralia, 6,812
5. #oldme, 6,418
6. #sydney, 6,196
7. #scottyfrommarketing, 5,185
8. #grammys, 5,085
9. #assange, 4,689
10. #sportsrorts, 4,516
-------------------------------------
Language Rank: 
1. English (en), 3,107,116
2. Undefined (und), 252,117
3. Thai (th), 134,571
4. Portuguese (pt), 125,858
5. Spanish (es), 74,028
6. Japanese (ja), 49,929
7. Tagalog (tl), 44,560
8. Indonesian (in), 42,296
9. French (fr), 38,098
10. Arabic (ar), 24,501

real	0m36.179s
user	4m38.022s
sys	0m10.041s

```



