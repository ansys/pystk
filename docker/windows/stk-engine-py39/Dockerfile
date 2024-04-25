# By default, start from the base STK Engine Python image
ARG baseImage=ansys/stk:dev-windowsservercore-ltsc2019
ARG basePythonImage=ansys/stk:dev-windowsservercore-ltsc2019-pybase
FROM ${basePythonImage} as builder

USER ContainerAdministrator

# Install Python
ADD "https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe" "C:\dist\python-3.9.13-amd64.exe"

COPY  scripts C:/dist/

RUN powershell -Command $ErrorActionPreference = 'Stop'; \
    $ProgressPreference = 'SilentlyContinue'; \
    C:\dist\install.ps1 $Env:agreeToLicense

USER STK

# Update the pip environment variables
ENV PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

ENTRYPOINT [ "python" ]