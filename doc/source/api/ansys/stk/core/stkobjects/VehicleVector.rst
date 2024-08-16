VehicleVector
=============

.. py:class:: ansys.stk.core.stkobjects.VehicleVector

   Aligned and Constrained attitude profile.

.. py:currentmodule:: VehicleVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleVector.body`
              - Get the body-fixed vector that is aligned or constrained with respect to the reference vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleVector.reference_vector`
              - Gets or sets the reference vector with respect to which the body-fixed vector is aligned or constrained.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleVector.available_reference_vectors`
              - Returns the available reference vectors.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleVector


Property detail
---------------

.. py:property:: body
    :canonical: ansys.stk.core.stkobjects.VehicleVector.body
    :type: IDirection

    Get the body-fixed vector that is aligned or constrained with respect to the reference vector.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.stkobjects.VehicleVector.reference_vector
    :type: str

    Gets or sets the reference vector with respect to which the body-fixed vector is aligned or constrained.

.. py:property:: available_reference_vectors
    :canonical: ansys.stk.core.stkobjects.VehicleVector.available_reference_vectors
    :type: list

    Returns the available reference vectors.


