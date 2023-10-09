#!/bin/bash
#SBATCH -o ./out/job.%j.out		# 脚本执行的输出将被保存在当job.%j.out文件下，%j表示作业号;
#SBATCH --partition=gpulab01	# 作业提交的指定分区队列为 gpulab01
#SBATCH -J pytorch_job_1		# 作业在调度系统中的作业名为 pytorch_job_1
#SBATCH -N 1					# 申请节点数为1,如果作业不能跨节点(MPI)运行, 申请的节点数应不超过1
#SBATCH --ntasks-per-node=2
#SBATCH --gres=gpu:1
#SBATCH --qos=gpulab01			# 指定作业的QOS


source activate pytorch-1.6.0
python test.py

