ISystemTransformResult
======================

.. py:class:: ansys.stk.core.vgt.ISystemTransformResult

   Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

.. py:currentmodule:: ISystemTransformResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISystemTransformResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.ISystemTransformResult.vector`
              - The transformed vector.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISystemTransformResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ISystemTransformResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.ISystemTransformResult.vector
    :type: ICartesian3Vector

    The transformed vector.


