SPACE_ENVIRONMENT_MAGNETIC_FIELD_COLOR_SCALE_TYPE
=================================================

.. py:class:: ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_MAGNETIC_FIELD_COLOR_SCALE_TYPE

   IntEnum


.. py:currentmodule:: SPACE_ENVIRONMENT_MAGNETIC_FIELD_COLOR_SCALE_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - An invalid AgESpEnvMagFieldColorScale value.

            * - :py:attr:`~LINEAR`
              - Assign colors based upon a linear scaling from minimum to maximum value.

            * - :py:attr:`~LOG`
              - Assign colors based upon a linear scaling from log10(minimum) to log10(maximum) value. Ignores 0.0 values.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SPACE_ENVIRONMENT_MAGNETIC_FIELD_COLOR_SCALE_TYPE


