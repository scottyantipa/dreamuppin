#!/bin/bash

# Generates data for the t2t problem
# Followed instructions https://github.com/tensorflow/tensor2tensor

# On floyd this would be /floyd/home/tmp
TMP_DIR=$1
DATA_DIR=$T2T_DATA_DIR
PROBLEM="language_to_web"

t2t-datagen \
  --t2t_usr_dir=$USR_DIR \
  --data_dir=$DATA_DIR \
  --tmp_dir=$TMP_DIR \
  --problem=$PROBLEM \
