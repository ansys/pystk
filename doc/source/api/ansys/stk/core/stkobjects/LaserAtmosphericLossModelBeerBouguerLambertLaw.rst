LaserAtmosphericLossModelBeerBouguerLambertLaw
==============================================

.. py:class:: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining an laser propagation loss model.

.. py:currentmodule:: LaserAtmosphericLossModelBeerBouguerLambertLaw

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.create_evenly_spaced_layers`
              - Clear any existing layers in the collection and creates evenly spaced layers from surface of the central body to the maximum altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.create_unevenly_spaced_layers`
              - Clear any existing layers in the collection and creates unevenly spaced layers using the array of supplied layer top heights.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.enable_evenly_spaced_heights`
              - Gets the option for enabling evenly spaced layer heights.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.maximum_altitude`
              - Gets the maximum altitude of the atmosphere.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.atmosphere_layers`
              - Gets the atmosphere layer collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LaserAtmosphericLossModelBeerBouguerLambertLaw


Property detail
---------------

.. py:property:: enable_evenly_spaced_heights
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.enable_evenly_spaced_heights
    :type: bool

    Gets the option for enabling evenly spaced layer heights.

.. py:property:: maximum_altitude
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.maximum_altitude
    :type: float

    Gets the maximum altitude of the atmosphere.

.. py:property:: atmosphere_layers
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.atmosphere_layers
    :type: IBeerBouguerLambertLawLayerCollection

    Gets the atmosphere layer collection.


Method detail
-------------



.. py:method:: create_evenly_spaced_layers(self, layerCount: int, maxAltitude: float) -> BeerBouguerLambertLawLayerCollection
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.create_evenly_spaced_layers

    Clear any existing layers in the collection and creates evenly spaced layers from surface of the central body to the maximum altitude.

    :Parameters:

    **layerCount** : :obj:`~int`
    **maxAltitude** : :obj:`~float`

    :Returns:

        :obj:`~BeerBouguerLambertLawLayerCollection`

.. py:method:: create_unevenly_spaced_layers(self, ppLayerHeights: list) -> BeerBouguerLambertLawLayerCollection
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.create_unevenly_spaced_layers

    Clear any existing layers in the collection and creates unevenly spaced layers using the array of supplied layer top heights.

    :Parameters:

    **ppLayerHeights** : :obj:`~list`

    :Returns:

        :obj:`~BeerBouguerLambertLawLayerCollection`


