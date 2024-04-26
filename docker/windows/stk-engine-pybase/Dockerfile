ARG baseImage=ansys/stk:dev-windowsservercore-ltsc2019
FROM ${baseImage}

USER ContainerAdministrator

# PIP Configuration
ENV PIP_CERT=c:/Temp/certificates/ca-bundle.crt

# Directs python pip installs to pull packages from a specified repository.
# Delete the following two lines if you do not need to override the default pip repository URL.
ARG pipIndexUrl=''
ENV PIP_INDEX_URL=${pipIndexUrl}

SHELL ["cmd", "/S", "/C"]

USER STK