ICalculationToolParameterSetGroundTrajectory
============================================

.. py:class:: ICalculationToolParameterSetGroundTrajectory

   object
   
   Ground trajectory parameter set contains various representations of trajectory of a point relative to central body reference shape.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~location`
            * - :py:meth:`~central_body`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolParameterSetGroundTrajectory


Property detail
---------------

.. py:property:: location
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetGroundTrajectory.location
    :type: IAgCrdnPoint

    Get the point for which ground trajectory representations are computed.

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.ICalculationToolParameterSetGroundTrajectory.central_body
    :type: str

    Get the central body relative to which ground trajectory representations are computed. Both the central body reference shape and its CBF (central body centered fixed) system are used by this parameter set.


