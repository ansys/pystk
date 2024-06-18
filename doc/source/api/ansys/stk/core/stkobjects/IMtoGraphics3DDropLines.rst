IMtoGraphics3DDropLines
=======================

.. py:class:: IMtoGraphics3DDropLines

   object
   
   Interface for MTO droplines.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~position`
            * - :py:meth:`~ephemeris`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3DDropLines


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DDropLines.position
    :type: "IAgVeVODropLinePosItemCollection"

    Get a list of droplines from the MTO's current positions.

.. py:property:: ephemeris
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DDropLines.ephemeris
    :type: "IAgVeVODropLinePathItemCollection"

    Get a list of droplines at intervals along the MTO's ephemeris.


