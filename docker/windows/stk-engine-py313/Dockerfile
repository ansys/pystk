# By default, start from the base STK Engine Python image
ARG baseImage=ansys/stk-12.10:dev-windowsservercore-ltsc2019
ARG basePythonImage=ansys/stk-12.10:dev-windowsservercore-ltsc2019-pybase
FROM ${basePythonImage} as builder

USER ContainerAdministrator

COPY scripts C:/dist/

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

# Install Python
RUN Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe" -OutFile C:\dist\python-3.13.0-amd64.exe

RUN C:\dist\install.ps1

SHELL ["cmd", "/S", "/C"]

USER STK

# Update the pip environment variables
ENV PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

ENTRYPOINT [ "python" ]
