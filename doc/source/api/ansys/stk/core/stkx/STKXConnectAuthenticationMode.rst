STKXConnectAuthenticationMode
=============================

.. py:class:: ansys.stk.core.stkx.STKXConnectAuthenticationMode

   IntEnum


.. py:currentmodule:: STKXConnectAuthenticationMode

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~SINGLE_USER_LOCAL`
              - Enforce local single user authentication.

            * - :py:attr:`~MUTUAL_TLS`
              - Use MutualTLS for authentication.

            * - :py:attr:`~INSECURE`
              - Allow connections without user authentication. Not recommended.

            * - :py:attr:`~DEFAULT`
              - Using default authentication mode.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import STKXConnectAuthenticationMode


