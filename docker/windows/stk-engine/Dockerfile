ARG baseImage=mcr.microsoft.com/dotnet/framework/runtime:4.8-windowsservercore-ltsc2019
FROM $baseImage
ARG agreeToLicense=no

# Add the engine packages to the builder stage
COPY distributions scripts C:/dist/

# Unpack engine
SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]
RUN C:\dist\install.ps1 $Env:agreeToLicense

USER ContainerUser
WORKDIR "C:/Program Files/AGI/STK 12/bin"
RUN [ "C:/Program Files/AGI/STK 12/bin/AgNewUserSetup.exe", "force", "showDlg=Off", "allowOnline" ]

CMD echo 'STK Engine requires a host application to run. Shutting down this container.'

# Copy shared library to enable Code 500 Ephemeris file format support
# which is used by some of the tests
RUN (mkdir -p /stk/Modules) -and (cp -Force /stk/bin/libagascode500.so /stk/Modules/)

# Set the base image for the next stage
FROM ${baseImage}

LABEL ANSYSLMD_LICENSE_FILE='Specifies the location of the Ansys Licensing Server. The format should be PORT@FQDN. If using a triad of license servers, list all servers in the same format separated by semicolons.  Required.'

# Define STK user home directory
ENV STK_USER_HOME=/home/stk

# Setup non-root STK user
RUN set -e; \
    useradd -ms /bin/bash stk; \
    yum -y install libgfortran5

# Switch to STK user
USER stk

# Copy files from the builder stage
COPY --from=builder --chown=stk /stk/ "${STK_USER_HOME}"/

# Configure environment
ENV LD_LIBRARY_PATH="${STK_USER_HOME}/bin" \
    PATH="${STK_USER_HOME}/bin:${PATH}" \
    STK_CONFIG_DIR="${STK_USER_HOME}/config" \
    STK_INSTALL_DIR="${STK_USER_HOME}"

# Run new user install
WORKDIR "C:/Program Files/AGI/STK 12/bin"
RUN [ "C:/Program Files/AGI/STK 12/bin/AgNewUserSetup.exe", "force", "showDlg=Off", "allowOnline" ]

CMD echo 'STK Engine requires a host application to run. Shutting down this container.'
