Install PySTK locally in Windows
################################

This guideline covers the local installation of PySTK in Windows platforms.

.. note::

    This guide assumes that you have a local installation of STK and a valid
    license in your machine.

Download artifacts
==================

Start by downloading PySTK wheel or source artifacts for Windows:

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

Install Windows artifacts by using the `pip`_ command:

.. jinja:: artifacts

    .. tab-set::
        :sync-group: artifacts

        .. tab-item:: **Wheels install**
            :sync: wheels

            .. code-block:: text
            
                python -m pip install {{ wheels }}

        .. tab-item:: **Source install**
            :sync: source

            .. code-block:: text
            
                python -m pip install {{ source }}

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
