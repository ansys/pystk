ITimeToolEventIntervalCollectionLighting
========================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionLighting

   object
   
   Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

.. py:currentmodule:: ITimeToolEventIntervalCollectionLighting

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionLighting.location`
              - The location point to compute sunlight, penumbra and umbra.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionLighting.eclipsing_bodies`
              - A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollectionLighting.use_object_eclipsing_bodies`
              - When true, configure eclipsing bodies list based on that of parent STK Object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalCollectionLighting


Property detail
---------------

.. py:property:: location
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionLighting.location
    :type: IVectorGeometryToolPoint

    The location point to compute sunlight, penumbra and umbra.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionLighting.eclipsing_bodies
    :type: list

    A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.

.. py:property:: use_object_eclipsing_bodies
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollectionLighting.use_object_eclipsing_bodies
    :type: bool

    When true, configure eclipsing bodies list based on that of parent STK Object.


