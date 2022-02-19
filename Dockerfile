
FROM pytorch/torchserve:0.5.1-gpu


USER root

RUN pip install transformers==4.12.5

# for ain-py, use python 3.7
RUN apt-get update &&     apt-get install -y python3.7 python3-pip     python3.7-dev python3-wheel autoconf libtool pkg-config libffi-dev
RUN python3.7 -m pip install cython ain-py wheel flask requests
    
ARG MODEL_NAME=gpt2-trained-model
ENV MODEL_NAME $MODEL_NAME
ARG MODEL_DOWNLOAD_LINK
ENV MODEL_DOWNLOAD_LINK $MODEL_DOWNLOAD_LINK

RUN echo $MODEL_NAME
RUN echo $MODEL_DOWNLOAD_LINK
    
RUN echo default_workers_per_model=1 >> /home/model-server/config.properties
RUN echo default_response_timeout=3600 >> /home/model-server/config.properties
RUN echo unregister_model_timeout=3600 >> /home/model-server/config.properties

USER model-server
WORKDIR /home/model-server
RUN curl -X GET $MODEL_DOWNLOAD_LINK -o model-store/$MODEL_NAME.mar

ENV LRU_CACHE_CAPACITY 1

COPY server.py .

EXPOSE 8000

CMD ["torchserve", "--start", "--ncs", "--model-store=/home/model-server/model-store", "--models=$MODEL_NAME.mar", "&", "python3.7", "server.py"]
