LIGHTING_OBSTRUCTION_MODEL_TYPE
===============================

.. py:class:: ansys.stk.core.stkobjects.LIGHTING_OBSTRUCTION_MODEL_TYPE

   IntEnum


.. py:currentmodule:: LIGHTING_OBSTRUCTION_MODEL_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CENTRAL_BODY_SHAPE`
              - The lighting obstruction model is the surface of the central body ellipsoid.

            * - :py:attr:`~AZ_EL_MASK`
              - Lighting obstruction is computed using the object's Az-El mask if defined, else uses the object's ground model.

            * - :py:attr:`~TERRAIN`
              - Lighting obstruction is computed using terrain data.

            * - :py:attr:`~GROUND_MODEL`
              - The lighting obstruction model is the object's ground model as used in the line-of-sight constraint computation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LIGHTING_OBSTRUCTION_MODEL_TYPE


