.. _ref_release_notes:

Release notes
#############

This document contains the release notes for the PySTK project.

.. vale off

.. towncrier release notes start

`0.2.1 <https://github.com/ansys/pystk/releases/tag/v0.2.1>`_ - December 03, 2025
=================================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Hooks for YAML and pyproject.toml files
          - `#865 <https://github.com/ansys/pystk/pull/865>`_

        * - Switch the repo to STK 13.0.1
          - `#900 <https://github.com/ansys/pystk/pull/900>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump pandas from 2.3.2 to 2.3.3
          - `#857 <https://github.com/ansys/pystk/pull/857>`_

        * - Bump ansys-sphinx-theme from 1.6.1 to 1.6.3 in the doc group
          - `#859 <https://github.com/ansys/pystk/pull/859>`_

        * - Bump plotly from 6.3.0 to 6.3.1
          - `#863 <https://github.com/ansys/pystk/pull/863>`_

        * - Bump matplotlib from 3.10.6 to 3.10.7
          - `#868 <https://github.com/ansys/pystk/pull/868>`_

        * - Update pre-commit hooks and use hashed versions
          - `#871 <https://github.com/ansys/pystk/pull/871>`_

        * - Bump jupytext from 1.17.3 to 1.18.1 in the doc group
          - `#875 <https://github.com/ansys/pystk/pull/875>`_

        * - Bump typer from 0.19.2 to 0.20.0
          - `#876 <https://github.com/ansys/pystk/pull/876>`_

        * - Bump jupyterlab from 4.4.9 to 4.4.10 in the doc group
          - `#878 <https://github.com/ansys/pystk/pull/878>`_

        * - Bump the actions group across 1 directory with 3 updates
          - `#884 <https://github.com/ansys/pystk/pull/884>`_

        * - Bump vale from 3.12.0.2 to 3.13.0.0
          - `#885 <https://github.com/ansys/pystk/pull/885>`_

        * - Bump libcst from 1.8.5 to 1.8.6
          - `#888 <https://github.com/ansys/pystk/pull/888>`_

        * - Bump plotly from 6.3.1 to 6.4.0
          - `#889 <https://github.com/ansys/pystk/pull/889>`_

        * - Bump safety from 3.6.2 to 3.7.0
          - `#890 <https://github.com/ansys/pystk/pull/890>`_

        * - Bump the tests group across 1 directory with 2 updates
          - `#892 <https://github.com/ansys/pystk/pull/892>`_

        * - Bump plotly from 6.4.0 to 6.5.0
          - `#894 <https://github.com/ansys/pystk/pull/894>`_

        * - Bump the doc group across 1 directory with 4 updates
          - `#897 <https://github.com/ansys/pystk/pull/897>`_

        * - Bump bandit[toml] from 1.8.6 to 1.9.2
          - `#898 <https://github.com/ansys/pystk/pull/898>`_

        * - Bump the actions group across 1 directory with 2 updates
          - `#899 <https://github.com/ansys/pystk/pull/899>`_

        * - Build: bump ansys/actions from 10.1.5 to 10.2.0 in the actions group
          - `#902 <https://github.com/ansys/pystk/pull/902>`_


  .. tab-item:: Documentation

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Remove PyPI installation tab for development versions
          - `#870 <https://github.com/ansys/pystk/pull/870>`_

        * - Add instructions on how to create account
          - `#880 <https://github.com/ansys/pystk/pull/880>`_

        * - Disable the Show Source link in the sidebar
          - `#886 <https://github.com/ansys/pystk/pull/886>`_

        * - Only use wheelhouses for all dependencies
          - `#887 <https://github.com/ansys/pystk/pull/887>`_


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Close widget before STK shutdown
          - `#864 <https://github.com/ansys/pystk/pull/864>`_

        * - Fix doc build
          - `#874 <https://github.com/ansys/pystk/pull/874>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Label strategy for changelog fragments
          - `#872 <https://github.com/ansys/pystk/pull/872>`_

        * - Ci(release): use stable images
          - `#903 <https://github.com/ansys/pystk/pull/903>`_


  .. tab-item:: Test

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update tests to use local data
          - `#882 <https://github.com/ansys/pystk/pull/882>`_


`0.2.0 <https://github.com/ansys/pystk/releases/tag/v0.2.0>`_ - October 09, 2025
================================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Switch the repo to STK 13.0.0
          - `#837 <https://github.com/ansys/pystk/pull/837>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump jupytext from 1.17.2 to 1.17.3 in the doc group
          - `#819 <https://github.com/ansys/pystk/pull/819>`_

        * - Bump matplotlib from 3.10.5 to 3.10.6
          - `#822 <https://github.com/ansys/pystk/pull/822>`_

        * - Bump typer from 0.16.1 to 0.17.3
          - `#823 <https://github.com/ansys/pystk/pull/823>`_

        * - Bump jupyterlab from 4.4.6 to 4.4.7 in the doc group
          - `#825 <https://github.com/ansys/pystk/pull/825>`_

        * - Bump pytest from 8.4.1 to 8.4.2 in the tests group
          - `#826 <https://github.com/ansys/pystk/pull/826>`_

        * - Bump ansys-sphinx-theme from 1.6.0 to 1.6.1 in the doc group
          - `#827 <https://github.com/ansys/pystk/pull/827>`_

        * - Bump the actions group across 1 directory with 4 updates
          - `#829 <https://github.com/ansys/pystk/pull/829>`_

        * - Bump pytest-cov from 6.2.1 to 6.3.0 in the tests group
          - `#831 <https://github.com/ansys/pystk/pull/831>`_

        * - Bump typer from 0.17.3 to 0.17.4
          - `#832 <https://github.com/ansys/pystk/pull/832>`_

        * - Bump vale from 3.12.0.1 to 3.12.0.2
          - `#833 <https://github.com/ansys/pystk/pull/833>`_

        * - Bump pytest-cov from 6.3.0 to 7.0.0 in the tests group
          - `#834 <https://github.com/ansys/pystk/pull/834>`_

        * - Bump libcst from 1.8.2 to 1.8.4
          - `#835 <https://github.com/ansys/pystk/pull/835>`_

        * - Bump ansys/actions from 10.0.20 to 10.1.1 in the actions group
          - `#836 <https://github.com/ansys/pystk/pull/836>`_

        * - Bump ansys/actions from 10.1.1 to 10.1.2 in the actions group
          - `#838 <https://github.com/ansys/pystk/pull/838>`_

        * - Bump ansys/actions from 10.1.2 to 10.1.3 in the actions group
          - `#842 <https://github.com/ansys/pystk/pull/842>`_

        * - Bump typer from 0.17.4 to 0.19.1
          - `#843 <https://github.com/ansys/pystk/pull/843>`_

        * - Bump typer from 0.19.1 to 0.19.2
          - `#845 <https://github.com/ansys/pystk/pull/845>`_

        * - Bump safety from 3.6.1 to 3.6.2
          - `#846 <https://github.com/ansys/pystk/pull/846>`_

        * - Bump ansys/actions from 10.1.3 to 10.1.4 in the actions group
          - `#847 <https://github.com/ansys/pystk/pull/847>`_

        * - Bump jupyterlab from 4.4.7 to 4.4.8 in the doc group
          - `#849 <https://github.com/ansys/pystk/pull/849>`_

        * - Bump libcst from 1.8.4 to 1.8.5
          - `#850 <https://github.com/ansys/pystk/pull/850>`_

        * - Bump jupyterlab from 4.4.8 to 4.4.9 in the doc group
          - `#853 <https://github.com/ansys/pystk/pull/853>`_


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Fix building the STK docker images with latest docker which uses Bake
          - `#821 <https://github.com/ansys/pystk/pull/821>`_

        * - Pedantic warnings
          - `#830 <https://github.com/ansys/pystk/pull/830>`_

        * - Use Python 3.10 for testing
          - `#840 <https://github.com/ansys/pystk/pull/840>`_

        * - Empty environment variable
          - `#844 <https://github.com/ansys/pystk/pull/844>`_

        * - Use runner name when starting a new container
          - `#848 <https://github.com/ansys/pystk/pull/848>`_

        * - Adjust container name in nightly build
          - `#851 <https://github.com/ansys/pystk/pull/851>`_

        * - Use raw link to display logo
          - `#852 <https://github.com/ansys/pystk/pull/852>`_

        * - Image name in tests job
          - `#855 <https://github.com/ansys/pystk/pull/855>`_

        * - Ignore python, jupyter, and PDF artifacts
          - `#860 <https://github.com/ansys/pystk/pull/860>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.1.2
          - `#816 <https://github.com/ansys/pystk/pull/816>`_

        * - Setup multi-runners strategy
          - `#841 <https://github.com/ansys/pystk/pull/841>`_


`0.1.2 <https://github.com/ansys/pystk/releases/tag/v0.1.2>`_ - September 05, 2025
==================================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - More graph wrappers
          - `#794 <https://github.com/ansys/pystk/pull/794>`_


  .. tab-item:: Dependencies

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Bump matplotlib from 3.10.3 to 3.10.5
          - `#788 <https://github.com/ansys/pystk/pull/788>`_

        * - Bump build from 1.2.2.post1 to 1.3.0
          - `#790 <https://github.com/ansys/pystk/pull/790>`_

        * - Bump actions/download-artifact from 4 to 5 in the actions group
          - `#793 <https://github.com/ansys/pystk/pull/793>`_

        * - Bump actions/checkout from 4 to 5 in the actions group
          - `#795 <https://github.com/ansys/pystk/pull/795>`_

        * - Bump plotly from 6.2.0 to 6.3.0
          - `#797 <https://github.com/ansys/pystk/pull/797>`_

        * - Bump the doc group across 1 directory with 2 updates
          - `#800 <https://github.com/ansys/pystk/pull/800>`_

        * - Bump pandas from 2.3.1 to 2.3.2
          - `#804 <https://github.com/ansys/pystk/pull/804>`_

        * - Bump jupyter-server from 2.16.0 to 2.17.0 in the doc group
          - `#805 <https://github.com/ansys/pystk/pull/805>`_

        * - Bump vale from 3.12.0.0 to 3.12.0.1
          - `#806 <https://github.com/ansys/pystk/pull/806>`_

        * - Bump ansys/actions from 10.0.15 to 10.0.16 in the actions group
          - `#810 <https://github.com/ansys/pystk/pull/810>`_


  .. tab-item:: Documentation

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Alphabetize methods, properties in doc
          - `#786 <https://github.com/ansys/pystk/pull/786>`_

        * - Tweak migration guide
          - `#791 <https://github.com/ansys/pystk/pull/791>`_

        * - Add compatibility table
          - `#801 <https://github.com/ansys/pystk/pull/801>`_

        * - Fix ``datatable`` background style for dark theme
          - `#815 <https://github.com/ansys/pystk/pull/815>`_


  .. tab-item:: Fixed

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update codecov badge
          - `#789 <https://github.com/ansys/pystk/pull/789>`_

        * - Include wheelhouse artifacts in releases
          - `#792 <https://github.com/ansys/pystk/pull/792>`_

        * - Restore linkcheck for changelog
          - `#796 <https://github.com/ansys/pystk/pull/796>`_

        * - Pin typer package to prevent AttributeError
          - `#807 <https://github.com/ansys/pystk/pull/807>`_

        * - Non-breaking space and invalid variable names
          - `#811 <https://github.com/ansys/pystk/pull/811>`_

        * - Invalid variable names
          - `#814 <https://github.com/ansys/pystk/pull/814>`_


  .. tab-item:: Maintenance

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - Update CHANGELOG for v0.1.1
          - `#785 <https://github.com/ansys/pystk/pull/785>`_

        * - Enable codecov
          - `#787 <https://github.com/ansys/pystk/pull/787>`_

        * - General improvements
          - `#802 <https://github.com/ansys/pystk/pull/802>`_

        * - Update classifiers to include Python 3.10
          - `#808 <https://github.com/ansys/pystk/pull/808>`_


`0.1.1 <https://github.com/ansys/pystk/releases/tag/v0.1.1>`_ - August 06, 2025
===============================================================================

.. tab-set::


  .. tab-item:: Added

    .. list-table::
        :header-rows: 0
        :widths: auto

        * - First release of PySTK
          - `#784 <https://github.com/ansys/pystk/pull/784>`_


.. vale on
