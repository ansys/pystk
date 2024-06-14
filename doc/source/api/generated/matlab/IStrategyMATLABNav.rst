IStrategyMATLABNav
==================

.. py:class:: IStrategyMATLABNav

   object
   
   Interface used to access options for a MATLAB - Horizontal Plane Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator.matlab

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_function_path_valid`
              - Check if the MATLAB function path is valid.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~function_name`
            * - :py:meth:`~check_for_errors`
            * - :py:meth:`~display_output`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator.matlab import IStrategyMATLABNav


Property detail
---------------

.. py:property:: function_name
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLABNav.function_name
    :type: str

    Gets or sets the name of the MATLAB function.

.. py:property:: check_for_errors
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLABNav.check_for_errors
    :type: bool

    Gets or sets the option to check the function for errors.

.. py:property:: display_output
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLABNav.display_output
    :type: bool

    Gets or sets the option to display the output from the MATLAB function.


Method detail
-------------



.. py:method:: is_function_path_valid(self) -> bool

    Check if the MATLAB function path is valid.

    :Returns:

        :obj:`~bool`





