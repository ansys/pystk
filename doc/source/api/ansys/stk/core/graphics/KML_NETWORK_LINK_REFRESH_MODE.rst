KML_NETWORK_LINK_REFRESH_MODE
=============================

.. py:class:: KML_NETWORK_LINK_REFRESH_MODE

   IntEnum


.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ON_CHANGE`
              - Refresh when the document is loaded and whenever the Link parameters change (the default).

            * - :py:attr:`~ON_INTERVAL`
              - Refresh the network link at the duration specified by refresh interval.

            * - :py:attr:`~ON_EXPIRE`
              - Refresh the network link when the expiration time is reached.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import KML_NETWORK_LINK_REFRESH_MODE


