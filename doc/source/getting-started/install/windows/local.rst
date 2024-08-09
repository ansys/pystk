Install PySTK locally in Windows
################################

PySTK can be installed in Windows by following these steps:


Download Windows artifacts
==========================

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
                  - `{{ wheels }} <_static/artifacts/{{ wheels }}>`_
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
                  - `{{ source }} <_static/artifacts/{{ source }}>`_
                * - **Size**
                  - {{ source_size }}
                * - **SHA-256**
                  - {{ source_hash }}

Install Windows artifacts
=========================

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

Verify Windows installation
===========================

Verify a successful installation of PySTK by running:

.. code-block:: python
    
    from ansys.stk.core.stkengine import STKEngine
    

    stk = STKEngine()
    print(f"STK version is {stk.version}")
