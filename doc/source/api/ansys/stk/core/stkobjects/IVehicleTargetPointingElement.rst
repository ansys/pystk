IVehicleTargetPointingElement
=============================

.. py:class:: IVehicleTargetPointingElement

   object
   
   Target pointing data for target pointing attitude.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reset_constrained_vector_reference`
              - Set the constrained vector reference to a default value. Returns true if succeeded, otherwise return false.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~target`
            * - :py:meth:`~aligned_vector`
            * - :py:meth:`~constrained_vector`
            * - :py:meth:`~constrained_vector_reference`
            * - :py:meth:`~available_constrained_vectors`
            * - :py:meth:`~latitude`
            * - :py:meth:`~longitude`
            * - :py:meth:`~altitude`
            * - :py:meth:`~intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTargetPointingElement


Property detail
---------------

.. py:property:: target
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.target
    :type: IAgLinkToObject

    Get a reference to the targeted object.

.. py:property:: aligned_vector
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.aligned_vector
    :type: IAgDirection

    Get the aligned vector.

.. py:property:: constrained_vector
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.constrained_vector
    :type: IAgDirection

    Get the constrained vector.

.. py:property:: constrained_vector_reference
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.constrained_vector_reference
    :type: str

    Gets or sets the reference for the constrained vector.

.. py:property:: available_constrained_vectors
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.available_constrained_vectors
    :type: list

    Returns the available constrained vectors.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.latitude
    :type: float

    Get the LLA position's latitude. Uses Latitude Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.longitude
    :type: float

    Get the LLA position's longitude. Uses Longitude Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.altitude
    :type: float

    Get the LLA position's altitude. Uses Distance Dimension.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.intervals
    :type: IAgVeTargetPointingIntervalCollection

    Returns a list of scheduled time intervals for the current target.


Method detail
-------------






.. py:method:: reset_constrained_vector_reference(self) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.reset_constrained_vector_reference

    Set the constrained vector reference to a default value. Returns true if succeeded, otherwise return false.

    :Returns:

        :obj:`~bool`






