echo "Run src/twitterAnalysis with MPI"
time mpiexec -n 1 python3 src/twitterAnalysis.py -f "data/smallTwitter.json"