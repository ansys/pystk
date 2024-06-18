IYarkovskyFunc
==============

.. py:class:: IYarkovskyFunc

   object
   
   Properties for the Yarkovsky Effect propagator function.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~alpha`
            * - :py:meth:`~r0`
            * - :py:meth:`~nm`
            * - :py:meth:`~nn`
            * - :py:meth:`~nk`
            * - :py:meth:`~a1`
            * - :py:meth:`~a2`
            * - :py:meth:`~a3`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IYarkovskyFunc


Property detail
---------------

.. py:property:: alpha
    :canonical: ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc.alpha
    :type: float

    Yarkovsky effect alpha constant. Dimensionless.

.. py:property:: r0
    :canonical: ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc.r0
    :type: float

    Heliocentric sublimation distance. Uses distance dimension.

.. py:property:: nm
    :canonical: ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc.nm
    :type: float

    Yarkovsky effect m exponent. Dimensionless.

.. py:property:: nn
    :canonical: ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc.nn
    :type: float

    Yarkovsky effect n exponent. Dimensionless.

.. py:property:: nk
    :canonical: ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc.nk
    :type: float

    Yarkovsky effect k exponent. Dimensionless.

.. py:property:: a1
    :canonical: ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc.a1
    :type: float

    Radial acceleration multiplier. Uses acceleration dimension.

.. py:property:: a2
    :canonical: ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc.a2
    :type: float

    Velocity tangent acceleration multiplier. Uses acceleration dimension.

.. py:property:: a3
    :canonical: ansys.stk.core.stkobjects.astrogator.IYarkovskyFunc.a3
    :type: float

    Orbit normal acceleration multiplier. Uses acceleration dimension.


