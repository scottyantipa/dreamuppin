#!/bin/bash

# permissions hacks: https://forum.floydhub.com/t/running-executable-gives-permission-denied/824
floyd run \
  --env tensorflow-1.10 \
  --gpu \
  -m "Running the full datagen-train-eval process with variance = 10, train_steps = 1000" \
  'cd ./t2t-model && chmod +x ./gen_train_eval.sh && ./gen_train_eval.sh'
