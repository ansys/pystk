SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD
=====================================

.. py:class:: ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD

   IntEnum


.. py:currentmodule:: SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - An invalid AgESpEnvMagneticMainField value.

            * - :py:attr:`~IGRF`
              - Models the main geomagnetic field using the IGRF model.

            * - :py:attr:`~OFFSET_DIPOLE`
              - Models the main geomagnetic field using a dipole offset from the Earth center.

            * - :py:attr:`~FAST_IGRF`
              - Models the main geomagnetic field using the Fast IGRF model.

            * - :py:attr:`~TILTED_DIPOLE`
              - Models the main geomagnetic field using a tilted dipole centered at the Earth center.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD


