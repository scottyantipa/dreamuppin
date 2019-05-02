#!/bin/bash

# Followed instructions https://github.com/tensorflow/tensor2tensor

OUTPUT_DIR=$1
DATA_DIR=$T2T_DATA_DIR

PROBLEM="language_to_web"
MODEL="transformer"

# params used in initial training
HPARAMS="transformer_base_single_gpu"

t2t-trainer \
  --t2t_usr_dir=$USR_DIR \
  --data_dir=$DATA_DIR \
  --problem=$PROBLEM \
  --model=$MODEL \
  --hparams_set=$HPARAMS \
  --output_dir=$OUTPUT_DIR \
  --train_steps=10000
