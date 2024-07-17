Constellation
=============

.. py:class:: ansys.stk.core.stkobjects.Constellation

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Class represents the STK Constellation.

.. py:currentmodule:: Constellation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Constellation.objects`
              - Get the collection of objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Constellation.constraints`
              - Get the constellation's constraints.
            * - :py:attr:`~ansys.stk.core.stkobjects.Constellation.graphics`
              - Constellation's 2D graphics settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.Constellation.routing`
              - Constellation's routing settings.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Constellation


Property detail
---------------

.. py:property:: objects
    :canonical: ansys.stk.core.stkobjects.Constellation.objects
    :type: IObjectLinkCollection

    Get the collection of objects in the chain.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.Constellation.constraints
    :type: IConstellationConstraints

    Get the constellation's constraints.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Constellation.graphics
    :type: IConstellationGraphics

    Constellation's 2D graphics settings.

.. py:property:: routing
    :canonical: ansys.stk.core.stkobjects.Constellation.routing
    :type: IConstellationRouting

    Constellation's routing settings.


