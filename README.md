# HPC Twitter Processing
COMP90024 Cluster and Cloud Computing Assignment 1

## How to run:
1. Run with `run.sh`, it would automately use 4 cores to run the application with `data/smallTwitter.json`.
    ```shell
    ./run.sh
    ```
2. Run with command:
    ```shell
    time mpiexec -n 4 python3 src/twitterAnalysis.py -f <datapath>
    ```

## Result:

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

## Script Usage:
1. Change the  username, password and data path in `pushToSpartan.sh` to your own info
2. Also change the info in `pullOut` to your own info.
3. Install `export` by `brew install export`.
4. Use `export pushToSpartan.sh` to push file to spartan.
5. Use `export pullOut` to pull the output file from spartan.



