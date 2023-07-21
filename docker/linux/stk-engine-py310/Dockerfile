# By default, start from the base STK Engine Python image
ARG baseImage=ansys/stk:latest-centos7
ARG basePythonImage=ansys/stk:latest-centos7-pybase
ARG withGraphics=true
FROM ${basePythonImage} as builder

##############################################
# 1) Build Python into its own builder stage
##############################################

# Install Python 3.10 and create a symbolic link named "python".
# This overrides the default Python 2.7 in CentOS7.
USER root
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz && \
    tar xzf Python-3.10.10.tgz && \
    cd Python-3.10.10 && \
    ./configure --enable-optimizations && \
    make altinstall

#############################################################
# 2) Copy the Python build to the system in the second stage
#############################################################

# Switch back to non-root user
FROM ${baseImage}
USER root

# Install required packages for X Window System and MESA graphics
RUN yum -y xorg-x11-server-Xorg xorg-x11-xauth xorg-x11-apps xorg-x11-utils xorg-x11-server-Xvfb; \
    yum -y install mesa-dri-drivers; \
    yum -y install tkinter python3-tkinter; \
    yum clean all;

# Set the display environment variable to allow GUI applications
ENV DISPLAY=:0

# Copy the Python interpreter, the standard library and pip to the final image
COPY --from=builder /usr/local/bin/python3.10 /usr/local/bin/python3.10 
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10 
COPY --from=builder /usr/local/bin/pip3.10 /usr/local/bin/pip3.10 

RUN ln -sfn /usr/local/bin/python3.10 /usr/bin/python && \
    ln -sfn /usr/local/bin/pip3.10 /usr/bin/pip

# Switch back to non-root user
USER stk

# Update the path to include Python executables
ENV PATH="${STK_USER_HOME}/.local/bin:${PATH}" \
    PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

ENTRYPOINT [ "python3.10" ]
