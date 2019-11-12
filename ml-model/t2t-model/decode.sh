#!/bin/bash

# Followed instructions https://github.com/tensorflow/tensor2tensor

DECODE_FILE=$1
DECODE_TO_FILE=$2

DATA_DIR=$T2T_DATA_DIR
TRAIN_DIR=$T2T_TRAIN_DIR

PROBLEM="language_to_web"
MODEL="transformer"

BEAM_SIZE="3"
ALPHA="0.6"

t2t-decoder \
  --t2t_usr_dir=$USR_DIR \
  --data_dir=$DATA_DIR \
  --problem=$PROBLEM \
  --model=$MODEL \
  --hparams_set="transformer_base_single_gpu" \
  --output_dir=$TRAIN_DIR \
  --decode_hparams="beam_size=$BEAM_SIZE,alpha=$ALPHA" \
  --decode_from_file=$DECODE_FILE \
  --decode_to_file=$DECODE_TO_FILE
