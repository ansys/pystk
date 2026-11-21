# Contributing

#### Table of Contents
* [Using Tox for testing and development](#using-tox-for-testing-and-development)
  + [Installing Tox](#installing-tox)
  + [Listing Tox environments](#listing-tox-environments)
  + [Building the STK container images with Tox](#building-the-stk-container-images-with-tox)
  + [Running an STK container with Tox](#running-an-stk-container-with-tox)
  + [Executing a command inside an STK container with Tox](#executing-a-command-inside-an-stk-container-with-tox)
      - [Ubuntu](#ubuntu)
      - [Windows](#windows)
  + [Launching Jupyter Lab with Tox](#launching-jupyter-lab-with-tox)
  + [Troubleshooting an STK container in UI mode with Tox](#troubleshooting-an-stk-container-in-ui-mode-with-tox)
  + [Stopping an STK container with Tox](#stopping-an-stk-container-with-tox)
  + [Removing an STK container with Tox](#removing-an-stk-container-with-tox)
* [Contributing examples](#contributing-examples)
  + [General guidelines](#general-guidelines)
  + [Set-up](#set-up)
      - [Create a branch](#create-a-branch)
      - [Edit examples.rst](#edit-examplesrst)
      - [Edit pyproject.toml](#edit-pyprojecttoml)
  + [Style conventions](#style-conventions)
  + [Code-style check](#code-style-check)
* [Additional documentation](#additional-documentation)

## Using Tox for testing and development

[Tox](https://tox.wiki) is a powerful tool that simplifies and automates the
process of testing and developing your project across multiple environments. It
allows you to define test environments, run tests, and perform various
development tasks in a consistent and reproducible manner. Tox is particularly
useful for ensuring that your project works seamlessly on different Python
versions, interpreters, and platforms.

### Installing Tox

To install Tox with uv and enable uv-backed environments, use:

```console
uv tool install tox --with tox-uv
```

You can verify the installation by running:

```console
tox --version
```

To generate or refresh the project lock file for development, run:

```console
uv lock
```

### Listing Tox environments

The configuration for Tox is stored in [the tox.ini file](https://github.com/ansys/pystk/blob/main/tox.ini).
This file contains various environments. Environments are a collection of
commands executed depending on the platform and the environment.

To list all Tox environments, you can use the following command:

```console
tox list
```

### Building the STK container images with Tox

Use the following commands to build the images for your target distribution:

- **Ubuntu**

    ```console
    tox -e docker-build-ubuntu_images
    ```
    This will result in the following images:

    ```bash
    ~$ docker images

    IMAGE                                       ID             DISK USAGE   CONTENT SIZE
    ansys/stk-13.1:dev-ubuntu22.04              0dabdfe303b3       8.06GB         3.04GB
    ansys/stk-13.1:dev-ubuntu22.04-pybase       c93dab83a65c       9.21GB         3.36GB
    ansys/stk-13.1:dev-ubuntu22.04-python3.11   b7d2e0eb90eb       8.94GB         3.24GB
    ansys/stk-13.1:dev-ubuntu22.04-python3.12   1b4bac1f7518       8.95GB         3.25GB
    ansys/stk-13.1:dev-ubuntu22.04-python3.13   54f55efae5a3       8.99GB         3.26GB
    ansys/stk-13.1:dev-ubuntu22.04-python3.14   7c1d8e7276c5       9.03GB         3.27GB
    ```

- **Windows**

    ```console
    tox -e docker-build-windows_images -- agreeToLicense=yes
    ```
    This will result in the following images:

    ```bash
    ~$ docker images

    IMAGE                                                                   ID             DISK USAGE   CONTENT SIZE   EXTRA
    ansys/stk-13.1:dev-windowsservercore-ltsc2019                           fba63d5cce9e       17.3GB             0B
    ansys/stk-13.1:dev-windowsservercore-ltsc2019-pybase                    5c66b083ba7f       17.3GB             0B
    ansys/stk-13.1:dev-windowsservercore-ltsc2019-python3.11                3ad836c75b7e       17.6GB             0B
    ansys/stk-13.1:dev-windowsservercore-ltsc2019-python3.12                588c444c0f30       17.6GB             0B
    ansys/stk-13.1:dev-windowsservercore-ltsc2019-python3.13                74fdf92ed167       17.6GB             0B
    ansys/stk-13.1:dev-windowsservercore-ltsc2019-python3.14                164e4c09f2c8       17.6GB             0B
    mcr.microsoft.com/dotnet/framework/runtime:4.8-windowsservercore-ltsc2019
                                                                            8fbece662844       7.89GB             0B
    ```


### Running an STK container with Tox

Once the images are built, you can create a new container targeting a specific Python version using the following command:

> [!NOTE]
>Make sure that the ANSYSLMD_LICENSE_FILE environment variable is properly configured before starting the container.

```console
tox -f docker-run-{ubuntu,windows}_container-{py311,py312,py313}
```

This will start a new virtual environment inside the container and install all the dependencies required to run the tests and generate the project documentation. This will also install Jupyter Lab and its dependencies in that virtual environment.

In the previous command, you need to select the Python version you want to
use, for instance:

- `tox -f docker-run-windows_container-py311` will start a Windows container configured with Python 3.11.
- `tox -f docker-run-ubuntu_container-py312` will start a Ubuntu container configured with Python 3.12.

### Executing a command inside an STK container with Tox

After building the images and running a container, you can execute a command inside the container using:

```console
tox -f docker-exec-py3{11,12,13,14}-{ubuntu,windows}_container-{linux,windows}_host -- {command}
```

For instance, to run `ls -la` inside a previously started Ubuntu 22.04 Python 3.14 container, use:

```console
tox -f docker-exec-ubuntu_container-py314 -- ls -la
```

Here are a few additional examples:

#### Ubuntu

- Starting a interactive shell inside the container:
    ```console
    tox -f docker-exec-ubuntu_container-py314 -- /bin/bash
    ```
- Running the Aviator tests in no graphics mode inside the container:
    ```console
    tox -f docker-exec-ubuntu_container-py314 -- pytest pystk/tests/generated/aviator_tests --target StkXNoGfx --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the Aviator tests with graphics:
    ```console
    tox -f docker-exec-ubuntu_container-py314 -- pytest pystk/tests/generated/aviator_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```
- Running the VGT tests in no graphics mode:
    ```console
    tox -f docker-exec-ubuntu_container-py314 -- pytest pystk/tests/generated/vgt_tests --target StkXNoGfx --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the VGT tests with graphics:
    ```console
    tox -f docker-exec-ubuntu_container-py314 -- pytest pystk/tests/generated/vgt_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```console
- Running the STK Vehicle tests in no graphics mode excluding (*deselecting* in pytest terminology) one test:
    ```
    tox -f docker-exec-ubuntu_container-py314 -- pytest pystk/tests/generated/stk_tests/vehicle --target StkXNoGfx --deselect=vehicle/satellite/astrogator/astrogator.py::EarlyBoundTests::test_CompBrowsCutCopyPaste --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the STK tests with graphics:
    ```console
    tox -f docker-exec-ubuntu_container-py314 -- pytest pystk/tests/generated/stk_tests --target StkX --exclude ExcludeOnLinux --exclude SEET --exclude PluginTests -vv
    ```

#### Windows

- Starting a interactive shell inside the container:
    ```console
    tox -f docker-exec-windows_container-py314 -- cmd
    ```
- Running the Aviator tests in no graphics mode inside the container:
    ```console
    tox -f docker-exec-windows_container-py314 -- pytest src/pystk/tests/generated/aviator_tests --target StkXNoGfx --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the Aviator tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py314 -- pytest src/pystk/tests/generated/aviator_tests --target StkX --exclude PluginTests -vv
    ```
- Running the VGT tests in no graphics mode:
    ```console
    tox -f docker-exec-windows_container-py314 -- pytest src/pystk/tests/generated/vgt_tests --target StkXNoGfx --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the VGT tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py314 -- pytest src/pystk/tests/generated/vgt_tests --target StkX --exclude PluginTests -vv
    ```
- Running the STK Vehicle tests in no graphics mode excluding (*deselecting* in pytest terminology) one test:
    ```console
    tox -f docker-exec-windows_container-py314 -- pytest src/pystk/tests/generated/stk_tests/vehicle --target StkXNoGfx --deselect=vehicle/satellite/astrogator/astrogator.py::EarlyBoundTests::test_CompBrowsCutCopyPaste --exclude PluginTests --exclude "Graphics Tests" --exclude "VO Tests" -vv
    ```
- Running the STK tests with graphics:
    ```console
    tox -f docker-exec-windows_container-py314 -- pytest src/pystk/tests/generated/stk_tests --target StkX --exclude PluginTests -vv
    ```

### Launching Jupyter Lab with Tox

After building the images and running a container, you can also start Jupyter Lab inside the container using:

```console
tox -f docker-lab-py3{11,12,13,14}-{ubuntu,windows}_container-{linux,windows}_host
```

In the previous command, you need to select the Python version you want to
use, for instance `tox -f docker-lab-py314-ubuntu_container-linux_host` will start an Ubuntu container configured with Python 3.14.

Once Jupyter Lab is running, use your browser to navigate to http://127.0.0.1:8888/lab?token=pystk.

### Troubleshooting an STK container in UI mode with Tox

After building the images and running a container, you can also start a desktop manager inside the container. This provides access to the X graphical user interface. This is particularly useful to troubleshoot any issue arising inside the container. A use case is debugging the graphics tests, as STK's 2D and 3D graphics are rendered inside the container using `xvfb` which is not visible by default.

To start the container in User Interface mode, run the following command:

```console
tox -f docker-novnc-{ubuntu}_container-{py311,py312,py313}
```

Once the container is ready, use your browser to navigate to http://127.0.0.1:8888/vnc_auto.html. This will give you access to a simple X11 desktop based on [fluxbox](http://fluxbox.org/), a lightweight windows manager. The user interface is served to your browser using VNC and [novnc](https://novnc.com/info.html). An xterm is also opened on the desktop, with the virtual environment required to run the Python tests activated.

In addition to running the UI, this configuration also enables `sudo` for the stk user (password identical as user name), so you can install any additional debugging tools required (for instance `gdb` or `valgrind`).

### Stopping an STK container with Tox

You can stop a running container using:

```console
tox -f docker-stop-{ubuntu,windows}_container-{py311,py312,py313}
```

### Removing an STK container with Tox

You can remove a container using:

```console
tox -f docker-rm-{ubuntu,windows}_container-{py311,py312,py313}
```

## Contributing examples

### General guidelines

- Start the example with an explanation of the main topic. For example, if you are discussing a certain orbital maneuver, explain what that maneuver entails. Similarly, if an example is centered around satellite coverage, provide an explanation of what coverage is. Try to use as many relevant keywords as possible in this section to optimize for Search Engine Optimization.
- The second section of the example should be a problem statement. This statement should include all of the parameters needed in the example, as well as a description of what the example aims to determine. Write this section in an imperative form.
- Include an explanation with each code cell. In a Jupyter notebook, this entails adding a markdown cell before each code cell. The explanations should be included before, not after, the corresponding code.
- The examples are built with the documentation and included in the help. As part of the build process, screenshots of the STK Engine 2D and 3D graphics are inserted in the document. You do not need to include the screenshots yourself. However, do include the graphics widgets (2D or 3D) at points in your example. When the documentation is built, a screenshot of the widget will be inserted in its place.
    - These widgets are included in `ansys.stk.core.experimental.jupyterwidgets`
    - To include a 2D widget run:

        ```python
        from ansys.stk.core.experimental.jupyterwidgets import MapWidget

        map_plotter = MapWidget(root, 640, 480)

        map_plotter.show()
        ```

    - To include a 3D widget run:

        ```python
        from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget

        globe_plotter = GlobeWidget(root, 640, 480)

        globe_plotter.show()
        ```

    - At any point where a screenshot should appear, show the plotter.
- As part of the documentation build process, screenshots of any graphs that are included will also be inserted. At any point where a screenshot of a graph should appear, show the graph using `matplotlib` or another Python plotting library.
- Designate a fixed time frame for the scenario. This ensures that the scenario will be consistent every time the documentation builds, and will not change per build based on the current date.

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
- Imports should be sorted in 3 groups: standard library, third party, and local packages. Within those groups, use alphabetical order.

### Code-style check

All examples submitted to the PySTK GitHub must pass a code-style check, which enforces rules like maximum line lengths, double quotes for strings, and avoiding trailing spaces. It is possible to run the code-style check locally by running

`tox -e code-style`

This command formats any files committed so that they follow the code-style rules. It is then possible to stage the formatted files and commit them.

## Additional documentation

For additional documentation refer to the
[PyAnsys Developer's Guide](https://dev.docs.pyansys.com/index.html).
