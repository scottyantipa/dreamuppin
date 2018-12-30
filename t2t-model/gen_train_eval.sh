#!/bin/bash

#
# Generates data, trains, and evaluates
#

SAVE_DIR="/floyd/home"
OUTPUT_DIR="$SAVE_DIR/output"
mkdir $OUTPUT_DIR

export USR_DIR="$SAVE_DIR/t2t-model/language_to_web"
export T2T_DATA_DIR="$OUTPUT_DIR/t2t_data"
export T2T_TRAIN_DIR="$OUTPUT_DIR/t2t_train"
export TMP_DIR="$SAVE_DIR/tmp"

mkdir $T2T_DATA_DIR
mkdir $T2T_TRAIN_DIR
mkdir $TMP_DIR

# make dataset
# permissions hacks: https://forum.floydhub.com/t/running-executable-gives-permission-denied/824
chmod +x ./gen_data.sh
./gen_data.sh $TMP_DIR

# train
# permissions hacks: https://forum.floydhub.com/t/running-executable-gives-permission-denied/824
chmod +x ./train.sh
./train.sh $T2T_DATA_DIR

# evaluate
EVAL_OUTPUT_DIR="$OUTPUT_DIR/model-eval"
mkdir -p $EVAL_OUTPUT_DIR
OUT_FILE="$EVAL_OUTPUT_DIR/output.txt"
touch $OUT_FILE

INPUT_FILE="$EVAL_OUTPUT_DIR/input.txt"
touch $INPUT_FILE

echo 'An image with the src "google.com"' >> $INPUT_FILE
echo 'An image with the src "source.com"' >> $INPUT_FILE
echo 'A paragraph with the words "hello friend"' >> $INPUT_FILE
echo 'An image with the source "source" and width of "30" and height of "20"' >> $INPUT_FILE
echo 'Bold sentence with words "hello friend"' >> $INPUT_FILE
# permissions hacks: https://forum.floydhub.com/t/running-executable-gives-permission-denied/824
chmod +x ./decode.sh
./decode.sh $INPUT_FILE $OUT_FILE
