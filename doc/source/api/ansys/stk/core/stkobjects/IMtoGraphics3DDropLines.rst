IMtoGraphics3DDropLines
=======================

.. py:class:: ansys.stk.core.stkobjects.IMtoGraphics3DDropLines

   object
   
   Interface for MTO droplines.

.. py:currentmodule:: IMtoGraphics3DDropLines

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DDropLines.position`
              - Get a list of droplines from the MTO's current positions.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoGraphics3DDropLines.ephemeris`
              - Get a list of droplines at intervals along the MTO's ephemeris.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoGraphics3DDropLines


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DDropLines.position
    :type: IVehicleGraphics3DDropLinePositionItemCollection

    Get a list of droplines from the MTO's current positions.

.. py:property:: ephemeris
    :canonical: ansys.stk.core.stkobjects.IMtoGraphics3DDropLines.ephemeris
    :type: IVehicleGraphics3DDropLinePathItemCollection

    Get a list of droplines at intervals along the MTO's ephemeris.


