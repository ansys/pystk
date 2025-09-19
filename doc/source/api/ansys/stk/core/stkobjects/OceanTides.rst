OceanTides
==========

.. py:class:: ansys.stk.core.stkobjects.OceanTides

   Class defining the contribution of ocean tides.

.. py:currentmodule:: OceanTides

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OceanTides.maximum_degree`
              - Maximum degree: limit the ocean tide model to contributions of a specified maximum degree. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.OceanTides.maximum_order`
              - Maximum order: limit the ocean tide model to contributions of a specified maximum order. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.OceanTides.minimum_amplitude`
              - Minimum amplitude: include only those constituents whose tidal amplitude is sufficiently large by specifying the minimum amplitude to include in the computation. Uses SmallDistanceUnit Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OceanTides


Property detail
---------------

.. py:property:: maximum_degree
    :canonical: ansys.stk.core.stkobjects.OceanTides.maximum_degree
    :type: int

    Maximum degree: limit the ocean tide model to contributions of a specified maximum degree. Dimensionless.

.. py:property:: maximum_order
    :canonical: ansys.stk.core.stkobjects.OceanTides.maximum_order
    :type: int

    Maximum order: limit the ocean tide model to contributions of a specified maximum order. Dimensionless.

.. py:property:: minimum_amplitude
    :canonical: ansys.stk.core.stkobjects.OceanTides.minimum_amplitude
    :type: float

    Minimum amplitude: include only those constituents whose tidal amplitude is sufficiently large by specifying the minimum amplitude to include in the computation. Uses SmallDistanceUnit Dimension.


