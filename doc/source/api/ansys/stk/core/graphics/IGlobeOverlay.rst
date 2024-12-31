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
              - Gets the central body that the globe overlay is displayed on. It will return <see langword='null' /> if the globe overlay hasn't been added to a central body.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.extent`
              - Gets the cartographic extent that represents the area covered by the globe overlay. The array elements are arranged in the order west longitude, south latitude, east longitude, north latitude.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.role`
              - Gets the globe overlay role of the globe overlay.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.uri_as_string`
              - Gets the absolute URI specifying the location of the globe overlay.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.is_valid`
              - Gets whether or not the overlay is valid. It can be invalid because of a missing file, corrupt file, unlicensed file, or a file on the incorrect central body.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeOverlay.display_condition`
              - Gets or sets the display condition that controls whether or not the globe overlay is displayed.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGlobeOverlay


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.central_body
    :type: str

    Gets the central body that the globe overlay is displayed on. It will return <see langword='null' /> if the globe overlay hasn't been added to a central body.

.. py:property:: extent
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.extent
    :type: list

    Gets the cartographic extent that represents the area covered by the globe overlay. The array elements are arranged in the order west longitude, south latitude, east longitude, north latitude.

.. py:property:: role
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.role
    :type: OverlayRole

    Gets the globe overlay role of the globe overlay.

.. py:property:: uri_as_string
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.uri_as_string
    :type: str

    Gets the absolute URI specifying the location of the globe overlay.

.. py:property:: is_valid
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.is_valid
    :type: bool

    Gets whether or not the overlay is valid. It can be invalid because of a missing file, corrupt file, unlicensed file, or a file on the incorrect central body.

.. py:property:: display_condition
    :canonical: ansys.stk.core.graphics.IGlobeOverlay.display_condition
    :type: IDisplayCondition

    Gets or sets the display condition that controls whether or not the globe overlay is displayed.


