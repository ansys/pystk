KmlNetworkLinkViewRefreshMode
=============================

.. py:class:: ansys.stk.core.graphics.KmlNetworkLinkViewRefreshMode

   IntEnum


.. py:currentmodule:: KmlNetworkLinkViewRefreshMode

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NEVER`
              - Do not refresh the network link when the camera's view changes.

            * - :py:attr:`~ON_REQUEST`
              - Only refresh the network link when it is explicitly refreshed by calling the refresh method.

            * - :py:attr:`~ON_STOP`
              - Refresh the network link after camera view movement stops for the duration specified by view refresh time.

            * - :py:attr:`~ON_REGION`
              - Refresh the network link when the region associated with this link becomes active.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import KmlNetworkLinkViewRefreshMode


