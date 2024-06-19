IVehicleConsiderAnalysisCollectionElement
=========================================

.. py:class:: IVehicleConsiderAnalysisCollectionElement

   object
   
   Item in Consider Analysis list for HPOP covariance.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~name`
            * - :py:meth:`~value`
            * - :py:meth:`~x`
            * - :py:meth:`~y`
            * - :py:meth:`~z`
            * - :py:meth:`~vx`
            * - :py:meth:`~vy`
            * - :py:meth:`~vz`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleConsiderAnalysisCollectionElement


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.type
    :type: VEHICLE_CONSIDER_ANALYSIS_TYPE

    Parameter type.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.name
    :type: str

    Get the consider parameter.

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.value
    :type: float

    Self-covariance value of the consider parameter. Dimensionless.

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.x
    :type: float

    X position covariance.Dimensionless.

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.y
    :type: float

    Y position covariance. Dimensionless.

.. py:property:: z
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.z
    :type: float

    Z position covariance. Dimensionless.

.. py:property:: vx
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.vx
    :type: float

    X velocity covariance. Dimensionless.

.. py:property:: vy
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.vy
    :type: float

    Y velocity covariance. Dimensionless.

.. py:property:: vz
    :canonical: ansys.stk.core.stkobjects.IVehicleConsiderAnalysisCollectionElement.vz
    :type: float

    Z velocity covariance. Dimensionless.


