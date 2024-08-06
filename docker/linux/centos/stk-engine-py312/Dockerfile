# By default, start from the base STK Engine Python image
ARG baseImage=ansys/stk:dev-centos7
ARG basePythonImage=ansys/stk:dev-centos7-pybase
FROM ${basePythonImage} as builder

##############################################
# 1) Build Python into its own builder stage
##############################################

# Install Python 3.12 and create a symbolic link named "python".
# This overrides the default Python 2.7 in CentOS7.
USER root
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.12.4/Python-3.12.4.tar.xz && \
    tar xf Python-3.12.4.tar.xz
WORKDIR /tmp/Python-3.12.4
RUN ./configure --enable-optimizations && \
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
    yum -y install tk; \
    yum -y install dos2unix; \
    yum clean all;

# Set the display environment variable to allow GUI applications
ENV DISPLAY=:0

# Copy the Python interpreter, the standard library and pip to the final image
COPY --from=builder /usr/local/bin/python3.12 /usr/local/bin/python3.12
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin/pip3.12 /usr/local/bin/pip3.12

RUN ln -sfn /usr/local/bin/python3.12 /usr/local/bin/python && \
    ln -sfn /usr/local/bin/pip3.12 /usr/local/bin/pip

COPY docker-entrypoint.sh "${STK_USER_HOME}/bin/docker-entrypoint.sh"
RUN chmod +x "${STK_USER_HOME}/bin/docker-entrypoint.sh"; \
    dos2unix "${STK_USER_HOME}/bin/docker-entrypoint.sh"

# Switch back to non-root user
USER stk

# Update the path to include Python executables
ENV PATH="/usr/local/bin:${STK_USER_HOME}/.local/bin:${PATH}" \
    PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

# Use the entrypoint script
ENTRYPOINT [ "docker-entrypoint.sh" ]
