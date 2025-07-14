# By default, start from the base STK Engine Python image
ARG baseImage=ansys/stk-12.10:dev-ubuntu22.04
ARG basePythonImage=ansys/stk-12.10:dev-ubuntu22.04-pybase
FROM ${basePythonImage} as builder

##############################################
# 1) Build Python into its own builder stage
##############################################

# Install Python 3.10 and create a symbolic link named "python".
USER root
WORKDIR /tmp
RUN wget --no-check-certificate https://www.python.org/ftp/python/3.10.18/Python-3.10.18.tar.xz && \
    tar xf Python-3.10.18.tar.xz
WORKDIR /tmp/Python-3.10.18
RUN ./configure --with-openssl=/tmp/openssl --enable-optimizations && \
    make altinstall

#############################################################
# 2) Copy the Python build to the system in the second stage
#############################################################

FROM ${baseImage}
USER root

# Install required packages for X Window System and MESA graphics
RUN apt-get update -y; \
    apt-get install --no-install-recommends -y xserver-xorg xvfb xauth; \
    apt-get install --no-install-recommends -y mesa-utils libgl1-mesa-dri libglu1-mesa; \
    apt-get install --no-install-recommends -y tk; \
    apt-get install --no-install-recommends -y dos2unix; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*

# Set the display environment variable to allow GUI applications
ENV DISPLAY=:0

# Copy the Python interpreter, the standard library and pip to the final image
COPY --from=builder /usr/local/bin/python3.10 /usr/local/bin/python3.10
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin/pip3.10 /usr/local/bin/pip3.10

RUN ln -sfn /usr/local/bin/python3.10 /usr/local/bin/python && \
    ln -sfn /usr/local/bin/pip3.10 /usr/local/bin/pip

COPY docker-entrypoint.sh "${STK_USER_HOME}/bin/docker-entrypoint.sh"
RUN chmod +x "${STK_USER_HOME}/bin/docker-entrypoint.sh"; \
    dos2unix "${STK_USER_HOME}/bin/docker-entrypoint.sh"

# Fix timezone and localtime. See the following issue with Ubuntu 20.04:
# Issue: https://bugs.launchpad.net/ubuntu/+source/tzdata/+bug/1899343
RUN set -e; \
    ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime; \
    echo 'Etc/UTC' > /etc/timezone

# Switch back to non-root user
USER stk

# Update the path to include Python executables
ENV PATH="/usr/local/bin:${STK_USER_HOME}/.local/bin:${PATH}" \
    PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

# Use the entrypoint script
ENTRYPOINT [ "docker-entrypoint.sh" ]
