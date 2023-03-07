# By default, start from the base STK Engine image
ARG baseImage=ansys/stk:latest-centos7
FROM ${baseImage}

# Install Python 3.8 and create a symbolic link named "python".
# This overrides the default Python 2.7 in CentOS7.
USER root
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
