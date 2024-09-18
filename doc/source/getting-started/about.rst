About PySTK
###########

PySTK is the next generation Python API for Ansys Systems Toolkit (STK). The
API is an evolution of the existing STK Python API with the following goals:

- PyAnsys compliance:

   - The API integrates with the rest of `PyAnsys`_ , enabling you to connect
     STK with other Ansys products.

   - The API adopts the PyAnsys guidelines, including similar packaging, naming
     conventions, and documentation.

   - The API integrates better with the Python ecosystem by following the best
     practices in the `Python Enhancement Proposals (PEP8) Style Guide`_ .

- Usability improvements:

   - The interface, class, method and property names have been updated to
     remove cryptic abbreviations, making your code easier to read and
     maintain, and facilitates discovering and locating API features.

   - Better code completion is now available in IDEs (Visual Studio Code,
     PyCharm) or Jupyter Lab.

   - The number of types included in the API has been greatly reduced by
     merging redundant interfaces and classes.

- Documentation improvements:

   - The documentation has been reorganized and features an :ref:`API reference`
     that is specific to Python, whereas the `STK Programming Help`_ covers
     multiple languages, including C#, Java and Python.

   - :ref:`Examples <Examples>` provided to demonstrate how to use the API for
     specific aerospace applications.

As a result of this evolution, existing code must be migrated to the PySTK API.
For details on migrating your code, refer to the Migrate to PySTK topic.

API version
===========

The current version of the API is |version|. This is an alpha release with the
goal of collecting feedback and improving the new API before widespread
adoption occurs.

Contribute to PySTK
===================

Contributions to the `PySTK GitHub repository
<https://github.com/ansys-internal/pystk>`_ are welcome and encouraged. This
includes updates to the documentation, examples, and the addition of high-level
APIs/helper functions that facilitate specific workflows.

What's included in the API
==========================

The PySTK API offers a variety of options to automate and customize STK and to
integrate its technology into other workflows. Additional options enable you to
interface to STK externally through gRPC (Remote Procedure Calls), and to
develop custom applications.

Available configurations and environments
-----------------------------------------

Multiple configurations and environments are supported, requiring specific
instructions to get setup. Refer to the table below to access prerequisites and
installation instructions for your desired environment.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - **Environment**
      - **Prerequisites guide**
      - **Installation guide**
    * - Locally on Windows
      - :ref:`Prerequisites <Windows local prerequisites>`
      - :ref:`Installation <Install PySTK locally in Windows>`
    * - Locally on Linux
      - :ref:`Prerequisites <Linux local prerequisites>`
      - :ref:`Installation <Install PySTK locally in Linux>`
    * - Windows Docker container
      - :ref:`Prerequisites <Windows Docker prerequisites>`
      - :ref:`Installation <Install PySTK in a Windows container>`
    * - Linux Docker container
      - :ref:`Prerequisites <Linux Docker prerequisites>`
      - :ref:`Installation <Install PySTK in a Linux container>`
     

Once your environment is setup, you can review the :ref:`user guide <User
guide>` to get acquainted with the API, or browse :ref:`examples <Examples>`.
Additionally, the :ref:`API reference` describes all types that are available
through the API.

Current limitations
===================

The PySTK API currently has the following limitations:

-  UI plugins are not currently supported.

-  Enabling socket connection by setting
  :py:attr:`STKXApplication.enable_connect` to ``True`` is not currently
  supported. Connect commands may be used through the
  :py:meth:`StkObjectRoot.execute_command` method.

-  When using gRPC, the following methods and properties
  :py:meth:`AccessConstraintPluginMinMax.get_raw_plugin_object`,
  :py:meth:`VehiclePluginPropagator.get_raw_plugin_object`,
  :py:attr:`ScatteringPointProviderPlugin.raw_plugin_object`,
  :py:attr:`ScatteringPointModelPlugin.raw_plugin_object`,
  :py:attr:`IRadarClutterGeometryModelPlugin.raw_plugin_object`,
  :py:attr:`RadarProbabilityOfDetectionPlugin.raw_plugin_object`,
  :py:attr:`IRadarClutterMapModelPlugin.raw_plugin_object`,
  :py:attr:`RadarCrossSectionComputeStrategyPlugin.raw_plugin_object`,
  :py:attr:`RadarStcAttenuationPlugi.raw_plugin_objectn` are not available and
  always return :py:class:`None`.

- Engine plugins are not currently supported.
