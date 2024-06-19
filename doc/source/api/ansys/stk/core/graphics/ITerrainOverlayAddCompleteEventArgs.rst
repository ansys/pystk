ITerrainOverlayAddCompleteEventArgs
===================================

.. py:class:: ITerrainOverlayAddCompleteEventArgs

   object
   
   The event is raised when the terrain overlay is displayed for the first time after having been added using AddAsync.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~overlay`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITerrainOverlayAddCompleteEventArgs


Property detail
---------------

.. py:property:: overlay
    :canonical: ansys.stk.core.graphics.ITerrainOverlayAddCompleteEventArgs.overlay
    :type: IAgStkGraphicsTerrainOverlay

    The terrain overlay being displayed for the first time.


