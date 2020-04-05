#!/bin/bash
#SBATCH --partition physical
#SBATCH --time=00:20:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --job-name=4node_8core
#SBATCH --output=4n8c.out

#SBATCH --mail-user=zhaofengq@student.unimelb.edu.au
#SBATCH --mail-type=FAIL

module load Python/3.6.4-intel-2017.u2-GCC-6.2.0-CUDA9
time mpiexec python src/twitterAnalysis.py