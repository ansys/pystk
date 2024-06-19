JPEG2000_COMPRESSION_PROFILE
============================

.. py:class:: JPEG2000_COMPRESSION_PROFILE

   IntEnum


.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~DEFAULT`
              - This is the default profile, which is recommended for those unfamiliar with the others.

            * - :py:attr:`~NITF_BIIF_NPJE`
              - This profile is designed for U.S. and NATO military applications.

            * - :py:attr:`~NITF_BIIF_EPJE`
              - This profile is designed for U.S. and NATO military applications. Based on NPJE, the profile is used for image exploitation, and improves image read times for lower resolutions in large images as compared to NPJE.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import JPEG2000_COMPRESSION_PROFILE


