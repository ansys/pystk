SWATH_COMPUTATIONAL_METHOD
==========================

.. py:class:: ansys.stk.core.stkobjects.SWATH_COMPUTATIONAL_METHOD

   IntEnum


.. py:currentmodule:: SWATH_COMPUTATIONAL_METHOD

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported computational method.

            * - :py:attr:`~ANALYTICAL`
              - The Analytical Computational Method is only valid if the parent of the Sensor is a Satellite and the Satellite has a Circular Orbit and the Satellite uses Nadir ECF Attitude and the Sensor is Nadir (Fixed) Pointing.

            * - :py:attr:`~NUMERICAL`
              - The Numerical Computational Method is not valid if the Sensor uses a Custom Pattern.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SWATH_COMPUTATIONAL_METHOD


