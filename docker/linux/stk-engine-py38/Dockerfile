# By default, start from the base STK Engine image
ARG baseImage=ansys/stk:latest-centos7
FROM ${baseImage}

# Install Python
USER root
RUN set -e; \
    yum -y install wget make gcc openssl-devel bzip2-devel libffi-devel tk-devel; \
    yum -y install python3 python3-tkinter python3.8-tkinter; \
    yum clean all; \
    rm -rf /var/cache/yum

# Install Python 3.8 and generate alias to it
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.8.16/Python-3.8.16.tgz && \
    tar xzf Python-3.8.16.tgz && \
    cd Python-3.8.16 && \
    ./configure --enable-optimizations && \
    make altinstall && \
    ln -sfn /usr/local/bin/python3.8 /usr/bin/python && \
    ln -sfn /usr/local/bin/pip3.8 /usr/bin/pip

# Switch back to non-root user
USER stk

# Update the path to include Python executables
ENV PATH="${STK_USER_HOME}/.local/bin:${PATH}" \
    PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

ENTRYPOINT [ "python3.8" ]
