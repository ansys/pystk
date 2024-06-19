IConstellation
==============

.. py:class:: IConstellation

   object
   
   Configuration options for constellations.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~objects`
            * - :py:meth:`~constraints`
            * - :py:meth:`~graphics`
            * - :py:meth:`~routing`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IConstellation


Property detail
---------------

.. py:property:: objects
    :canonical: ansys.stk.core.stkobjects.IConstellation.objects
    :type: IAgObjectLinkCollection

    Get the collection of objects in the chain.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.IConstellation.constraints
    :type: IAgCnConstraints

    Get the constellation's constraints.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IConstellation.graphics
    :type: IAgCnGraphics

    Constellation's 2D graphics settings.

.. py:property:: routing
    :canonical: ansys.stk.core.stkobjects.IConstellation.routing
    :type: IAgCnRouting

    Constellation's routing settings.


