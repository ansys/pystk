StrategyMATLABFull3D
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.matlab.IBasicManeuverStrategy`

   Class defining the MATLAB - Full 3D strategy for a basic maneuver procedure.

.. py:currentmodule:: StrategyMATLABFull3D

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D.is_function_path_valid`
              - Check if the MATLAB function path is valid.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D.function_name`
              - Get or set the name of the MATLAB function.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D.check_for_errors`
              - Get or set the option to check the function for errors.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D.display_output`
              - Get or set the option to display the output from the MATLAB function.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator.matlab import StrategyMATLABFull3D


Property detail
---------------

.. py:property:: function_name
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D.function_name
    :type: str

    Get or set the name of the MATLAB function.

.. py:property:: check_for_errors
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D.check_for_errors
    :type: bool

    Get or set the option to check the function for errors.

.. py:property:: display_output
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D.display_output
    :type: bool

    Get or set the option to display the output from the MATLAB function.


Method detail
-------------



.. py:method:: is_function_path_valid(self) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.StrategyMATLABFull3D.is_function_path_valid

    Check if the MATLAB function path is valid.

    :Returns:

        :obj:`~bool`





