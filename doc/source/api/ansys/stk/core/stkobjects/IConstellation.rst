IConstellation
==============

.. py:class:: ansys.stk.core.stkobjects.IConstellation

   object
   
   Configuration options for constellations.

.. py:currentmodule:: IConstellation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellation.objects`
              - Get the collection of objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellation.constraints`
              - Get the constellation's constraints.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellation.graphics`
              - Constellation's 2D graphics settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.IConstellation.routing`
              - Constellation's routing settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IConstellation


Property detail
---------------

.. py:property:: objects
    :canonical: ansys.stk.core.stkobjects.IConstellation.objects
    :type: IObjectLinkCollection

    Get the collection of objects in the chain.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.IConstellation.constraints
    :type: IConstellationConstraints

    Get the constellation's constraints.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IConstellation.graphics
    :type: IConstellationGraphics

    Constellation's 2D graphics settings.

.. py:property:: routing
    :canonical: ansys.stk.core.stkobjects.IConstellation.routing
    :type: IConstellationRouting

    Constellation's routing settings.


