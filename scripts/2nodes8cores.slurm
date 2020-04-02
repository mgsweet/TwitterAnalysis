#!/bin/bash
#SBATCH --partition physical
#SBATCH --time=00:20:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=1
#SBATCH --job-name=2node_8core
#SBATCH --output=2n8c.out

#SBATCH --mail-user=zhaofengq@student.unimelb.edu.au
#SBATCH --mail-type=FAIL

module load Python/3.7.3-spartan_gcc-8.1.0
time mpiexec -n 8 python src/twitterAnalysis.py