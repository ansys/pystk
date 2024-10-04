SpatialAnalysisToolConditionValidTimeAtLocation
===============================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolConditionValidTimeAtLocation

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   An volume from time satisfaction volume interface.

.. py:currentmodule:: SpatialAnalysisToolConditionValidTimeAtLocation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionValidTimeAtLocation.time_satisfaction`
              - The interval list within which the global minimum or maximum is sought. The default is the overall availability of host object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolConditionValidTimeAtLocation


Property detail
---------------

.. py:property:: time_satisfaction
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionValidTimeAtLocation.time_satisfaction
    :type: ITimeToolTimeIntervalList

    The interval list within which the global minimum or maximum is sought. The default is the overall availability of host object.


