About PySTK
###########

PySTK is the next generation Python API for Ansys Systems Toolkit (STK). The API is an evolution of the existing STK Python API with the following goals:

- PyAnsys compliance:
   - The API integrates with the rest of `PyAnsys <https://docs.pyansys.com/>`_, enabling you to connect STK with other Ansys products.

   - The API adopts the PyAnsys guidelines, including similar packaging, naming conventions, and documentation.

   - The API integrates better with the Python ecosystem by following the best practices in the `Python Enhancement Proposals (PEP8) Style Guide <https://peps.python.org/pep-0008/>`_.

- Usability improvements:
   - The interface, class, method and property names have been updated to remove cryptic abbreviations, making your code easier to read and maintain, and facilitates discovering and locating API features.

   - Better code completion is now available in IDEs (Visual Studio Code, PyCharm) or Jupyter Lab.

   - The number of types included in the API has been greatly reduced by merging redundant interfaces and classes.

- Documentation improvements:
   - The documentation has been reorganized and features an `API Reference <https://stk.docs.pyansys.com/version/dev/api.html>`_ that is specific to Python, whereas the `STK Programming Help <https://help.agi.com/stkdevkit/index.htm>`_ covers multiple languages, including C#, Java and Python.

   - `Examples <https://stk.docs.pyansys.com/version/dev/examples.html>`_ are provided to demonstrate how to use the API for specific aerospace applications.

As a result of this evolution, existing code must be migrated to the PySTK API. For details on migrating your code, refer to the Migrate to PySTK topic.

API version
===========

The current version of the API is 0.1. This is an alpha release with the goal of collecting feedback and improving the new API before widespread adoption occurs.

Contribute to PySTK
===================

Contributions to the `PySTK GitHub repository <https://github.com/ansys-internal/pystk>`_ are welcome and encouraged. This includes updates to the documentation, examples, and the addition of high-level APIs/helper functions that facilitate specific workflows.

What's included in the API
==========================

The PySTK API offers a variety of options to automate and customize STK and to integrate its technology into other workflows. Additional options enable you to interface to STK externally through gRPC (Remote Procedure Calls), and to develop custom applications.

Available configurations and environments
-----------------------------------------

Multiple configurations and environments are supported, requiring specific instructions to get setup. Refer to the table below to access prerequisites and installation instructions for your desired environment.

.. jinja::

    .. list-table::
        :widths: 10 20 
        :header-rows: 1

        * - **Environment**
          - **Details**
        * - Locally on Windows
          - - `Prerequisites <https://stk.docs.pyansys.com/version/dev/getting-started/prerequisites/windows/local.html>`_
            - `Installation instructions <https://stk.docs.pyansys.com/version/dev/getting-started/install/windows/local.html>`_
        * - Locally on Linux
          - - `Prerequisites <https://stk.docs.pyansys.com/version/dev/getting-started/prerequisites/linux/local.html>`_
            - `Installation instructions <https://stk.docs.pyansys.com/version/dev/getting-started/install/linux/local.html>`_
        * - Windows Docker container
          - - `Prerequisites <https://stk.docs.pyansys.com/version/dev/getting-started/prerequisites/windows/docker.html>`_
            - `Installation instructions <https://stk.docs.pyansys.com/version/dev/getting-started/install/windows/docker.html>`_
        * - Linux Docker container
          - - `Prerequisites <https://stk.docs.pyansys.com/version/dev/getting-started/prerequisites/linux/docker.html>`_
            - `Installation instructions <https://stk.docs.pyansys.com/version/dev/getting-started/install/linux/docker.html>`_ 
         

Once your environment is setup, you can review the `user guide <https://stk.docs.pyansys.com/version/dev/user-guide.html>`_ to get acquainted with the API, or browse `examples <https://stk.docs.pyansys.com/version/dev/examples.html>`_. Additionally, the `API reference <https://stk.docs.pyansys.com/version/dev/api.html>`_ describes all types that are available through the API.

Current limitations
===================

The PySTK API currently has the following limitations:

-  UI plugins are not currently supported.
-  Enabling socket connection by setting ``STKXApplication.enable_connect`` to True is not currently supported. Connect commands may be used through the object model root.
   `execute_command <https://stk.docs.pyansys.com/version/dev/api/ansys/stk/core/stkobjects/StkObjectRoot.html>`_ method.
-  When using gRPC, ``get_raw_plugin_object`` (available on ``AccessConstraintPluginMinMax`` and ``VehiclePluginPropagator``) and ``raw_plugin_object`` (available on ``ScatteringPointProviderPlugin``, ``ScatteringPointModelPlugin``, ``IRadarClutterGeometryModelPlugin``, ``RadarProbabilityOfDetectionPlugin``, ``IRadarClutterMapModelPlugin``, ``RadarCrossSectionComputeStrategyPlugin``, and ``RadarStcAttenuationPlugin``) are not available and always return None.
- Engine plugins are not currently supported.


