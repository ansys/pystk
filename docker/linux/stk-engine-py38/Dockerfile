# By default, start from the base STK Engine Python image
ARG baseImage=ansys/stk:latest-centos7
ARG basePythonImage=ansys/stk:latest-centos7-pybase
ARG withGraphics=true
FROM ${basePythonImage} as builder

##############################################
# 1) Build Python into its own builder stage
##############################################

# Install Python 3.8 and create a symbolic link named "python".
# This overrides the default Python 2.7 in CentOS7.
USER root
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.8.16/Python-3.8.16.tgz && \
    tar xzf Python-3.8.16.tgz && \
    cd Python-3.8.16 && \
    ./configure --enable-optimizations && \
    make altinstall

#############################################################
# 2) Copy the Python build to the system in the second stage
#############################################################

# Switch back to non-root user
FROM ${baseImage}
USER root

# Copy the Python interpreter, the standard library and pip to the final image
COPY --from=builder /usr/local/bin/python3.8 /usr/local/bin/python3.8 
COPY --from=builder /usr/local/lib/python3.8 /usr/local/lib/python3.8 
COPY --from=builder /usr/local/bin/pip3.8 /usr/local/bin/pip3.8 

RUN ln -sfn /usr/local/bin/python3.8 /usr/bin/python && \
    ln -sfn /usr/local/bin/pip3.8 /usr/bin/pip

# Install graphic utilities (if needed)
RUN set -e; \
    if [ "$withGraphics" = "true" ]; then \
        yum groupinstall -y "X Window System"; \
        yum install mesa-libGL mesa-libGL-devel mesa-libGLU mesa-libGLU-devel; \
        yum -y install tkinter python3-tkinter; \
        yum clean all; \
        rm -rf /var/cache/yum; \
    fi;

# Switch back to non-root user
USER stk

# Update the path to include Python executables
ENV PATH="${STK_USER_HOME}/.local/bin:${PATH}" \
    PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

ENTRYPOINT [ "python3.8" ]
