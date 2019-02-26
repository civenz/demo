@echo off

color 0a

:HOME
cls
set setChoice=
set tempIP=
set autoDNS=
set tempDNS1=
set tempDNS2=
set tempName=
set setIP=
set setDNS=
set setDNS1=
set setDNS2=
set setName=
set setGateway=


echo IP SETTING:
echo.
echo        Press 1 - �Զ���ȡ IP
echo        Press 2 - �ֶ����� IP
echo        Press 3 - Exit
echo.

set setChoice=yes

rem 3.0 = NT3
rem 3.5 = NT3.5
rem 4.0 = NT/WIN95
rem 4.1 = WIN98
rem 4.9 = WINME
rem 5.0 = WIN2000
rem 5.1 = WINXP
rem 5.2 = WIN2003
rem 6.0 = Vista/Server 2008
rem 6.1 = WIN7/Server 2008 R2
rem 6.2 = WIN8/Server 2012
rem 6.3 = WIN8.1/Server 2012 R2
rem 6.4 = WIN10
rem 10.0 = WIN10


ver | find "3.0">nul && IF Errorlevel 0 set setChoice=no
ver | find "3.5">nul && IF Errorlevel 0 set setChoice=no
ver | find "4.0">nul && IF Errorlevel 0 set setChoice=no
ver | find "4.1">nul && IF Errorlevel 0 set setChoice=no
ver | find "4.9">nul && IF Errorlevel 0 set setChoice=no
ver | find "5.0">nul && IF Errorlevel 0 set setChoice=no
ver | find "5.1">nul && IF Errorlevel 0 set setChoice=no
ver | find "5.2">nul && IF Errorlevel 0 set setChoice=no

IF "%setChoice%"=="yes" (
    CHOICE /c:123
    IF Errorlevel 3 GOTO Exit
    IF Errorlevel 2 GOTO STATIC
    IF ErrorLevel 1 GOTO DHCP
)


set /p setChoice=SETTING:
IF "%setChoice%"=="1" (
    GOTO DHCP
) ELSE IF "%setChoice%"=="2" (
    GOTO STATIC
) ELSE IF "%setChoice%"=="3" (
    GOTO EXIT
) ELSE (
    GOTO HOME
)


:DHCP
setlocal EnableDelayedExpansion

echo.
echo �����е�������������:
FOR /f "skip=1 tokens=*" %%i in ('wmic.exe nic get NetConnectionID') DO (
    FOR /f "delims=" %%i in ("%%i") DO (
        echo %%~nxi
    )
)
echo.

set /p tempName=�������������� (Ĭ��: Wireless Network Connection):

IF defined tempName (
    set setName=%tempName%
) ELSE (
    set setName=Wireless Network Connection
)

netsh interface ip set address name="%setName%" source=dhcp

echo.
echo �Ƿ����� DNS Ϊ�Զ���ȡ? y=�Զ���ȡ, n=�ֶ���ȡ, ����=����ԭ���ֶ�����DNS.
echo.
set /p autoDNS=�Զ���ȡ:

IF "%autoDNS%"=="y" (
    netsh interface ip set dns name="%setName%" source=dhcp
) else if "%autoDNS%"=="n" (
    set /p tempDNS1=�������һ�� DNS �����ַ:
    set /p tempDNS2=������ڶ��� DNS �����ַ:

    IF defined tempDNS1 (
        set setDNS1=!tempDNS1!
    ) ELSE (
        set setDNS1=8.8.8.8
    )

    IF defined tempDNS2 (
        set setDNS2=!tempDNS2!
    ) ELSE (
        set setDNS2=8.8.4.4
    )
    netsh interface ip set dns name="%setName%" source=static addr=!setDNS1! register=PRIMARY
    netsh interface ip add dns name="%setName%" addr=!setDNS2! index=2
)

endlocal

goto HOME


:STATIC
setlocal EnableDelayedExpansion

echo.
echo �����е�������������:
for /f "skip=1 tokens=*" %%i in ('wmic.exe nic get NetConnectionID') DO (
    for /f "delims=" %%i in ("%%i") DO (
        echo %%~nxi
    )
)
echo.

set /p tempName=�������������� (Ĭ��: Wireless Network Connection):
set /p tempIP=������ IP ��ַ (Ĭ��: 192.168.1.111):
set /p tempDNS1=�������һ�� DNS ��������ַ (Ĭ��: 8.8.8.8):
set /p tempDNS2=�������һ�� DNS ��������ַ (Ĭ��: 8.8.4.4):

IF defined tempIP (
    set setIP=%tempIP%
) ELSE (
    set setIP=192.168.1.111
)

FOR /F "tokens=1-3 delims=." %%i IN ("%setIP%") DO (
    set /a a = %%i
    set /a b = %%j
    set /a c = %%k
)
set setGateway=!a!.!b!.!c!.1

IF defined tempName (
    set setName=%tempName%
) ELSE (
    set setName=Wireless Network Connection
)

IF defined tempDNS1 (
    set setDNS1=%tempDNS1%
) ELSE (
    set setDNS1=8.8.8.8
)
IF defined tempDNS2 (
    set setDNS2=%tempDNS2%
) ELSE (
    set setDNS2=8.8.4.4
)


netsh interface ip set address name="%setName%" source=static addr=%setIP% mask=255.255.255.0 gateway=%setGateway% gwmetric=0
netsh interface ip set dns name="%setName%" source=static addr=%setDNS1% register=PRIMARY
netsh interface ip add dns name="%setName%" addr=%setDNS2% index=2

echo ��������:   %setName%
echo IP ��ַ:    %setIP%
echo ����:       255.255.255.0
echo ����:       %setGateway%
echo DNS1:       %setDNS1%
echo DNS2:       %setDNS2%

endlocal
pause
goto HOME


:EXIT
set setChoice=
rem exit