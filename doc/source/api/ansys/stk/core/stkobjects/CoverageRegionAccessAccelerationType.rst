CoverageRegionAccessAccelerationType
====================================

.. py:class:: ansys.stk.core.stkobjects.CoverageRegionAccessAccelerationType

   IntEnum


.. py:currentmodule:: CoverageRegionAccessAccelerationType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown regional acceleration option.

            * - :py:attr:`~AUTOMATIC`
              - Automatic - if selected and the grid altitude is 0 with respect to the defining ellipsoid for the central body, visibility to regions' bounding sets of points is computed and used to limit times for computations to enclosed points.

            * - :py:attr:`~OFF`
              - Off - should be selected in certain cases, such as the use of a very small or narrow sensor in conjunction with a very narrow coverage region.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageRegionAccessAccelerationType


