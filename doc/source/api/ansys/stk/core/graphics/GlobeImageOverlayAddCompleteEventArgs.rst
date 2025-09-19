GlobeImageOverlayAddCompleteEventArgs
=====================================

.. py:class:: ansys.stk.core.graphics.GlobeImageOverlayAddCompleteEventArgs

   The event is raised when the globe image overlay is displayed for the first time after being added using AddAsync.

.. py:currentmodule:: GlobeImageOverlayAddCompleteEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.GlobeImageOverlayAddCompleteEventArgs.overlay`
              - The overlay object that was added earlier using AddAsync.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import GlobeImageOverlayAddCompleteEventArgs


Property detail
---------------

.. py:property:: overlay
    :canonical: ansys.stk.core.graphics.GlobeImageOverlayAddCompleteEventArgs.overlay
    :type: IGlobeImageOverlay

    The overlay object that was added earlier using AddAsync.


