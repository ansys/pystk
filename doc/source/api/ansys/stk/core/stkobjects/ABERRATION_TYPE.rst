ABERRATION_TYPE
===============

.. py:class:: ABERRATION_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Not supported type.

            * - :py:attr:`~TOTAL`
              - Total: Apply the full aberration correction, when light time delay is computed.

            * - :py:attr:`~ANNUAL`
              - Annual: Consider annual aberration only. Aberration is applied only cases where the light time delay is computed using the solar system barycenter frame.

            * - :py:attr:`~NONE`
              - None: Ignore aberration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ABERRATION_TYPE


