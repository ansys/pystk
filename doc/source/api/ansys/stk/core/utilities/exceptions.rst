The ``exceptions`` module
=========================

.. py:module:: ansys.stk.core.utilities.exceptions

Summary
-------

.. tab-set::

    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:class:`~ansys.stk.core.utilities.exceptions.STKInitializationError`
              - Raised in STKDesktop and STKEngine when unable to initialize or attach to STK.

            * - :py:class:`~ansys.stk.core.utilities.exceptions.STKInvalidCastError`
              - Raised when attempting to cast an object to an unsupported interface or class type.

            * - :py:class:`~ansys.stk.core.utilities.exceptions.STKRuntimeError`
              - Raised when an STK method call fails.

            * - :py:class:`~ansys.stk.core.utilities.exceptions.STKAttributeError`
              - Raised when attempting to set an unrecognized attribute within the STK API.

            * - :py:class:`~ansys.stk.core.utilities.exceptions.STKEventsAPIError`
              - Raised when attempting to assign to an STK Event rather than using operator += or -=.

            * - :py:class:`~ansys.stk.core.utilities.exceptions.STKPluginMethodNotImplementedError`
              - Raised when a plugin method is called by STK that was not implemented by the user.

            * - :py:class:`~ansys.stk.core.utilities.exceptions.STKInvalidTimerError`
              - Raised when attempting to use an engine timer that cannot be implemented.

            * - :py:class:`~ansys.stk.core.utilities.exceptions.STKColorError`
              - Raised when a problem is encountered with color classes.

            * - :py:class:`~ansys.stk.core.utilities.exceptions.GrpcUtilitiesError`
              - Raised when using gRPC utilities in an unsupported manner.



Description
-----------

Contains specific exceptions that may be raised from the STK API.

.. py:currentmodule:: ansys.stk.core.utilities.exceptions

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     STKInitializationError<exceptions/STKInitializationError>
     STKInvalidCastError<exceptions/STKInvalidCastError>
     STKRuntimeError<exceptions/STKRuntimeError>
     STKAttributeError<exceptions/STKAttributeError>
     STKEventsAPIError<exceptions/STKEventsAPIError>
     STKPluginMethodNotImplementedError<exceptions/STKPluginMethodNotImplementedError>
     STKInvalidTimerError<exceptions/STKInvalidTimerError>
     STKColorError<exceptions/STKColorError>
     GrpcUtilitiesError<exceptions/GrpcUtilitiesError>


