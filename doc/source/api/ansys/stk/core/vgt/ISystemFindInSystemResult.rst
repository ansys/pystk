ISystemFindInSystemResult
=========================

.. py:class:: ansys.stk.core.vgt.ISystemFindInSystemResult

   Contains the results returned with IAgCrdnSystem.FindInSystem method.

.. py:currentmodule:: ISystemFindInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISystemFindInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.ISystemFindInSystemResult.position`
              - A position vector.
            * - :py:attr:`~ansys.stk.core.vgt.ISystemFindInSystemResult.velocity`
              - A velocity vector.
            * - :py:attr:`~ansys.stk.core.vgt.ISystemFindInSystemResult.rate`
              - Rate of change.
            * - :py:attr:`~ansys.stk.core.vgt.ISystemFindInSystemResult.orientation`
              - Orientation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISystemFindInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ISystemFindInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.ISystemFindInSystemResult.position
    :type: ICartesian3Vector

    A position vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.ISystemFindInSystemResult.velocity
    :type: ICartesian3Vector

    A velocity vector.

.. py:property:: rate
    :canonical: ansys.stk.core.vgt.ISystemFindInSystemResult.rate
    :type: ICartesian3Vector

    Rate of change.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.ISystemFindInSystemResult.orientation
    :type: IOrientation

    Orientation.


