ARG baseImage=ubuntu:22.04
FROM ${baseImage} AS builder

# Add the engine packages to the builder stage
COPY distributions/stk*.tgz /tmp/

# Unpack engine
RUN set -e; \
    mkdir -p /stk; \
    find /tmp -name stk*.tgz -exec tar -zxf {} --strip-components=1 -C /stk \;

# Copy shared library to enable Code 500 Ephemeris file format support
# which is used by some of the tests
RUN mkdir -p /stk/Modules && cp -f /stk/bin/libagascode500.so /stk/Modules/

# Reduce image size by removing unnecessary components 
#
# Keep Intro_STK_Aircraft_Systems.vdf as it is required to
# run sone of the tests
# If this VDF is not needed in your use case, replace the
# find command with:
#     rm -rf /stk/Data/ExampleScenarios/
#
# Also keep the VO directory as it is required to run the
# 2D and 3D tests
# If the VO directory is not needed in your use case, add:
#     rm -rf /stk/STKData/VO; \
RUN set -e; \
    find /stk/Data/ExampleScenarios/ -type f -not -name 'Intro_STK_Aircraft_Systems.vdf' -exec rm -rf {} \;; \
    rm -rf /stk/Data/HtmlInterface/; \
    rm -rf /stk/Data/HtmlUtilities/; \
    rm -rf /stk/Data/LicAndReg/; \
    rm -rf /stk/Data/Resources/; \
    rm -rf /stk/Data/Viewer/; \
    rm -rf /stk/licensingclient/linx64/ClientSettings

# Set the base image for the next stage
FROM ${baseImage}

LABEL ANSYSLMD_LICENSE_FILE='Specifies the location of the Ansys Licensing Server. The format should be PORT@FQDN. If using a triad of license servers, list all servers in the same format separated by semicolons.  Required.'

# Define STK user home directory
ENV STK_USER_HOME=/home/stk

# Setup non-root STK user
RUN set -e; \
    useradd -ms /bin/bash stk; \
    apt-get install -y libgfortran5

# Switch to STK user
WORKDIR "${STK_USER_HOME}"
USER stk

# Copy files from the builder stage
COPY --from=builder --chown=stk /stk/ "${STK_USER_HOME}"/

# Configure environment
ENV LD_LIBRARY_PATH="${STK_USER_HOME}/bin" \
    PATH="${STK_USER_HOME}/bin:${PATH}" \
    STK_CONFIG_DIR="${STK_USER_HOME}/config" \
    STK_INSTALL_DIR="${STK_USER_HOME}"

# Run new user install
RUN stkxnewuser /force /allowOnline=yes

CMD echo 'STK Engine requires a host application to run. Shutting down this container.'
