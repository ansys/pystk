IConstellationConstraintObjectRestriction
=========================================

.. py:class:: IConstellationConstraintObjectRestriction

   IConstellationConstraintRestriction
   
   A restriction interface that is satisfied only when specified number of objects meets the conditions for the chain access.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~number_of_objects`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IConstellationConstraintObjectRestriction


Property detail
---------------

.. py:property:: number_of_objects
    :canonical: ansys.stk.core.stkobjects.IConstellationConstraintObjectRestriction.number_of_objects
    :type: int

    A number of objects that must be satisfied to meet conditions for the chain access. Dimensionless.


