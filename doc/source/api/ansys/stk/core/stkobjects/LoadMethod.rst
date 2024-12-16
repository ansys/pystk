LoadMethod
==========

.. py:class:: ansys.stk.core.stkobjects.LoadMethod

   IntEnum


.. py:currentmodule:: LoadMethod

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~AUTOMATIC_LOAD`
              - Auto load: STK automatically loads the TLE sets corresponding to the SSC number of the satellite when the satellite is loaded.

            * - :py:attr:`~FILE_INSERT`
              - File insert: adds the selected TLE data but retains TLE data that is currently associated with the satellite.

            * - :py:attr:`~FILE_LOAD`
              - File load: loads the selected TLE data and replaces all TLE data that is currently associated with the satellite.

            * - :py:attr:`~ONLINE_AUTOMATIC_LOAD`
              - Online auto-load: STK automatically loads the TLE sets corresponding to the SSC number of the satellite from the AGI Web site.

            * - :py:attr:`~ONLINE_LOAD`
              - goes directly to the AGI Web site to download the latest TLE sets.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LoadMethod


