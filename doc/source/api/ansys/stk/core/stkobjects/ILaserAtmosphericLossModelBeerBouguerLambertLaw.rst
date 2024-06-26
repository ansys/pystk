ILaserAtmosphericLossModelBeerBouguerLambertLaw
===============================================

.. py:class:: ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw

   object
   
   Provide access to the properties and methods a Beer-Bouguer-Lambert law laser propagation loss model.

.. py:currentmodule:: ILaserAtmosphericLossModelBeerBouguerLambertLaw

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.create_evenly_spaced_layers`
              - Clear any existing layers in the collection and creates evenly spaced layers from surface of the central body to the maximum altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.create_unevenly_spaced_layers`
              - Clear any existing layers in the collection and creates unevenly spaced layers using the array of supplied layer top heights.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.enable_evenly_spaced_heights`
              - Gets the option for enabling evenly spaced layer heights.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.maximum_altitude`
              - Gets the maximum altitude of the atmosphere.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.atmosphere_layers`
              - Gets the atmosphere layer collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILaserAtmosphericLossModelBeerBouguerLambertLaw


Property detail
---------------

.. py:property:: enable_evenly_spaced_heights
    :canonical: ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.enable_evenly_spaced_heights
    :type: bool

    Gets the option for enabling evenly spaced layer heights.

.. py:property:: maximum_altitude
    :canonical: ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.maximum_altitude
    :type: float

    Gets the maximum altitude of the atmosphere.

.. py:property:: atmosphere_layers
    :canonical: ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.atmosphere_layers
    :type: IBeerBouguerLambertLawLayerCollection

    Gets the atmosphere layer collection.


Method detail
-------------



.. py:method:: create_evenly_spaced_layers(self, layerCount: int, maxAltitude: float) -> IBeerBouguerLambertLawLayerCollection
    :canonical: ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.create_evenly_spaced_layers

    Clear any existing layers in the collection and creates evenly spaced layers from surface of the central body to the maximum altitude.

    :Parameters:

    **layerCount** : :obj:`~int`
    **maxAltitude** : :obj:`~float`

    :Returns:

        :obj:`~IBeerBouguerLambertLawLayerCollection`

.. py:method:: create_unevenly_spaced_layers(self, ppLayerHeights: list) -> IBeerBouguerLambertLawLayerCollection
    :canonical: ansys.stk.core.stkobjects.ILaserAtmosphericLossModelBeerBouguerLambertLaw.create_unevenly_spaced_layers

    Clear any existing layers in the collection and creates unevenly spaced layers using the array of supplied layer top heights.

    :Parameters:

    **ppLayerHeights** : :obj:`~list`

    :Returns:

        :obj:`~IBeerBouguerLambertLawLayerCollection`


