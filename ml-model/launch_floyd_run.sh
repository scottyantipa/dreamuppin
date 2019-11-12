#!/bin/bash

# The references parameters (variance, train_steps) can be adjusted in train.sh
# and language_to_web.py

# permissions hacks: https://forum.floydhub.com/t/running-executable-gives-permission-denied/824
floyd run \
  --env tensorflow-1.10 \
  --gpu \
  -m "Running the full datagen-train-eval process with mturk data 3318 samples from combining all prior batches. 300000 train steps. With hparams transformer_base_single_gpu, beamsize 3, alpha 0.6." \
  'cd ./t2t-model && chmod +x ./gen_train_eval.sh && ./gen_train_eval.sh'
