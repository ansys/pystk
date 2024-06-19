CRDN_PARAMETER_SET_TYPE
=======================

.. py:class:: CRDN_PARAMETER_SET_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported parameter set.

            * - :py:attr:`~ATTITUDE`
              - A parameter set type is defined by identifying one set of axes in reference to another.

            * - :py:attr:`~GROUND_TRAJECTORY`
              - A parameter set type is defined by identifying location in reference central body.

            * - :py:attr:`~TRAJECTORY`
              - A parameter set type is defined by identifying location in reference coordinate system.

            * - :py:attr:`~ORBIT`
              - A parameter set type is defined by identifying orbiting point and its central body.

            * - :py:attr:`~VECTOR`
              - A parameter set type is defined by identifying vector in reference axes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_PARAMETER_SET_TYPE


