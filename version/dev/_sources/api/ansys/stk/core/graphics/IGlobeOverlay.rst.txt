IGlobeOverlay
=============

.. py:class:: ansys.stk.core.graphics.IGlobeOverlay

   The base class of all terrain overlay and globe image overlay objects.

.. py:currentmodule:: IGlobeOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.central_body`
              - Get the central body that the globe overlay is displayed on. It will return <see langword='null' /> if the globe overlay hasn't been added to a central body.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.display_condition`
              - Get or set the display condition that controls whether or not the globe overlay is displayed.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.extent`
              - Get the cartographic extent that represents the area covered by the globe overlay. The array elements are arranged in the order west longitude, south latitude, east longitude, north latitude.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.is_valid`
              - Get whether or not the overlay is valid. It can be invalid because of a missing file, corrupt file, unlicensed file, or a file on the incorrect central body.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.role`
              - Get the globe overlay role of the globe overlay.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.uri_as_string`
              - Get the absolute URI specifying the location of the globe overlay.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGlobeOverlay


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.central_body
    :type: str

    Get the central body that the globe overlay is displayed on. It will return <see langword='null' /> if the globe overlay hasn't been added to a central body.

.. py:property:: display_condition
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.display_condition
    :type: IDisplayCondition

    Get or set the display condition that controls whether or not the globe overlay is displayed.

.. py:property:: extent
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.extent
    :type: list

    Get the cartographic extent that represents the area covered by the globe overlay. The array elements are arranged in the order west longitude, south latitude, east longitude, north latitude.

.. py:property:: is_valid
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.is_valid
    :type: bool

    Get whether or not the overlay is valid. It can be invalid because of a missing file, corrupt file, unlicensed file, or a file on the incorrect central body.

.. py:property:: role
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.role
    :type: OverlayRole

    Get the globe overlay role of the globe overlay.

.. py:property:: uri_as_string
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.uri_as_string
    :type: str

    Get the absolute URI specifying the location of the globe overlay.


