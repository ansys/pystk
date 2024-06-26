GRAV_PARAM_SOURCE
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.GRAV_PARAM_SOURCE

   IntEnum


.. py:currentmodule:: GRAV_PARAM_SOURCE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CENTRAL_BODY_FILE`
              - The Cb file provided with STK; uses the default, body centered gravity source for the central body.

            * - :py:attr:`~DESIGN_EXPLORER_OPTIMIZER_FILE`
              - A DE file; body centered for the inner planets and barycentered for the outer planets.

            * - :py:attr:`~USER`
              - User defined; requires you to specify the mu value of the Gravitational Parameter.

            * - :py:attr:`~CENTRAL_BODY_FILE_SYSTEM`
              - The Cb file provided with STK; uses the default, barycentered gravity source for the central body.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GRAV_PARAM_SOURCE


