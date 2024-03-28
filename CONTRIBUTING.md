# Contributing

## Using Tox for testing and development

[Tox](https://tox.wiki) is a powerful tool that simplifies and automates the
process of testing and developing your project across multiple environments. It
allows you to define test environments, run tests, and perform various
development tasks in a consistent and reproducible manner. Tox is particularly
useful for ensuring that your project works seamlessly on different Python
versions, interpreters, and platforms.

## Installing Tox

To install Tox, you can use the following command:

```console
python -m pip install tox
```

You can verify the installation by running:

```console
tox --version
```

## Listing Tox environments

The configuration for Tox is stored in [the tox.ini file](https://github.com/ansys-internal/pystk/blob/main/tox.ini). 
This file contains various environments. Environments are a collection of
commands executed depending on the platform and the environment.

To list all Tox environments, you can use the following command:

```console
tox list
```

## Building the STK container images with Tox

Use the following commands to build the images:

### Linux

```console
tox -e docker-build-linux_images
```

This will result in the following images:

```bash
~$ docker images

REPOSITORY   TAG                         IMAGE ID       CREATED          SIZE
ansys/stk    latest-centos7-python3.8    bffb1a81b5ba   31 seconds ago   2.75GB
ansys/stk    latest-centos7-python3.10   f045f5453c31   43 seconds ago   2.77GB
ansys/stk    latest-centos7-python3.9    48c6275abedb   49 seconds ago   2.76GB
ansys/stk    latest-centos7-pybase       85117878fee1   2 minutes ago    3.22GB
ansys/stk    latest-centos7              bf55f684403c   6 minutes ago    2.37GB
centos       7                           f87a3c43c945   10 minutes ago   205MB
```

### Windows

```console
tox -e docker-build-windows_images
```

This will result in the following images:


```bash
~$ docker images


REPOSITORY                                         TAG                                         IMAGE ID       CREATED        SIZE
ansys/stk                                          dev-windowsservercore-ltsc2019-python3.10   da112bee5232   13 hours ago   11.1GB
ansys/stk                                          dev-windowsservercore-ltsc2019-pybase       6386ed51b256   13 hours ago   10.9GB
ansys/stk                                          dev-windowsservercore-ltsc2019              59ab48f41f9c   13 hours ago   10.8GB
mcr.artifactory.stk.com/dotnet/framework/runtime   4.8-windowsservercore-ltsc2019              6b8d98588f15   6 weeks ago    6.91GB
mcr.microsoft.com/dotnet/framework/runtime         4.8-windowsservercore-ltsc2019              6b8d98588f15   6 weeks ago    6.91GB
```
## Running an STK container with Tox

Once the images are built, you can create a new container targeting a specific Python version using the following command:

> [!NOTE]
>Make sure that the ANSYSLMD_LICENSE_FILE environment variable is properly configured before starting the container.

```console
tox -f docker-run-{linux_container,windows_container}-{py38,py39,py310}
```

This will start a new virtual environment inside the container and install all the dependencies required to run the tests and generate the project documentation. This will also install Jupyter Lab and its dependencies in that virtual environment.

In the previous command, you need to select the OS and Python version you want to
use, for instance `tox -f docker-run-linux_container-py310` will start a Linux container configured with Python 3.10.

## Executing a command inside an STK container with Tox

After building the images and running a container, you can execute a command inside the container using:

```console
tox -f docker-exec-{linux_container,windows_container}-{py38,py39,py310} -- {command}
```

For instance, to run `ls -la` inside a previously started Linux Python 3.10 container, use:

```console
tox -f docker-exec-linux_container-py310 -- ls -la
```

Here are a few additional examples:
### Linux
- Starting a interactive shell inside the container:
    ```console
    tox -f docker-exec-windows_container-py310 -- cmd
    ```
- Running the Aviator tests in no graphics mode inside the container:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkXNoGfx --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the Aviator tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkX --exclude SEET --exclude PluginTests -vv
    ```
- Running the VGT tests in no graphics mode:
    ```console
    tox -f docker-exec-linux_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkXNoGfx --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the VGT tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkX --exclude SEET --exclude PluginTests -vv
    ```
- Running the STK Vehicle tests in no graphics mode excluding (*deselecting* in pytest terminology) one test:
    ```console
    tox -f docker-exec-linux_container-py310 -- pytest pystk/tests/generated/stk_tests/vehicle --target StkXNoGfx --deselect=vehicle/satellite/astrogator/astrogator.py::EarlyBoundTests::test_CompBrowsCutCopyPaste --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv 
    ```
- Running the STK tests with graphics:
    ```console
    tox -f docker-exec-linux_container-py310 -- pytest pystk/tests/generated/stk_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```
### Windows
- Starting a interactive shell inside the container:
    ```console
    tox -f docker-exec-windows_container-py310 -- cmd
    ```
- Running the Aviator tests in no graphics mode inside the container:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkXNoGfx --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the Aviator tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkX --exclude SEET --exclude PluginTests -vv
    ```
- Running the VGT tests in no graphics mode:
    ```console
    tox -f docker-exec-linux_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkXNoGfx --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the VGT tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkX --exclude SEET --exclude PluginTests -vv
    ```
- Running the STK Vehicle tests in no graphics mode excluding (*deselecting* in pytest terminology) one test:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/stk_tests/vehicle --target StkXNoGfx --deselect=vehicle/satellite/astrogator/astrogator.py::EarlyBoundTests::test_CompBrowsCutCopyPaste --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv 
    ```
- Running the STK tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/stk_tests --target StkX --exclude SEET --exclude PluginTests -vv
    ```

## Launching Jupyter Lab with Tox

After building the images and running a container, you can also start Jupyter Lab inside the container using:

```
tox -f docker-lab-linux_container-{py38,py39,py310}
```

In the previous command, you need to select the Python version you want to
use, for instance `tox -f docker-lab-linux_container-py310` will start a Linux container configured with Python 3.10.

Once Jupyter Lab is running, use your browser to navigate to http://127.0.0.1:8888/lab?token=pystk.

## Troubleshooting an STK container in UI mode with Tox 

After building the images and running a container, you can also start a desktop manager inside the container. This provides access to the X graphical user interface. This is particularly useful to troubleshoot any issue arising inside the container. A use case is debugging the graphics tests, as STK's 2D and 3D graphics are rendered inside the container using `xvfb` which is not visible by default.

To start the container in User Interface mode, run the following command:

```
tox -f docker-novnc-linux_container-{py38,py39,py310}
```

Once the container is ready, use your browser to navigate to http://127.0.0.1:8888/vnc_auto.html. This will give you access to a simple X11 desktop based on [fluxbox](http://fluxbox.org/), a lightweight windows manager. The user interface is served to your browser using VNC and [novnc](https://novnc.com/info.html). An xterm is also opened on the desktop, with the virtual environment required to run the Python tests activated.

In addition to running the UI, this configuration also enables `sudo` for the stk user (password identical as user name), so you can install any additional debugging tools required (for instance `gdb` or `valgrind`).

## Stopping an STK container with Tox

You can stop a running container using:

```
tox -f docker-stop-linux_container-{py38,py39,py310}
```

## Removing an STK container with Tox

You can remove a container using:

```
tox -f docker-rm-linux_container-{py38,py39,py310}
```

## Additional documentation

For additional documentation refer to the
[PyAnsys Developer's Guide](https://dev.docs.pyansys.com/index.html).
