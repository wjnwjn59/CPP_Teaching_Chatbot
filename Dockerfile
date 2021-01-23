FROM nvidia/cuda:10.1-devel-ubuntu18.04


WORKDIR /app

COPY . .

COPY environment.yml .
RUN conda env create -f environment.yml

RUN conda init bash

SHELL ["conda", "run", "-n", "new_rasa_fix_2", "/bin/bash", "-c"]
