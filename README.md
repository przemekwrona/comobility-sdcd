# co-mobility ATHENA

co-mobility ATHENA is a subproject of project co-mobility that build a system to collect, store and analyze public
transport data.

## Installation

Create environment with Conda https://docs.conda.io/

```shell
conda env create -f environment.yml
```

If your environment has been created before and you need only update dependencies run script below

```shell
conda env update --file environment.yml --prune
```

## Run

Run project with python 2.7

```shell
python main.py
```

## Data prepartion 

Copy data from Hadoop to Local filesystem

```shell
hadoop fs -copyToLocal /projects/co-mobility/data/warsaw/vehicles-delay-between-stops/2021-12-13/ /home/hdfs
```

Copy data from remote machine to local computer

```shell
scp wronap2@192.168.137.213:/home/hdfs/2021-12-11 C:/workspace
```