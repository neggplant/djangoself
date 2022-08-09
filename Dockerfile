FROM djangoself:base

WORKDIR /djangoself
COPY . /djangoself

RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt
USER root
EXPOSE 7778
EXPOSE 7779

ENTRYPOINT ["/bin/bash"]