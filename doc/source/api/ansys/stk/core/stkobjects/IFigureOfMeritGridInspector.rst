IFigureOfMeritGridInspector
===========================

.. py:class:: IFigureOfMeritGridInspector

   object
   
   Provide access to the FOM grid inspector properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~select_point`
              - Select point.
            * - :py:meth:`~clear_selection`
              - Clear the selected point or region.
            * - :py:meth:`~select_region`
              - Select a region.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~region_figure_of_merit`
            * - :py:meth:`~region_satisfaction`
            * - :py:meth:`~point_figure_of_merit`
            * - :py:meth:`~point_satisfaction`
            * - :py:meth:`~message`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGridInspector


Property detail
---------------

.. py:property:: region_figure_of_merit
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.region_figure_of_merit
    :type: "IAgDataProviderInfo"

    Retrieves the Region FOM data provider.

.. py:property:: region_satisfaction
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.region_satisfaction
    :type: "IAgDataProviderInfo"

    Retrieves the Region Satisfaction data provider.

.. py:property:: point_figure_of_merit
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.point_figure_of_merit
    :type: "IAgDataProviderInfo"

    Retrieves the Point FOM data provider.

.. py:property:: point_satisfaction
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.point_satisfaction
    :type: "IAgDataProviderInfo"

    Retrieves the Point Satisfaction data provider.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGridInspector.message
    :type: str

    Retrieves the message when a point or region is selected.


Method detail
-------------

.. py:method:: select_point(self, lat:typing.Any, lon:typing.Any) -> None

    Select point.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: clear_selection(self) -> None

    Clear the selected point or region.

    :Returns:

        :obj:`~None`

.. py:method:: select_region(self, regionName:str) -> None

    Select a region.

    :Parameters:

    **regionName** : :obj:`~str`

    :Returns:

        :obj:`~None`






