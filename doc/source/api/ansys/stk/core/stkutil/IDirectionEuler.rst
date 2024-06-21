IDirectionEuler
===============

.. py:class:: ansys.stk.core.stkutil.IDirectionEuler

   IDirection
   
   Interface for Euler direction sequence.

.. py:currentmodule:: IDirectionEuler

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IDirectionEuler.b`
            * - :py:attr:`~ansys.stk.core.stkutil.IDirectionEuler.c`
            * - :py:attr:`~ansys.stk.core.stkutil.IDirectionEuler.sequence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IDirectionEuler


Property detail
---------------

.. py:property:: b
    :canonical: ansys.stk.core.stkutil.IDirectionEuler.b
    :type: typing.Any

    Euler B angle. Uses Angle Dimension.

.. py:property:: c
    :canonical: ansys.stk.core.stkutil.IDirectionEuler.c
    :type: typing.Any

    Euler C angle. Uses Angle Dimension.

.. py:property:: sequence
    :canonical: ansys.stk.core.stkutil.IDirectionEuler.sequence
    :type: EULER_DIRECTION_SEQUENCE

    Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.


