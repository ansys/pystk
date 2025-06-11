SpatialAnalysisToolConditionCombined
====================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A combined volume interface.

.. py:currentmodule:: SpatialAnalysisToolConditionCombined

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.get_all_conditions`
              - Get all spatial conditions.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.set_all_conditions`
              - Set all spatial conditions.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.set_condition`
              - Set spatial conditions at a position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.get_condition`
              - Get spatial conditions at a position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.remove_condition`
              - Remove spatial conditions at a position.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.boolean_operation`
              - Get or set volume combined operation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.count`
              - Return the spatial condition vector size.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolConditionCombined


Property detail
---------------

.. py:property:: boolean_operation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.boolean_operation
    :type: VolumeCombinedOperationType

    Get or set volume combined operation.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.count
    :type: int

    Return the spatial condition vector size.


Method detail
-------------




.. py:method:: get_all_conditions(self) -> list
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.get_all_conditions

    Get all spatial conditions.

    :Returns:

        :obj:`~list`

.. py:method:: set_all_conditions(self, conditions: list) -> None
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.set_all_conditions

    Set all spatial conditions.

    :Parameters:

        **conditions** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: set_condition(self, ref: ISpatialAnalysisToolVolume, pos: int) -> None
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.set_condition

    Set spatial conditions at a position.

    :Parameters:

        **ref** : :obj:`~ISpatialAnalysisToolVolume`

        **pos** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: get_condition(self, pos: int) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.get_condition

    Get spatial conditions at a position.

    :Parameters:

        **pos** : :obj:`~int`


    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: remove_condition(self, pos: int) -> None
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionCombined.remove_condition

    Remove spatial conditions at a position.

    :Parameters:

        **pos** : :obj:`~int`


    :Returns:

        :obj:`~None`

