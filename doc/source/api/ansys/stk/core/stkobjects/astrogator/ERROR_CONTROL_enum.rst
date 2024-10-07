ERROR_CONTROL
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ERROR_CONTROL

   IntEnum


.. py:currentmodule:: ERROR_CONTROL

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ABSOLUTE`
              - The error estimate of each integrated component is compared to the absolute error tolerance. Error control with this method is based on absolute values, e.g. in meters for position, m/sec for velocity, etc.

            * - :py:attr:`~RELATIVE_BY_COMPONENT`
              - The error estimate of each element being integrated relative to the element's value at the start of the step is compared to the relative error tolerance, and the absolute error estimate of each element is compared to the absolute error tolerance.

            * - :py:attr:`~RELATIVE_TO_STATE`
              - Relative to State error control.

            * - :py:attr:`~RELATIVE_TO_STEP`
              - Error estimate of each integrated component relative to the element's change in value over the step is compared to the relative error tolerance, and the absolute error estimate of each integrated component is compared to the absolute error tolerance.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ERROR_CONTROL


