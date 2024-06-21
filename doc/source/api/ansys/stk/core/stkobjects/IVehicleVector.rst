IVehicleVector
==============

.. py:class:: ansys.stk.core.stkobjects.IVehicleVector

   object
   
   Aligned and Constrained attitude profile.

.. py:currentmodule:: IVehicleVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleVector.body`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleVector.reference_vector`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleVector.available_reference_vectors`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleVector


Property detail
---------------

.. py:property:: body
    :canonical: ansys.stk.core.stkobjects.IVehicleVector.body
    :type: IDirection

    Get the body-fixed vector that is aligned or constrained with respect to the reference vector.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.stkobjects.IVehicleVector.reference_vector
    :type: str

    Gets or sets the reference vector with respect to which the body-fixed vector is aligned or constrained.

.. py:property:: available_reference_vectors
    :canonical: ansys.stk.core.stkobjects.IVehicleVector.available_reference_vectors
    :type: list

    Returns the available reference vectors.


