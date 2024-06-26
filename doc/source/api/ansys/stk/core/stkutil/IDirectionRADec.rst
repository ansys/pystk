IDirectionRADec
===============

.. py:class:: ansys.stk.core.stkutil.IDirectionRADec

   IDirection
   
   Interface for Spherical direction (Right Ascension and Declination).

.. py:currentmodule:: IDirectionRADec

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IDirectionRADec.dec`
              - Declination: angle above the x-y plane. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirectionRADec.ra`
              - Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirectionRADec.magnitude`
              - A unitless value that represents magnitude.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IDirectionRADec


Property detail
---------------

.. py:property:: dec
    :canonical: ansys.stk.core.stkutil.IDirectionRADec.dec
    :type: typing.Any

    Declination: angle above the x-y plane. Uses Latitude Dimension.

.. py:property:: ra
    :canonical: ansys.stk.core.stkutil.IDirectionRADec.ra
    :type: typing.Any

    Right Ascension: angle in x-y plane from x towards y. Uses Longitude Dimension.

.. py:property:: magnitude
    :canonical: ansys.stk.core.stkutil.IDirectionRADec.magnitude
    :type: float

    A unitless value that represents magnitude.


