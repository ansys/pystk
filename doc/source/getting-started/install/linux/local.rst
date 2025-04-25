Install PySTK locally in Linux
##############################

This topic provides details on installing PySTK locally in Linux platforms.

.. note::

    This topic assumes that you have a local installation of STK and a valid
    license in your machine.

Download artifacts
==================

Start by downloading PySTK wheel or source artifacts for Linux:

.. jinja:: artifacts

    .. tab-set::
        :sync-group: artifacts

        .. tab-item:: **Wheels download**
            :sync: wheels

            Wheel artifacts are the preferred option for installing PySTK:

            .. list-table::
                :widths: auto

                * - **Artifact**
                  - `{{ wheels }} <../../../_static/artifacts/{{ wheels }}>`_
                * - **Size**
                  - {{ wheels_size }}
                * - **SHA-256**
                  - {{ wheels_hash }}

        .. tab-item:: **Source download**
            :sync: source

            Source distribution for installing PySTK:

            .. list-table::
                :widths: auto
        
                * - **Artifact**
                  - `{{ source }} <../../../_static/artifacts/{{ source }}>`_
                * - **Size**
                  - {{ source_size }}
                * - **SHA-256**
                  - {{ source_hash }}

Install artifacts
=================

Install Linux artifacts by using the `pip`_ command:

.. jinja:: artifacts

    .. tab-set::
        :sync-group: artifacts

        .. tab-item:: **PyPI install**
            :sync: pypi

            .. code-block:: text
            
                python -m pip install "ansys-stk-core=={{ PYSTK_VERSION }}"

        .. tab-item:: **Wheels install**
            :sync: wheels

            .. code-block:: text
            
                python -m pip install {{ wheels }}

        .. tab-item:: **Source install**
            :sync: source

            .. code-block:: text
            
                python -m pip install {{ source }}

Install extra artifacts
=======================

PySTK includes some additional features such as gRPC connection support or
Jupyter widgets for visualization. These features require some extra artifacts
to be installed, either pulling those dependencies from the public PyPi
registry or from the wheelhouses included on the :ref:`artifacts <Artifacts>`
page. A wheelhouse provides all of the required dependencies. It facilitates
deploying PySTK on isolated networks that do not have access to the public PyPi
registry.

Start by selecting the additional feature group to install with PySTK. Finally,
select the type of installation.

.. jinja:: optional_dependencies

    .. tab-set::

        {% for target, dependencies in optional_dependencies.items() %}

        .. tab-item:: {{ target }}

            .. tab-set::
                
                .. tab-item:: PyPI install

                    Install the extra dependencies by running:
                    
                    .. code-block:: bash

                        python -m pip install ansys-stk-core[{{ target }}]

                .. tab-item:: Wheelhouse install

                    Download the wheelhouse for :ref:`all extra artifacts <all
                    extra artifacts>`. Then, decompress it by running:

                    .. code-block:: bash
                       
                        unzip <wheelhouse.zip> -d wheelhouse

                    Finally, install the extra dependencies by running:

                    .. code-block:: bash

                        python -m pip install --find-links wheelhouse ansys-stk-core[{{ target }}]

            Dependencies included with the ``{{ target }}`` target are:

            .. raw:: html

                <!-- Initialize DataTables -->
                <script>
                    $(document).ready(function() {
                        $('#target-{{ target }}').DataTable();
                    });
                </script>

                <!-- Populate and render the table -->
                <table id="target-{{ target }}" class="display" style="width:100%">
                    <thead>
                        <tr>
                            <th>PyAnsys project</th>
                            <th>Version</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for project, version in dependencies.items() %}
                        <tr>
                            <td>{{ project }}</td>
                            <td><a href="https://pypi.org/project/{{ project }}/{{ version }}">{{ version }}</a></td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>

         {% endfor %}

Verify installation
===================

Verify a successful installation of PySTK by running:

.. jinja::

    .. code-block:: python
        
        from ansys.stk.core.stkengine import STKEngine
        
    
        stk = STKEngine.start_application(no_graphics=True)
        print(f"STK version is {stk.version}")

    Output:

    .. code-block:: text

        STK version is {{ STK_VERSION }}

        
