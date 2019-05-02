#!/bin/bash

# The references parameters (variance, train_steps) can be adjusted in train.sh
# and language_to_web.py

# permissions hacks: https://forum.floydhub.com/t/running-executable-gives-permission-denied/824
floyd run \
  --env tensorflow-1.10 \
  --gpu \
  -m "Running the full datagen-train-eval process with mturk data 1011 samples. 10000 train steps." \
  'cd ./t2t-model && chmod +x ./gen_train_eval.sh && ./gen_train_eval.sh'
