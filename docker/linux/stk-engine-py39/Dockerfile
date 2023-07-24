# By default, start from the base STK Engine Python image
ARG baseImage=ansys/stk:latest-centos7
ARG basePythonImage=ansys/stk:latest-centos7-pybase
ARG withGraphics=true
FROM ${basePythonImage} as builder

##############################################
# 1) Build Python into its own builder stage
##############################################

# Install Python 3.9 and create a symbolic link named "python".
# This overrides the default Python 2.7 in CentOS7.
USER root
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz && \
    tar xzf Python-3.9.16.tgz && \
    cd Python-3.9.16 && \
    ./configure --enable-optimizations && \
    make altinstall

#############################################################
# 2) Copy the Python build to the system in the second stage
#############################################################

# Switch back to non-root user
FROM ${baseImage}
USER root

# Install required packages for X Window System and MESA graphics
RUN yum -y install xorg-x11-server-Xorg xorg-x11-server-Xvfb xorg-x11-xauth; \
    yum -y install mesa-dri-drivers mesa-libGLU; \
    yum -y install glxinfo; \
    yum -y install tkinter python3-tkinter; \
    yum clean all;

# Set the display environment variable to allow GUI applications
ENV DISPLAY=:0

# Copy the Python interpreter, the standard library and pip to the final image
COPY --from=builder /usr/local/bin/python3.9 /usr/local/bin/python3.9 
COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9 
COPY --from=builder /usr/local/bin/pip3.9 /usr/local/bin/pip3.9 

RUN ln -sfn /usr/local/bin/python3.9 /usr/bin/python && \
    ln -sfn /usr/local/bin/pip3.9 /usr/bin/pip

# Switch back to non-root user
USER stk

# Update the path to include Python executables
ENV PATH="${STK_USER_HOME}/.local/bin:${PATH}" \
    PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

# Start Xvfb in background mode
CMD ["Xvfb", "$DISPLAY", "+extension", "GLX", "-screen", "0", "1024x768x24", "&"]

ENTRYPOINT [ "bash" ]
