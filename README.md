# Exploring an implementation of The Dreamup

The Dreamup is an idea for a codeless alternative to the web. This repo is an initial exploration into using a tensor2tensor nlp model to produce HTML from a Dreamup application.

Status: This is in progress. Nothing is really working yet. There isn't yet a sufficient language->html dataset to feed our model. As it stands, the model prints out nonsense when given the nlp input. I'm looking at options of generating a valid dataset.

# What's inside?

The `ml-model` directory contains the language->html tensor2tensor problem. It is setup to be run on Floydhub.

The `data` directory contains:
* An example seq2seq dataset. The `t2t-model` dir contains a tensor2tensor problem which generates similar seq2seq data as well.
* hand written examples of nlp->html which are meant to server as example dreamup applications. These examples are not yet consumed by any model.

The `browser` dir is a super simple Dreamup browser. The `apps` dir are sample applications that you can point the dreamup browser at.

# Running the code
This repo is meant to be run on floydhub.com. The 'launch_floyd_run.sh' file will execute the full datagen-train-evaluate process. You will first need to setup your own floydhub project and purchase GPU credits. The environments and parameters can already be found in the code here.

# Contributing
Some possible areas to work on:
* producing a language->html dataset
* explore other models than seq2seq, like seq2tree
* implementing the server/client of the browser
* exploring different implementations all together (not nlp -> html)
