Install PySTK locally in Windows
################################

PySTK can be installed in Windows by following these steps:


Download Windows artifacts
==========================

Start by downloading PySTK wheel or source artifacts for Windows:

.. jinja:: artifacts

    .. list-table::
        :header-rows: 1
        :widths: auto

        * - Wheels (recommended)
          - Source
        * - `{{ wheels }} <_static/artifacts/{{ wheels }}>`_
          - `{{ source }} <_static/artifacts/{{ source }}>`_

Install Windows artifacts
=========================

Install the Windows artifacts by using the `pip`_ command:

.. jinja:: artifacts

    **Wheels (recommended)**

    .. code-block:: text
    
        python -m pip install {{ wheels }}

    **Source**

    .. code-block:: text
    
        python -m pip install {{ source }}


Verify Windows installation
===========================

To verify a successful installation of PySTK, run the following code:

.. code-block:: python
    
    from ansys.stk.core.stkengine import STKEngine
    

    stk = STKEngine()
    print(f"STK version is {stk.version}")
