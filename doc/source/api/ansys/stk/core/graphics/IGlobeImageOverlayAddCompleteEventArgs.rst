IGlobeImageOverlayAddCompleteEventArgs
======================================

.. py:class:: IGlobeImageOverlayAddCompleteEventArgs

   object
   
   The event is raised when the globe image overlay is displayed for the first time after being added using AddAsync.

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

    from ansys.stk.core.graphics import IGlobeImageOverlayAddCompleteEventArgs


Property detail
---------------

.. py:property:: overlay
    :canonical: ansys.stk.core.graphics.IGlobeImageOverlayAddCompleteEventArgs.overlay
    :type: "IAgStkGraphicsGlobeImageOverlay"

    The overlay object that was added earlier using AddAsync.


