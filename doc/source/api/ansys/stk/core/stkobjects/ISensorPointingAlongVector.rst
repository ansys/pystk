ISensorPointingAlongVector
==========================

.. py:class:: ISensorPointingAlongVector

   object
   
   IAgSnPtAlongVector Interface for a sensor whose alignment is controlled by a pair of vectors defined using the Vector Geometry tool.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~alignment_vector`
            * - :py:meth:`~available_alignment_vectors`
            * - :py:meth:`~constraint_vector`
            * - :py:meth:`~available_constraint_vectors`
            * - :py:meth:`~clock_angle_offset`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorPointingAlongVector


Property detail
---------------

.. py:property:: alignment_vector
    :canonical: ansys.stk.core.stkobjects.ISensorPointingAlongVector.alignment_vector
    :type: str

    The alignment vector for along vector sensor pointing alignment.

.. py:property:: available_alignment_vectors
    :canonical: ansys.stk.core.stkobjects.ISensorPointingAlongVector.available_alignment_vectors
    :type: list

    Get the available Alignment Vectors.

.. py:property:: constraint_vector
    :canonical: ansys.stk.core.stkobjects.ISensorPointingAlongVector.constraint_vector
    :type: str

    The constraint vector for along vector sensor pointing alignment.

.. py:property:: available_constraint_vectors
    :canonical: ansys.stk.core.stkobjects.ISensorPointingAlongVector.available_constraint_vectors
    :type: list

    Get the available Constraint Vector.

.. py:property:: clock_angle_offset
    :canonical: ansys.stk.core.stkobjects.ISensorPointingAlongVector.clock_angle_offset
    :type: typing.Any

    The clock angle offset for along vector sensor pointing alignment.It is an optional value that is entered in degrees, between -360.0 and 360.0.


