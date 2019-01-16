#!/bin/bash

floyd run \
  --env tensorflow-1.10 \
  --gpu \
  --data "scottantipa/projects/dreamup-nlp/37:model" \
  -m "Decode from a model checkpoint" \
  "cd ./t2t-model && chmod +x ./decode_from_checkpoint.sh && ./decode_from_checkpoint.sh"
