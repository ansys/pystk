IAxesFindAxesWithRateResult
===========================

.. py:class:: ansys.stk.core.vgt.IAxesFindAxesWithRateResult

   Contains the results returned with IAgCrdnAxes.FindInAxesWithRate method.

.. py:currentmodule:: IAxesFindAxesWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAxesFindAxesWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IAxesFindAxesWithRateResult.angular_velocity`
              - Axes' angular velocity.
            * - :py:attr:`~ansys.stk.core.vgt.IAxesFindAxesWithRateResult.orientation`
              - The axes' orientation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAxesFindAxesWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IAxesFindAxesWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: angular_velocity
    :canonical: ansys.stk.core.vgt.IAxesFindAxesWithRateResult.angular_velocity
    :type: ICartesian3Vector

    Axes' angular velocity.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.IAxesFindAxesWithRateResult.orientation
    :type: IOrientation

    The axes' orientation.


