AttitudeProfileInertial
=======================

.. py:class:: ansys.stk.core.stkobjects.AttitudeProfileInertial

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`

   Inertially fixed attitude profile: maintains a constant orientation of the body-fixed axes with respect to the inertial axes, using the selected coordinate type.

.. py:currentmodule:: AttitudeProfileInertial

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileInertial.inertial`
              - Get inertial axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeProfileInertial


Property detail
---------------

.. py:property:: inertial
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileInertial.inertial
    :type: IOrientation

    Get inertial axes.


