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

Use the following commands to build the images for your target distribution:
- **centos**
    ```console
    tox -e docker-build-centos_images
    ```
    This will result in the following images:

    ```bash
    ~$ docker images

    REPOSITORY   TAG                         IMAGE ID       CREATED          SIZE
    ansys/stk    dev-centos7-python3.8    bffb1a81b5ba   31 seconds ago   2.75GB
    ansys/stk    dev-centos7-python3.10   f045f5453c31   43 seconds ago   2.77GB
    ansys/stk    dev-centos7-python3.9    48c6275abedb   49 seconds ago   2.76GB
    ansys/stk    dev-centos7-pybase       85117878fee1   2 minutes ago    3.22GB
    ansys/stk    dev-centos7              bf55f684403c   6 minutes ago    2.37GB
    centos       7                        f87a3c43c945   10 minutes ago   205MB
    ```
- **ubuntu**
    ```console
    tox -e docker-build-ubuntu_images
    ```
    This will result in the following images:

    ```bash
    ~$ docker images

    REPOSITORY   TAG                             IMAGE ID       CREATED          SIZE
    ansys/stk    dev-ubuntu22.04-python3.10   b73373a4f70f   11 seconds ago   3.75GB
    ansys/stk    dev-ubuntu22.04-python3.9    da1e30388a60   15 seconds ago   3.74GB
    ansys/stk    dev-ubuntu22.04-python3.8    7492f6675ae8   22 seconds ago   3.74GB
    ansys/stk    dev-ubuntu22.04-pybase       e2207493249c   2 minutes ago    4.15GB
    ansys/stk    dev-ubuntu22.04              4fa0a28358bd   7 minutes ago    3.13GB
    ubuntu       22.04                        1c6025966a65   8 minutes ago    133MB
    ```
- **Windows**
    ```console
    tox -e docker-build-windows_images -- agreeToLicense=yes
    ```
    This will result in the following images:

    ```bash
    ~$ docker images

    REPOSITORY                                         TAG                                         IMAGE ID       CREATED        SIZE
    ansys/stk                                          dev-windowsservercore-ltsc2019-python3.10   8399f5359163   2 hours ago   20.9GB
    ansys/stk                                          dev-windowsservercore-ltsc2019-python3.9    12ed5235a1e4   2 hours ago   20.9GB
    ansys/stk                                          dev-windowsservercore-ltsc2019-python3.8    0e5d12988064   2 hours ago   20.9GB
    ansys/stk                                          dev-windowsservercore-ltsc2019-pybase       00868a57cc61   3 hours ago   20.7GB
    ansys/stk                                          dev-windowsservercore-ltsc2019              a8e6508529ba   3 hours ago   20.7GB
    mcr.microsoft.com/dotnet/framework/runtime         4.8-windowsservercore-ltsc2019              6b8d98588f15   4 weeks ago   6.91GB
    ```


## Running an STK container with Tox

Once the images are built, you can create a new container targeting a specific Python version using the following command:

> [!NOTE]
>Make sure that the ANSYSLMD_LICENSE_FILE environment variable is properly configured before starting the container.

```console
tox -f docker-run-{centos,ubuntu,windows}_container-{py38,py39,py310}
```

This will start a new virtual environment inside the container and install all the dependencies required to run the tests and generate the project documentation. This will also install Jupyter Lab and its dependencies in that virtual environment.

In the previous command, you need to select the Python version you want to
use, for instance:
- `tox -f docker-run-centos_container-py38` will start a CentOS container configured with Python 3.8.
- `tox -f docker-run-ubuntu_container-py39` will start a Ubuntu container configured with Python 3.9.
- `tox -f docker-run-windows_container-py310` will start a Windows container configured with Python 3.10.

## Executing a command inside an STK container with Tox

After building the images and running a container, you can execute a command inside the container using:

```console
tox -f docker-exec-{centos,ubuntu,windows}_container-{py38,py39,py310} -- {command}
```

For instance, to run `ls -la` inside a previously started CentOS Python 3.10 container, use:

```console
tox -f docker-exec-centos_container-py310 -- ls -la
```

Here are a few additional examples:
### centOS
- Starting a interactive shell inside the container:
    ```console
    tox -f docker-exec-centos_container-py310 -- /bin/bash
    ```
- Running the Aviator tests in no graphics mode inside the container:
    ```console
    tox -f docker-exec-centos_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkXNoGfx --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the Aviator tests with graphics:
    ```console
    tox -f docker-exec-centos_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```
- Running the VGT tests in no graphics mode:
    ```console
    tox -f docker-exec-centos_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkXNoGfx --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the VGT tests with graphics:
    ```console
    tox -f docker-exec-centos_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```console
- Running the STK Vehicle tests in no graphics mode excluding (*deselecting* in pytest terminology) one test:
    ```
    tox -f docker-exec-centos_container-py310 -- pytest pystk/tests/generated/stk_tests/vehicle --target StkXNoGfx --deselect=vehicle/satellite/astrogator/astrogator.py::EarlyBoundTests::test_CompBrowsCutCopyPaste --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv 
    ```
- Running the STK tests with graphics:
    ```console
    tox -f docker-exec-centos_container-py310 -- pytest pystk/tests/generated/stk_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```
### ubuntu
- Starting a interactive shell inside the container:
    ```console
    tox -f docker-exec-ubuntu_container-py310 -- /bin/bash
    ```
- Running the Aviator tests in no graphics mode inside the container:
    ```console
    tox -f docker-exec-ubuntu_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkXNoGfx --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the Aviator tests with graphics:
    ```console
    tox -f docker-exec-ubuntu_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```
- Running the VGT tests in no graphics mode:
    ```console
    tox -f docker-exec-ubuntu_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkXNoGfx --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the VGT tests with graphics:
    ```console
    tox -f docker-exec-ubuntu_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```console
- Running the STK Vehicle tests in no graphics mode excluding (*deselecting* in pytest terminology) one test:
    ```
    tox -f docker-exec-ubuntu_container-py310 -- pytest pystk/tests/generated/stk_tests/vehicle --target StkXNoGfx --deselect=vehicle/satellite/astrogator/astrogator.py::EarlyBoundTests::test_CompBrowsCutCopyPaste --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv 
    ```
- Running the STK tests with graphics:
    ```console
    tox -f docker-exec-ubuntu_container-py310 -- pytest pystk/tests/generated/stk_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```
### Windows
- Starting a interactive shell inside the container:
    ```console
    tox -f docker-exec-windows_container-py310 -- cmd
    ```
- Running the Aviator tests in no graphics mode inside the container:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkXNoGfx --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the Aviator tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/aviator_tests --target StkX --exclude PluginTests -vv
    ```
- Running the VGT tests in no graphics mode:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkXNoGfx --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the VGT tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/vgt_tests --target StkX --exclude PluginTests -vv
    ```
- Running the STK Vehicle tests in no graphics mode excluding (*deselecting* in pytest terminology) one test:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/stk_tests/vehicle --target StkXNoGfx --deselect=vehicle/satellite/astrogator/astrogator.py::EarlyBoundTests::test_CompBrowsCutCopyPaste --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv 
    ```
- Running the STK tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py310 -- pytest pystk/tests/generated/stk_tests --target StkX --exclude PluginTests -vv
    ```

## Launching Jupyter Lab with Tox

After building the images and running a container, you can also start Jupyter Lab inside the container using:

```console
tox -f docker-lab-{centos,ubuntu,windows}_container-{py38,py39,py310}
```

In the previous command, you need to select the Python version you want to
use, for instance `tox -f docker-lab-centos_container-py310` will start a CentOS container configured with Python 3.10.

Once Jupyter Lab is running, use your browser to navigate to http://127.0.0.1:8888/lab?token=pystk.

## Troubleshooting an STK container in UI mode with Tox 

After building the images and running a container, you can also start a desktop manager inside the container. This provides access to the X graphical user interface. This is particularly useful to troubleshoot any issue arising inside the container. A use case is debugging the graphics tests, as STK's 2D and 3D graphics are rendered inside the container using `xvfb` which is not visible by default.

To start the container in User Interface mode, run the following command:

```console
tox -f docker-novnc-{centos,ubuntu}_container-{py38,py39,py310}
```

Once the container is ready, use your browser to navigate to http://127.0.0.1:8888/vnc_auto.html. This will give you access to a simple X11 desktop based on [fluxbox](http://fluxbox.org/), a lightweight windows manager. The user interface is served to your browser using VNC and [novnc](https://novnc.com/info.html). An xterm is also opened on the desktop, with the virtual environment required to run the Python tests activated.

In addition to running the UI, this configuration also enables `sudo` for the stk user (password identical as user name), so you can install any additional debugging tools required (for instance `gdb` or `valgrind`).

## Stopping an STK container with Tox

You can stop a running container using:

```console
tox -f docker-stop-{centos,ubuntu,windows}_container-{py38,py39,py310}
```

## Removing an STK container with Tox

You can remove a container using:

```console
tox -f docker-rm-{centos,ubuntu,windows}_container-{py38,py39,py310}
```

## Contributing examples

### General guidelines

- Start the example with an explanation of the main topic. For example, if you are discussing a certain orbital maneuver, explain what that maneuver entails. Similarly, if an example is centered around satellite coverage, provide an explanation of what coverage is. Try to use as many keywords as possible in this section.
- The second section of the example should be a problem statement. This statement should include all of the parameters needed in the example, as well as a description of what the example aims to determine. Write this section in an imperative form.
- Include an explanation with each code cell. In a Jupyter notebook, this entails adding a markdown cell before each code cell.
- The examples are built with the documentation and included in the help. As part of the build process, screenshots of the STK Engine 2D and 3D graphics are inserted in the document. You do not need to include the screenshots yourself. However, do include the graphics widgets (2D or 3D) at points in your example. When the documentation is built, a screenshot of the widget will be inserted in its place.
    - These widgets are included in `ansys.stk.core.stkengine.experimental.jupyterwidgets`
    - To include a 2D widget run:

        `from ansys.stk.core.stkengine.experimental.jupyterwidgets import MapWidget`

        `map_plotter = MapWidget(root, 640, 480)`

        `map_plotter.show()`

    - To include a 3D widget run:

        `from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget`

        ` globe_plotter = GlobeWidget(root, 640, 480)`

        `globe_plotter.show()`

    - At any point where a screenshot should appear, show the plotter.
- As part of the documentation build process, screenshots of any graphs that are included will also be inserted. At any point where a screenshot of a graph should appear, show the graph using `matplotlib` or another Python plotting library.

### Set-up

#### Create a branch
To start contributing, create a branch off of the PySTK repository. The branch name must follow [PyAnsys conventions](https://dev.docs.pyansys.com/how-to/contributing.html#branch-naming).

#### Edit examples.rst

When adding an example, add the file name to `doc/source/examples.rst`. This file defines how the examples section of the documentation is built. Each `.. nbgallery::` section corresponds to a thumbnail gallery. Add the path to your example (e.g. `examples/hohmann-transfer`) under the gallery that corresponds to your example type. For example, add examples depicting orbital maneuvers under the `Orbital maneuvers` thumbnail gallery. If your example does not correspond to any of the existing galleries, add a new heading (with `=================` under the text), caption, and gallery.

#### Edit pyproject.toml

If your example requires any dependencies that are not already present in the `doc` section of `pyproject.toml`, add a line in this section with the dependency. Use the version of the dependency on your machine, as dependency bot will update it automatically.

### Style conventions
- Follow the [PyAnsys guidelines](https://dev.docs.pyansys.com/doc-style/index.html#documentation-style):
    - Write headings in sentence case.
    - Use present tense.
- Avoid first-person pronoun usage, and minimize use of second-person pronouns. Instead, use the imperative voice.
- Use LaTeX format for things such as latitude and longitude coordinates, angles, and orbital parameters.
- Insert 2 blank lines between import statements and the first instruction after.
- Use inline highlights for paths to objects and the names of interfaces, classes, methods, properties, and enumerations. 

## Additional documentation

For additional documentation refer to the
[PyAnsys Developer's Guide](https://dev.docs.pyansys.com/index.html).