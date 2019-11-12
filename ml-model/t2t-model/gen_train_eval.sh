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

# Assumes we are using the video tag data
echo 'Display a video from "http://video.com/video.mp4". Make it muted.' >> $INPUT_FILE
echo 'Display a video at the url "http://hello.com/ya.mp4". Loop the video at the end.' >> $INPUT_FILE
echo 'Show a video at the url "http://someurl.com/video.mp4" on loop. Mute the video.' >> $INPUT_FILE
echo 'Autoplay a video at the url "someurl.com/video.mp4". Loop the video.' >> $INPUT_FILE

# permissions hacks: https://forum.floydhub.com/t/running-executable-gives-permission-denied/824
chmod +x ./decode.sh
./decode.sh $INPUT_FILE $OUT_FILE
