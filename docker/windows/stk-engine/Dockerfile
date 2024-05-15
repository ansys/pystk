ARG baseImage=mcr.microsoft.com/dotnet/framework/runtime:4.8-windowsservercore-ltsc2019
FROM $baseImage
ARG agreeToLicense=no

RUN net user STK /ADD

COPY distributions scripts C:/Users/STK/dist/

RUN powershell -Command $ErrorActionPreference = 'Stop'; \
    $ProgressPreference = 'SilentlyContinue'; \
    C:\Users\STK\dist\install.ps1 $Env:agreeToLicense

RUN icacls "C:\Users\STK" /grant STK:(OI)(CI)F /T
USER STK
RUN [ "C:/Program Files/AGI/STK 12/bin/AgNewUserSetup.exe", "force", "showDlg=Off", "allowOnline" ]

WORKDIR "C:\Users\STK"

CMD ["echo", "STK Engine requires a host application to run. Shutting down this container."]
