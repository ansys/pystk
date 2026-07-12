CesiumIonTerrainOverlayFactory
==============================

.. py:class:: ansys.stk.core.graphics.CesiumIonTerrainOverlayFactory

   A terrain overlay for handling Cesium Ion Streaming Terrain.

.. py:currentmodule:: CesiumIonTerrainOverlayFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CesiumIonTerrainOverlayFactory.initialize_with_asset_uri`
              - Initialize a cesiumion terrain overlay with the provided values necessary to communicate with a Cesium ion endpoint.
            * - :py:attr:`~ansys.stk.core.graphics.CesiumIonTerrainOverlayFactory.initialize_with_string`
              - Initialize a cesiumion terrain overlay with the provided values necessary to communicate with a Cesium ion endpoint.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CesiumIonTerrainOverlayFactory



Method detail
-------------

.. py:method:: initialize_with_asset_uri(self, asset_uri: str, api_endpoint_uri: str, access_token: str) -> CesiumIonTerrainOverlay
    :canonical: ansys.stk.core.graphics.CesiumIonTerrainOverlayFactory.initialize_with_asset_uri

    Initialize a cesiumion terrain overlay with the provided values necessary to communicate with a Cesium ion endpoint.

    :Parameters:

        **asset_uri** : :obj:`~str`

        **api_endpoint_uri** : :obj:`~str`

        **access_token** : :obj:`~str`


    :Returns:

        :obj:`~CesiumIonTerrainOverlay`

.. py:method:: initialize_with_string(self, tileset_name: str, api_endpoint_uri: str, access_token: str) -> CesiumIonTerrainOverlay
    :canonical: ansys.stk.core.graphics.CesiumIonTerrainOverlayFactory.initialize_with_string

    Initialize a cesiumion terrain overlay with the provided values necessary to communicate with a Cesium ion endpoint.

    :Parameters:

        **tileset_name** : :obj:`~str`

        **api_endpoint_uri** : :obj:`~str`

        **access_token** : :obj:`~str`


    :Returns:

        :obj:`~CesiumIonTerrainOverlay`

