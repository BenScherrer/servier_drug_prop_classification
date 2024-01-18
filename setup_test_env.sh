#!/bin/bash

export PATH=~/miniconda/bin:$PATH

echo "UPDATED PATH : $PATH"

source activate servier

flask --app main run