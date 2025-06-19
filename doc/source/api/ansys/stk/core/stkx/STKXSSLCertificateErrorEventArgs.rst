STKXSSLCertificateErrorEventArgs
================================

.. py:class:: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs

   Provide information about an SSL certificate that is expired or invalid.

.. py:currentmodule:: STKXSSLCertificateErrorEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.set_ignore_error`
              - Specify True to ignore the certificate error and continue with establishing secure HTTP connection to the remote server.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.set_ignore_error_permanently`
              - Specify True to ignore the certificate error and add the certificate to the list of trusted certificates.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.is_error_ignored`
              - Return whether the invalid certificate error is ignored.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.serial_number`
              - Certificate's serial number.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.issuer`
              - The provider who issued the certificate.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.subject`
              - Certificate's subject field.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.valid_date`
              - Certificate's valid date.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.expiration_date`
              - Certificate's expiration date.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.is_expired`
              - Whether the certificate is expired.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.pem_data`
              - Certificate's PEM data encoded as base-64.
            * - :py:attr:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.handled`
              - Indicate whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import STKXSSLCertificateErrorEventArgs


Property detail
---------------

.. py:property:: is_error_ignored
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.is_error_ignored
    :type: bool

    Return whether the invalid certificate error is ignored.

.. py:property:: serial_number
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.serial_number
    :type: str

    Certificate's serial number.

.. py:property:: issuer
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.issuer
    :type: str

    The provider who issued the certificate.

.. py:property:: subject
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.subject
    :type: str

    Certificate's subject field.

.. py:property:: valid_date
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.valid_date
    :type: datetime

    Certificate's valid date.

.. py:property:: expiration_date
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.expiration_date
    :type: datetime

    Certificate's expiration date.

.. py:property:: is_expired
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.is_expired
    :type: bool

    Whether the certificate is expired.

.. py:property:: pem_data
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.pem_data
    :type: str

    Certificate's PEM data encoded as base-64.

.. py:property:: handled
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.handled
    :type: bool

    Indicate whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners.


Method detail
-------------

.. py:method:: set_ignore_error(self, ignore_error: bool) -> None
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.set_ignore_error

    Specify True to ignore the certificate error and continue with establishing secure HTTP connection to the remote server.

    :Parameters:

        **ignore_error** : :obj:`~bool`


    :Returns:

        :obj:`~None`


.. py:method:: set_ignore_error_permanently(self, ignore_error_permanently: bool) -> None
    :canonical: ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs.set_ignore_error_permanently

    Specify True to ignore the certificate error and add the certificate to the list of trusted certificates.

    :Parameters:

        **ignore_error_permanently** : :obj:`~bool`


    :Returns:

        :obj:`~None`










