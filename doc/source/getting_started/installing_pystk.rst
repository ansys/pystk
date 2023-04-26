Installing PySTK
################

Installing PySTK is as simple as installing a Python library. However, a runninc
instance of STK is required to use PySTK.

PySTK is just a Python API to STK, meaning that STK is still required to perform
all the necessary computations.

Make sure that you follow the :ref:`Building STK images` guide to containerize
STK. Although PySTK can attach to an 


User installation
=================

There are multiple sources for installing the latest stable version of PySTK.
These include ``pip`` and ``GitHub``.


.. jinja:: install_guide

    .. tab-set::
    
        .. tab-item:: From public PyPI
    
            .. code-block:: console
    
                python -m pip install ansys-stk-core
    

        .. tab-item:: From official GitHub repository
    
            .. code-block:: console

                python -m pip install git+https://github.com/pyansys/pystk.git@v{{ version }}







Developer installation
======================

Developer installation allows to modify the source code of PySTK and see the
changes ins

There are several ways to install PySTK. 
