ISpatialAnalysisToolVolumeCombined
==================================

.. py:class:: ISpatialAnalysisToolVolumeCombined

   object
   
   A combined volume interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_all_conditions`
              - Get all spatial conditions.
            * - :py:meth:`~set_all_conditions`
              - Set all spatial conditions.
            * - :py:meth:`~set_condition`
              - Set spatial conditions at a position.
            * - :py:meth:`~get_condition`
              - Get spatial conditions at a position.
            * - :py:meth:`~remove_condition`
              - Remove spatial conditions at a position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~combine_operation`
            * - :py:meth:`~condition_count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeCombined


Property detail
---------------

.. py:property:: combine_operation
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCombined.combine_operation
    :type: CRDN_VOLUME_COMBINED_OPERATION_TYPE

    Sets/Returns volume combined operation.

.. py:property:: condition_count
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCombined.condition_count
    :type: int

    Returns the spatial condition vector size.


Method detail
-------------




.. py:method:: get_all_conditions(self) -> list
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCombined.get_all_conditions

    Get all spatial conditions.

    :Returns:

        :obj:`~list`

.. py:method:: set_all_conditions(self, conditions: list) -> None
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCombined.set_all_conditions

    Set all spatial conditions.

    :Parameters:

    **conditions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_condition(self, ref: ISpatialAnalysisToolVolume, pos: int) -> None
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCombined.set_condition

    Set spatial conditions at a position.

    :Parameters:

    **ref** : :obj:`~ISpatialAnalysisToolVolume`
    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: get_condition(self, pos: int) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCombined.get_condition

    Get spatial conditions at a position.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: remove_condition(self, pos: int) -> None
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCombined.remove_condition

    Remove spatial conditions at a position.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

