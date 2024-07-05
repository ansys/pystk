IFigureOfMeritGridInspector
===========================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector

   object
   
   Provide access to the FOM grid inspector properties.

.. py:currentmodule:: IFigureOfMeritGridInspector

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.select_point`
              - Select point.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.clear_selection`
              - Clear the selected point or region.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.select_region`
              - Select a region.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.region_figure_of_merit`
              - Retrieves the Region FOM data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.region_satisfaction`
              - Retrieves the Region Satisfaction data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.point_figure_of_merit`
              - Retrieves the Point FOM data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.point_satisfaction`
              - Retrieves the Point Satisfaction data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.message`
              - Retrieves the message when a point or region is selected.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGridInspector


Property detail
---------------

.. py:property:: region_figure_of_merit
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.region_figure_of_merit
    :type: IDataProviderInfo

    Retrieves the Region FOM data provider.

.. py:property:: region_satisfaction
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.region_satisfaction
    :type: IDataProviderInfo

    Retrieves the Region Satisfaction data provider.

.. py:property:: point_figure_of_merit
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.point_figure_of_merit
    :type: IDataProviderInfo

    Retrieves the Point FOM data provider.

.. py:property:: point_satisfaction
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.point_satisfaction
    :type: IDataProviderInfo

    Retrieves the Point Satisfaction data provider.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.message
    :type: str

    Retrieves the message when a point or region is selected.


Method detail
-------------

.. py:method:: select_point(self, lat: typing.Any, lon: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.select_point

    Select point.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: clear_selection(self) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.clear_selection

    Clear the selected point or region.

    :Returns:

        :obj:`~None`

.. py:method:: select_region(self, regionName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.select_region

    Select a region.

    :Parameters:

    **regionName** : :obj:`~str`

    :Returns:

        :obj:`~None`






