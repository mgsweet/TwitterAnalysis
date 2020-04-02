#!/bin/bash
#SBATCH --partition physical
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=1
#SBATCH --job-name=1node_8cores

#SBATCH --mail-user=zhaofengq@student.unimelb.edu.au
#SBATCH --mail-type=FAIL

echo "1node8core:"

module load Python/3.7.3-spartan_gcc-8.1.0
time mpiexec python src/twitterAnalysis.py