KmlNetworkLink
==============

.. py:class:: ansys.stk.core.graphics.KmlNetworkLink

   Bases: :py:class:`~ansys.stk.core.graphics.IKmlFeature`

   A KML network link.

.. py:currentmodule:: KmlNetworkLink

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.refresh`
              - Refresh the network link.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.cookie`
              - Get the cookie string associated with this network link.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.expires`
              - Get the string specifying the date/time this network should expire and be refreshed.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.link_snippet`
              - Get the link snippet associated with this network link.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.message`
              - Get the message string associated with this network link.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.minimum_refresh_period`
              - Get the duration that is the minimum allowed time between refreshes of this network link.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.refresh_interval`
              - Get or set the interval duration at which this network link will refresh, when refresh mode is set to on interval.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.refresh_mode`
              - Get or set the refresh mode of the network link. The refresh mode specifies a time-based refresh policy for this link.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.uri`
              - Get the uri of the network link.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.view_bound_scale`
              - Get or set the value that scales the bounding box defining the view associated with this network link. A value less than 1.0 specifies to use less than the full view (screen). A value greater than 1...
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.view_refresh_mode`
              - Get or set the view refresh mode of the network link. The view refresh mode specifies the refresh policy for the when the camera's view changes.
            * - :py:attr:`~ansys.stk.core.graphics.KmlNetworkLink.view_refresh_time`
              - Get or set the duration after camera view movement stops that this network link will refresh, when view refresh mode is set to on stop.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import KmlNetworkLink


Property detail
---------------

.. py:property:: cookie
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.cookie
    :type: str

    Get the cookie string associated with this network link.

.. py:property:: expires
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.expires
    :type: str

    Get the string specifying the date/time this network should expire and be refreshed.

.. py:property:: link_snippet
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.link_snippet
    :type: str

    Get the link snippet associated with this network link.

.. py:property:: message
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.message
    :type: str

    Get the message string associated with this network link.

.. py:property:: minimum_refresh_period
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.minimum_refresh_period
    :type: float

    Get the duration that is the minimum allowed time between refreshes of this network link.

.. py:property:: refresh_interval
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.refresh_interval
    :type: float

    Get or set the interval duration at which this network link will refresh, when refresh mode is set to on interval.

.. py:property:: refresh_mode
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.refresh_mode
    :type: KmlNetworkLinkRefreshMode

    Get or set the refresh mode of the network link. The refresh mode specifies a time-based refresh policy for this link.

.. py:property:: uri
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.uri
    :type: str

    Get the uri of the network link.

.. py:property:: view_bound_scale
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.view_bound_scale
    :type: float

    Get or set the value that scales the bounding box defining the view associated with this network link. A value less than 1.0 specifies to use less than the full view (screen). A value greater than 1...

.. py:property:: view_refresh_mode
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.view_refresh_mode
    :type: KmlNetworkLinkViewRefreshMode

    Get or set the view refresh mode of the network link. The view refresh mode specifies the refresh policy for the when the camera's view changes.

.. py:property:: view_refresh_time
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.view_refresh_time
    :type: float

    Get or set the duration after camera view movement stops that this network link will refresh, when view refresh mode is set to on stop.


Method detail
-------------






.. py:method:: refresh(self) -> None
    :canonical: ansys.stk.core.graphics.KmlNetworkLink.refresh

    Refresh the network link.

    :Returns:

        :obj:`~None`












