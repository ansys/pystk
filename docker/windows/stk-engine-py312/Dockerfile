# By default, start from the base STK Engine Python image
ARG basePythonImage=ansys/stk-13.0:dev-windowsservercore-ltsc2019-pybase
FROM ${basePythonImage} AS builder

USER ContainerAdministrator

COPY scripts C:/dist/

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

# Install Python
ADD "https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe" "C:\dist\python-3.12.4-amd64.exe"

RUN C:\dist\install.ps1

SHELL ["cmd", "/S", "/C"]

USER STK

# Update the pip environment variables
ENV PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

ENTRYPOINT [ "python" ]
