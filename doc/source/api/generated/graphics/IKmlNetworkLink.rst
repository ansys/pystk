IKmlNetworkLink
===============

.. py:class:: IKmlNetworkLink

   object
   
   A KML network link.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~refresh`
              - Refresh the network link.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~uri`
            * - :py:meth:`~refresh_mode`
            * - :py:meth:`~refresh_interval`
            * - :py:meth:`~view_refresh_mode`
            * - :py:meth:`~view_refresh_time`
            * - :py:meth:`~view_bound_scale`
            * - :py:meth:`~minimum_refresh_period`
            * - :py:meth:`~cookie`
            * - :py:meth:`~message`
            * - :py:meth:`~link_snippet`
            * - :py:meth:`~expires`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IKmlNetworkLink


Property detail
---------------

.. py:property:: uri
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.uri
    :type: str

    Gets the uri of the network link.

.. py:property:: refresh_mode
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.refresh_mode
    :type: "KML_NETWORK_LINK_REFRESH_MODE"

    Gets or sets the refresh mode of the network link. The refresh mode specifies a time-based refresh policy for this link.

.. py:property:: refresh_interval
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.refresh_interval
    :type: float

    Gets or sets the interval duration at which this network link will refresh, when refresh mode is set to on interval.

.. py:property:: view_refresh_mode
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.view_refresh_mode
    :type: "KML_NETWORK_LINK_VIEW_REFRESH_MODE"

    Gets or sets the view refresh mode of the network link. The view refresh mode specifies the refresh policy for the when the camera's view changes.

.. py:property:: view_refresh_time
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.view_refresh_time
    :type: float

    Gets or sets the duration after camera view movement stops that this network link will refresh, when view refresh mode is set to on stop.

.. py:property:: view_bound_scale
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.view_bound_scale
    :type: float

    Gets or sets the value that scales the bounding box defining the view associated with this network link. A value less than 1.0 specifies to use less than the full view (screen). A value greater than 1...

.. py:property:: minimum_refresh_period
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.minimum_refresh_period
    :type: float

    Gets the duration that is the minimum allowed time between refreshes of this network link.

.. py:property:: cookie
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.cookie
    :type: str

    Gets the cookie string associated with this network link.

.. py:property:: message
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.message
    :type: str

    Gets the message string associated with this network link.

.. py:property:: link_snippet
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.link_snippet
    :type: str

    Gets the link snippet associated with this network link.

.. py:property:: expires
    :canonical: ansys.stk.core.graphics.IKmlNetworkLink.expires
    :type: str

    Gets the string specifying the date/time this network should expire and be refreshed.


Method detail
-------------

















.. py:method:: refresh(self) -> None

    Refresh the network link.

    :Returns:

        :obj:`~None`

