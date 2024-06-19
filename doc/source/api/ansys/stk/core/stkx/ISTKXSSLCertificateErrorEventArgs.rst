ISTKXSSLCertificateErrorEventArgs
=================================

.. py:class:: ISTKXSSLCertificateErrorEventArgs

   object
   
   Provide information about an SSL certificate that is expired or invalid.

.. py:currentmodule:: ansys.stk.core.stkx

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_ignore_error`
              - Specify True to ignore the certificate error and continue with establishing secure HTTP connection to the remote server.
            * - :py:meth:`~set_ignore_error_permanently`
              - Specify True to ignore the certificate error and add the certificate to the list of trusted certificates.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_error_ignored`
            * - :py:meth:`~serial_number`
            * - :py:meth:`~issuer`
            * - :py:meth:`~subject`
            * - :py:meth:`~valid_date`
            * - :py:meth:`~expiration_date`
            * - :py:meth:`~is_expired`
            * - :py:meth:`~pem_data`
            * - :py:meth:`~handled`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import ISTKXSSLCertificateErrorEventArgs


Property detail
---------------

.. py:property:: is_error_ignored
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.is_error_ignored
    :type: bool

    Returns whether the invalid certificate error is ignored.

.. py:property:: serial_number
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.serial_number
    :type: str

    Certificate's serial number.

.. py:property:: issuer
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.issuer
    :type: str

    The provider who issued the certificate.

.. py:property:: subject
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.subject
    :type: str

    Certificate's subject field.

.. py:property:: valid_date
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.valid_date
    :type: datetime

    Certificate's valid date.

.. py:property:: expiration_date
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.expiration_date
    :type: datetime

    Certificate's expiration date.

.. py:property:: is_expired
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.is_expired
    :type: bool

    Whether the certificate is expired.

.. py:property:: pem_data
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.pem_data
    :type: str

    Certificate's PEM data encoded as base-64.

.. py:property:: handled
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.handled
    :type: bool

    Indicates whether the event should continue be routed to the listeners. Setting Handled to true will prevent the event from reaching any remaining listeners.


Method detail
-------------

.. py:method:: set_ignore_error(self, ignoreError: bool) -> None
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.set_ignore_error

    Specify True to ignore the certificate error and continue with establishing secure HTTP connection to the remote server.

    :Parameters:

    **ignoreError** : :obj:`~bool`

    :Returns:

        :obj:`~None`


.. py:method:: set_ignore_error_permanently(self, ignoreErrorPermanently: bool) -> None
    :canonical: ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs.set_ignore_error_permanently

    Specify True to ignore the certificate error and add the certificate to the list of trusted certificates.

    :Parameters:

    **ignoreErrorPermanently** : :obj:`~bool`

    :Returns:

        :obj:`~None`










