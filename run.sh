echo "Run src/twitterAnalysis with MPI"
time mpiexec -n 4 python3 src/twitterAnalysis.py -f "data/smallTwitter.json"