ISpatialAnalysisToolVolumeFromCalc
==================================

.. py:class:: ISpatialAnalysisToolVolumeFromCalc

   object
   
   An volume from calc volume interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_minimum`
              - Get the minimum bound value from the bounds. Call SetMinimum to apply changes.
            * - :py:meth:`~set_minimum`
              - Set the minimum bound value for the bounds.
            * - :py:meth:`~get_maximum`
              - Get the maximum bound value from the bounds. Call SetMaximum to apply changes.
            * - :py:meth:`~set_maximum`
              - Set the maximum bound value for the condition.
            * - :py:meth:`~set`
              - Set the min/max bounds. Throws an exception if the minimum is greater than maximum.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~operation`
            * - :py:meth:`~volume_calc`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeFromCalc


Property detail
---------------

.. py:property:: operation
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCalc.operation
    :type: CRDN_CONDITION_THRESHOLD_OPTION

    Get the operation from the condition that determines how the bounds are considered. The operation can be set to define satisfaction when the scalar is above minimum, below maximum, between minimum and maximum or outside minimum and maximum.

.. py:property:: volume_calc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCalc.volume_calc
    :type: IAgCrdnVolumeCalc

    Get the volume calc from the bounds.


Method detail
-------------





.. py:method:: get_minimum(self) -> IQuantity
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCalc.get_minimum

    Get the minimum bound value from the bounds. Call SetMinimum to apply changes.

    :Returns:

        :obj:`~IQuantity`

.. py:method:: set_minimum(self, value: IQuantity) -> None
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCalc.set_minimum

    Set the minimum bound value for the bounds.

    :Parameters:

    **value** : :obj:`~IQuantity`

    :Returns:

        :obj:`~None`

.. py:method:: get_maximum(self) -> IQuantity
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCalc.get_maximum

    Get the maximum bound value from the bounds. Call SetMaximum to apply changes.

    :Returns:

        :obj:`~IQuantity`

.. py:method:: set_maximum(self, value: IQuantity) -> None
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCalc.set_maximum

    Set the maximum bound value for the condition.

    :Parameters:

    **value** : :obj:`~IQuantity`

    :Returns:

        :obj:`~None`

.. py:method:: set(self, min: IQuantity, max: IQuantity) -> None
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCalc.set

    Set the min/max bounds. Throws an exception if the minimum is greater than maximum.

    :Parameters:

    **min** : :obj:`~IQuantity`
    **max** : :obj:`~IQuantity`

    :Returns:

        :obj:`~None`

