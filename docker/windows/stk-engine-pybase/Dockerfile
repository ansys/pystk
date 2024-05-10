ARG baseImage=ansys/stk:dev-windowsservercore-ltsc2019
FROM ${baseImage}

USER ContainerAdministrator

# Directs python pip installs to pull packages from a specified repository.
# Delete the following two lines if you do not need to override the default pip repository URL.
ARG pipIndexUrl=''
ENV PIP_INDEX_URL=${pipIndexUrl}

SHELL ["cmd", "/S", "/C"]

USER STK