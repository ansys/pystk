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
              - Get the option for enabling evenly spaced layer heights.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.maximum_altitude`
              - Get the maximum altitude of the atmosphere.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.atmosphere_layers`
              - Get the atmosphere layer collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LaserAtmosphericLossModelBeerBouguerLambertLaw


Property detail
---------------

.. py:property:: enable_evenly_spaced_heights
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.enable_evenly_spaced_heights
    :type: bool

    Get the option for enabling evenly spaced layer heights.

.. py:property:: maximum_altitude
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.maximum_altitude
    :type: float

    Get the maximum altitude of the atmosphere.

.. py:property:: atmosphere_layers
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.atmosphere_layers
    :type: BeerBouguerLambertLawLayerCollection

    Get the atmosphere layer collection.


Method detail
-------------



.. py:method:: create_evenly_spaced_layers(self, layer_count: int, max_altitude: float) -> BeerBouguerLambertLawLayerCollection
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.create_evenly_spaced_layers

    Clear any existing layers in the collection and creates evenly spaced layers from surface of the central body to the maximum altitude.

    :Parameters:

    **layer_count** : :obj:`~int`
    **max_altitude** : :obj:`~float`

    :Returns:

        :obj:`~BeerBouguerLambertLawLayerCollection`

.. py:method:: create_unevenly_spaced_layers(self, pp_layer_heights: list) -> BeerBouguerLambertLawLayerCollection
    :canonical: ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw.create_unevenly_spaced_layers

    Clear any existing layers in the collection and creates unevenly spaced layers using the array of supplied layer top heights.

    :Parameters:

    **pp_layer_heights** : :obj:`~list`

    :Returns:

        :obj:`~BeerBouguerLambertLawLayerCollection`


