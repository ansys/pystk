FigureOfMeritGridInspector
==========================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritGridInspector

   Bases: 

   AgFmGridInspector class provides methods to use the grid inspector tool for FOM.

.. py:currentmodule:: FigureOfMeritGridInspector

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector.select_point`
              - Select point.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector.clear_selection`
              - Clear the selected point or region.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector.select_region`
              - Select a region.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector.region_figure_of_merit`
              - Retrieves the Region FOM data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector.region_satisfaction`
              - Retrieves the Region Satisfaction data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector.point_figure_of_merit`
              - Retrieves the Point FOM data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector.point_satisfaction`
              - Retrieves the Point Satisfaction data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector.message`
              - Retrieves the message when a point or region is selected.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritGridInspector


Property detail
---------------

.. py:property:: region_figure_of_merit
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGridInspector.region_figure_of_merit
    :type: IDataProviderInfo

    Retrieves the Region FOM data provider.

.. py:property:: region_satisfaction
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGridInspector.region_satisfaction
    :type: IDataProviderInfo

    Retrieves the Region Satisfaction data provider.

.. py:property:: point_figure_of_merit
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGridInspector.point_figure_of_merit
    :type: IDataProviderInfo

    Retrieves the Point FOM data provider.

.. py:property:: point_satisfaction
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGridInspector.point_satisfaction
    :type: IDataProviderInfo

    Retrieves the Point Satisfaction data provider.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGridInspector.message
    :type: str

    Retrieves the message when a point or region is selected.


Method detail
-------------

.. py:method:: select_point(self, lat: typing.Any, lon: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGridInspector.select_point

    Select point.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: clear_selection(self) -> None
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGridInspector.clear_selection

    Clear the selected point or region.

    :Returns:

        :obj:`~None`

.. py:method:: select_region(self, regionName: str) -> None
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGridInspector.select_region

    Select a region.

    :Parameters:

    **regionName** : :obj:`~str`

    :Returns:

        :obj:`~None`






