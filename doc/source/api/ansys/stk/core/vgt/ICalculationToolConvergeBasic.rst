ICalculationToolConvergeBasic
=============================

.. py:class:: ansys.stk.core.vgt.ICalculationToolConvergeBasic

   object
   
   Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

.. py:currentmodule:: ICalculationToolConvergeBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConvergeBasic.sense`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConvergeBasic.time_tolerance`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConvergeBasic.absolute_tolerance`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConvergeBasic.relative_tolerance`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConvergeBasic


Property detail
---------------

.. py:property:: sense
    :canonical: ansys.stk.core.vgt.ICalculationToolConvergeBasic.sense
    :type: CRDN_THRESH_CONVERGE_SENSE

    Get the convergence sense which determines whether the converged value should be limited to just within or just outside of condition boundaries.

.. py:property:: time_tolerance
    :canonical: ansys.stk.core.vgt.ICalculationToolConvergeBasic.time_tolerance
    :type: float

    Get the time tolerance which determines the time accuracy of the converged value.

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.vgt.ICalculationToolConvergeBasic.absolute_tolerance
    :type: float

    Get the absolute tolerance which determines the distance between the value and the boundaries within which the value is considered converged.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.vgt.ICalculationToolConvergeBasic.relative_tolerance
    :type: float

    Get the relative tolerance which determines the relative distance between the value and the boundaries within which the value is considered converged.


