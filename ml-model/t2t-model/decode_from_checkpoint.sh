#!/bin/bash

# Run this to launch a floyd run that will use
# the output of a previous training run as a
# checkpoint for this model.

# See launch_decode_run.sh
export T2T_TRAIN_DIR="/floyd/input/model/output/t2t_train"
export T2T_DATA_DIR="/floyd/input/model/output/t2t_data"

SAVE_DIR="/floyd/home"
OUTPUT_DIR="$SAVE_DIR/output"
mkdir $OUTPUT_DIR

export USR_DIR="$SAVE_DIR/t2t-model/language_to_web"

# evaluate
EVAL_OUTPUT_DIR="$OUTPUT_DIR/model-eval"
mkdir -p $EVAL_OUTPUT_DIR
OUT_FILE="$EVAL_OUTPUT_DIR/output.txt"
touch $OUT_FILE

INPUT_FILE="$EVAL_OUTPUT_DIR/input.txt"
touch $INPUT_FILE

echo 'An image with the src "google.com"' >> $INPUT_FILE
echo 'An image with the src "source.com"' >> $INPUT_FILE

# permissions hacks: https://forum.floydhub.com/t/running-executable-gives-permission-denied/824
chmod +x ./decode.sh
./decode.sh $INPUT_FILE $OUT_FILE
