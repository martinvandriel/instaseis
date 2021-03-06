#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic integration tests for the AxiSEM database Python interface.

:copyright:
    Martin van Driel (Martin@vanDriel.de), 2014
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2014
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from __future__ import absolute_import

import inspect
import numpy as np
import os
import pytest
import shutil

from instaseis import InstaSeisDB
from instaseis import Source, Receiver, ForceSource

from .testdata import BWD_TEST_DATA, FWD_TEST_DATA
from .testdata import BWD_STRAIN_ONLY_TEST_DATA, BWD_FORCE_TEST_DATA


# Most generic way to get the data folder path.
DATA = os.path.join(os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))), "data")


def test_fwd_vs_bwd():
    """
    Test fwd against bwd mode
    """
    instaseis_fwd = InstaSeisDB(os.path.join(DATA, "100s_db_fwd"))

    instaseis_bwd = InstaSeisDB(os.path.join(DATA, "100s_db_bwd_displ_only"))

    source_fwd = Source(latitude=4., longitude=3.0, depth_in_m=None,
                        m_rr=4.71e+17, m_tt=3.81e+17, m_pp=-4.74e+17,
                        m_rt=3.99e+17, m_rp=-8.05e+17, m_tp=-1.23e+17)
    source_bwd = Source(latitude=4., longitude=3.0, depth_in_m=0,
                        m_rr=4.71e+17, m_tt=3.81e+17, m_pp=-4.74e+17,
                        m_rt=3.99e+17, m_rp=-8.05e+17, m_tp=-1.23e+17)

    receiver_fwd = Receiver(latitude=10., longitude=20., depth_in_m=0)
    receiver_bwd = Receiver(latitude=10., longitude=20., depth_in_m=None)

    st_fwd = instaseis_fwd.get_seismograms(
        source=source_fwd, receiver=receiver_fwd,
        components=('Z', 'N', 'E', 'R', 'T'))
    st_bwd = instaseis_bwd.get_seismograms(
        source=source_bwd, receiver=receiver_bwd,
        components=('Z', 'N', 'E', 'R', 'T'))

    st_bwd.filter('lowpass', freq=0.002)
    st_fwd.filter('lowpass', freq=0.002)

    np.testing.assert_allclose(st_fwd.select(component="Z")[0].data,
                               st_bwd.select(component="Z")[0].data,
                               rtol=1E-3, atol=1E-10)

    np.testing.assert_allclose(st_fwd.select(component="N")[0].data,
                               st_bwd.select(component="N")[0].data,
                               rtol=1E-3, atol=1E-10)

    np.testing.assert_allclose(st_fwd.select(component="E")[0].data,
                               st_bwd.select(component="E")[0].data,
                               rtol=1E-3, atol=1E-10)

    np.testing.assert_allclose(st_fwd.select(component="R")[0].data,
                               st_bwd.select(component="R")[0].data,
                               rtol=1E-3, atol=1E-10)

    np.testing.assert_allclose(st_fwd.select(component="T")[0].data,
                               st_bwd.select(component="T")[0].data,
                               rtol=1E-3, atol=1E-10)


def test_fwd_vs_bwd_axial():
    """
    Test fwd against bwd mode, axial element. Differences are a bit larger then
    in non axial case, presumably because the close source, which is not
    exactly a point source in the SEM representation.
    """
    instaseis_fwd = InstaSeisDB(os.path.join(DATA, "100s_db_fwd_deep"))

    instaseis_bwd = InstaSeisDB(os.path.join(DATA, "100s_db_bwd_displ_only"))

    source_fwd = Source(latitude=0., longitude=0., depth_in_m=None,
                        m_rr=4.71e+17, m_tt=3.81e+17, m_pp=-4.74e+17,
                        m_rt=3.99e+17, m_rp=-8.05e+17, m_tp=-1.23e+17)
    source_bwd = Source(latitude=0., longitude=0., depth_in_m=310000,
                        m_rr=4.71e+17, m_tt=3.81e+17, m_pp=-4.74e+17,
                        m_rt=3.99e+17, m_rp=-8.05e+17, m_tp=-1.23e+17)

    receiver_fwd = Receiver(latitude=0., longitude=0.1, depth_in_m=0)
    receiver_bwd = Receiver(latitude=0., longitude=0.1, depth_in_m=None)

    st_fwd = instaseis_fwd.get_seismograms(
        source=source_fwd, receiver=receiver_fwd,
        components=('Z', 'N', 'E', 'R', 'T'))
    st_bwd = instaseis_bwd.get_seismograms(
        source=source_bwd, receiver=receiver_bwd,
        components=('Z', 'N', 'E', 'R', 'T'))

    st_bwd.filter('lowpass', freq=0.01)
    st_fwd.filter('lowpass', freq=0.01)
    st_bwd.filter('lowpass', freq=0.01)
    st_fwd.filter('lowpass', freq=0.01)
    st_bwd.differentiate()
    st_fwd.differentiate()

    np.testing.assert_allclose(st_fwd.select(component="Z")[0].data,
                               st_bwd.select(component="Z")[0].data,
                               rtol=1E-2, atol=5E-9)

    np.testing.assert_allclose(st_fwd.select(component="N")[0].data,
                               st_bwd.select(component="N")[0].data,
                               rtol=1E-2, atol=5E-9)

    np.testing.assert_allclose(st_fwd.select(component="E")[0].data,
                               st_bwd.select(component="E")[0].data,
                               rtol=1E-2, atol=6E-9)

    np.testing.assert_allclose(st_fwd.select(component="R")[0].data,
                               st_bwd.select(component="R")[0].data,
                               rtol=1E-2, atol=6E-9)

    np.testing.assert_allclose(st_fwd.select(component="T")[0].data,
                               st_bwd.select(component="T")[0].data,
                               rtol=1E-2, atol=5E-9)


def test_incremental_bwd():
    """
    incremental tests of bwd mode with displ_only db
    """
    instaseis_bwd = InstaSeisDB(os.path.join(DATA, "100s_db_bwd_displ_only"))

    receiver = Receiver(latitude=42.6390, longitude=74.4940)
    source = Source(
        latitude=89.91, longitude=0.0, depth_in_m=12000,
        m_rr=4.710000e+24 / 1E7,
        m_tt=3.810000e+22 / 1E7,
        m_pp=-4.740000e+24 / 1E7,
        m_rt=3.990000e+23 / 1E7,
        m_rp=-8.050000e+23 / 1E7,
        m_tp=-1.230000e+24 / 1E7)

    st_bwd = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver, components=('Z', 'N', 'E', 'R', 'T'))

    np.testing.assert_allclose(st_bwd.select(component='Z')[0].data,
                               BWD_TEST_DATA["Z"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='N')[0].data,
                               BWD_TEST_DATA["N"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='E')[0].data,
                               BWD_TEST_DATA["E"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='R')[0].data,
                               BWD_TEST_DATA["R"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='T')[0].data,
                               BWD_TEST_DATA["T"], rtol=1E-7, atol=1E-12)
    assert instaseis_bwd.meshes.px.strain_buffer.efficiency == 0.0
    assert instaseis_bwd.meshes.pz.strain_buffer.efficiency == 0.0

    # read on init
    instaseis_bwd = InstaSeisDB(os.path.join(DATA, "100s_db_bwd_displ_only"),
                                read_on_demand=False)

    st_bwd = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver, components=('Z', 'N', 'E', 'R', 'T'))

    np.testing.assert_allclose(st_bwd.select(component='Z')[0].data,
                               BWD_TEST_DATA["Z"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='N')[0].data,
                               BWD_TEST_DATA["N"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='E')[0].data,
                               BWD_TEST_DATA["E"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='R')[0].data,
                               BWD_TEST_DATA["R"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='T')[0].data,
                               BWD_TEST_DATA["T"], rtol=1E-7, atol=1E-12)
    assert instaseis_bwd.meshes.px.strain_buffer.efficiency == 0.0
    assert instaseis_bwd.meshes.pz.strain_buffer.efficiency == 0.0

    # read the same again to test buffer
    st_bwd = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver, components=('Z', 'N', 'E', 'R', 'T'))
    np.testing.assert_allclose(st_bwd.select(component='Z')[0].data,
                               BWD_TEST_DATA["Z"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='N')[0].data,
                               BWD_TEST_DATA["N"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='E')[0].data,
                               BWD_TEST_DATA["E"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='R')[0].data,
                               BWD_TEST_DATA["R"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='T')[0].data,
                               BWD_TEST_DATA["T"], rtol=1E-7, atol=1E-12)
    assert instaseis_bwd.meshes.px.strain_buffer.efficiency == 1.0 / 2.0
    assert instaseis_bwd.meshes.pz.strain_buffer.efficiency == 1.0 / 2.0

    # test resampling
    dt = instaseis_bwd.dt
    st_bwd = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver, components=('Z'), dt=dt)
    np.testing.assert_allclose(st_bwd.select(component='Z')[0].data,
                               BWD_TEST_DATA["Z"], rtol=1E-7, atol=1E-12)


def test_vertical_only_db(tmpdir):
    """
    Everything should work even if only the vertical component is present.
    """
    # Copy only the vertical component data.
    tmpdir = str(tmpdir)
    path = os.path.join(tmpdir, "PZ", "Data", "ordered_output.nc4")
    os.makedirs(os.path.dirname(path))
    shutil.copy(
        os.path.join(DATA, "100s_db_bwd_displ_only", "PZ", "Data",
                     "ordered_output.nc4"), path)

    receiver = Receiver(latitude=42.6390, longitude=74.4940)
    source = Source(
        latitude=89.91, longitude=0.0, depth_in_m=12000,
        m_rr=4.710000e+24 / 1E7,
        m_tt=3.810000e+22 / 1E7,
        m_pp=-4.740000e+24 / 1E7,
        m_rt=3.990000e+23 / 1E7,
        m_rp=-8.050000e+23 / 1E7,
        m_tp=-1.230000e+24 / 1E7)

    # vertical only DB
    instaseis_bwd = InstaSeisDB(tmpdir)

    st_bwd = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver, components=('Z'))

    np.testing.assert_allclose(st_bwd.select(component='Z')[0].data,
                               BWD_TEST_DATA["Z"], rtol=1E-7, atol=1E-12)


def test_horizontal_only_db(tmpdir):
    """
    Everything should work even if only the horizontal component is present.
    """
    # Copy only the horizontal component data.
    tmpdir = str(tmpdir)
    path = os.path.join(tmpdir, "PX", "Data", "ordered_output.nc4")
    os.makedirs(os.path.dirname(path))
    shutil.copy(
        os.path.join(DATA, "100s_db_bwd_displ_only", "PX", "Data",
                     "ordered_output.nc4"),
        path)

    receiver = Receiver(latitude=42.6390, longitude=74.4940)
    source = Source(
        latitude=89.91, longitude=0.0, depth_in_m=12000,
        m_rr=4.710000e+24 / 1E7,
        m_tt=3.810000e+22 / 1E7,
        m_pp=-4.740000e+24 / 1E7,
        m_rt=3.990000e+23 / 1E7,
        m_rp=-8.050000e+23 / 1E7,
        m_tp=-1.230000e+24 / 1E7)

    # vertical only DB
    instaseis_bwd = InstaSeisDB(tmpdir)

    st_bwd = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver, components=('N'))

    np.testing.assert_allclose(st_bwd.select(component='N')[0].data,
                               BWD_TEST_DATA["N"], rtol=1E-7, atol=1E-12)


def test_requesting_wrong_component_horizontal(tmpdir):
    # Copy only the horizontal component data.
    tmpdir = str(tmpdir)
    path = os.path.join(tmpdir, "PX", "Data", "ordered_output.nc4")
    os.makedirs(os.path.dirname(path))
    shutil.copy(
        os.path.join(DATA, "100s_db_bwd_displ_only", "PX", "Data",
                     "ordered_output.nc4"),
        path)

    receiver = Receiver(latitude=42.6390, longitude=74.4940)
    source = Source(
        latitude=89.91, longitude=0.0, depth_in_m=12000,
        m_rr=4.710000e+24 / 1E7,
        m_tt=3.810000e+22 / 1E7,
        m_pp=-4.740000e+24 / 1E7,
        m_rt=3.990000e+23 / 1E7,
        m_rp=-8.050000e+23 / 1E7,
        m_tp=-1.230000e+24 / 1E7)

    # vertical only DB
    instaseis_bwd = InstaSeisDB(tmpdir)

    with pytest.raises(ValueError):
        instaseis_bwd.get_seismograms(
            source=source, receiver=receiver, components=('Z'))


def test_requesting_wrong_component_vertical(tmpdir):
    # Copy only the horizontal component data.
    tmpdir = str(tmpdir)
    path = os.path.join(tmpdir, "PZ", "Data", "ordered_output.nc4")
    os.makedirs(os.path.dirname(path))
    shutil.copy(
        os.path.join(DATA, "100s_db_bwd_displ_only", "PZ", "Data",
                     "ordered_output.nc4"),
        path)

    receiver = Receiver(latitude=42.6390, longitude=74.4940)
    source = Source(
        latitude=89.91, longitude=0.0, depth_in_m=12000,
        m_rr=4.710000e+24 / 1E7,
        m_tt=3.810000e+22 / 1E7,
        m_pp=-4.740000e+24 / 1E7,
        m_rt=3.990000e+23 / 1E7,
        m_rp=-8.050000e+23 / 1E7,
        m_tp=-1.230000e+24 / 1E7)

    # vertical only DB
    instaseis_bwd = InstaSeisDB(tmpdir)

    with pytest.raises(ValueError):
        instaseis_bwd.get_seismograms(
            source=source, receiver=receiver, components=('E'))
    with pytest.raises(ValueError):
        instaseis_bwd.get_seismograms(
            source=source, receiver=receiver, components=('N'))
    with pytest.raises(ValueError):
        instaseis_bwd.get_seismograms(
            source=source, receiver=receiver, components=('T'))
    with pytest.raises(ValueError):
        instaseis_bwd.get_seismograms(
            source=source, receiver=receiver, components=('R'))


def test_incremental_fwd():
    """
    incremental tests of fwd mode
    """
    instaseis_fwd = InstaSeisDB(os.path.join(DATA, "100s_db_fwd"))

    receiver = Receiver(latitude=42.6390, longitude=74.4940)
    source = Source(
        latitude=89.91, longitude=0.0, depth_in_m=None,
        m_rr=4.710000e+24 / 1E7,
        m_tt=3.810000e+22 / 1E7,
        m_pp=-4.740000e+24 / 1E7,
        m_rt=3.990000e+23 / 1E7,
        m_rp=-8.050000e+23 / 1E7,
        m_tp=-1.230000e+24 / 1E7)

    st_fwd = instaseis_fwd.get_seismograms(
        source=source, receiver=receiver, components=('Z', 'N', 'E', 'R', 'T'))

    np.testing.assert_allclose(st_fwd.select(component='Z')[0].data,
                               FWD_TEST_DATA["Z"], rtol=1E-7, atol=1E-16)
    np.testing.assert_allclose(st_fwd.select(component='N')[0].data,
                               FWD_TEST_DATA["N"], rtol=1E-7, atol=1E-16)
    np.testing.assert_allclose(st_fwd.select(component='E')[0].data,
                               FWD_TEST_DATA["E"], rtol=1E-7, atol=1E-16)
    np.testing.assert_allclose(st_fwd.select(component='R')[0].data,
                               FWD_TEST_DATA["R"], rtol=1E-7, atol=1E-16)
    np.testing.assert_allclose(st_fwd.select(component='T')[0].data,
                               FWD_TEST_DATA["T"], rtol=1E-7, atol=1E-16)
    assert instaseis_fwd.meshes.m1.displ_buffer.efficiency == 0.0
    assert instaseis_fwd.meshes.m2.displ_buffer.efficiency == 0.0
    assert instaseis_fwd.meshes.m3.displ_buffer.efficiency == 0.0
    assert instaseis_fwd.meshes.m4.displ_buffer.efficiency == 0.0

    # read the same again to test buffer
    st_fwd = instaseis_fwd.get_seismograms(
        source=source, receiver=receiver, components=('Z', 'N', 'E', 'R', 'T'))
    np.testing.assert_allclose(st_fwd.select(component='Z')[0].data,
                               FWD_TEST_DATA["Z"], rtol=1E-7, atol=1E-16)
    np.testing.assert_allclose(st_fwd.select(component='N')[0].data,
                               FWD_TEST_DATA["N"], rtol=1E-7, atol=1E-16)
    np.testing.assert_allclose(st_fwd.select(component='E')[0].data,
                               FWD_TEST_DATA["E"], rtol=1E-7, atol=1E-16)
    np.testing.assert_allclose(st_fwd.select(component='R')[0].data,
                               FWD_TEST_DATA["R"], rtol=1E-7, atol=1E-16)
    np.testing.assert_allclose(st_fwd.select(component='T')[0].data,
                               FWD_TEST_DATA["T"], rtol=1E-7, atol=1E-16)
    assert instaseis_fwd.meshes.m1.displ_buffer.efficiency == 1.0 / 2.0
    assert instaseis_fwd.meshes.m2.displ_buffer.efficiency == 1.0 / 2.0
    assert instaseis_fwd.meshes.m3.displ_buffer.efficiency == 1.0 / 2.0
    assert instaseis_fwd.meshes.m4.displ_buffer.efficiency == 1.0 / 2.0


def test_incremental_bwd_strain_only():
    """
    incremental tests of bwd mode with strain_only DB
    """
    instaseis_bwd = InstaSeisDB(os.path.join(DATA, "100s_db_bwd_strain_only"))

    receiver = Receiver(latitude=42.6390, longitude=74.4940)
    source = Source(
        latitude=89.91, longitude=0.0, depth_in_m=12000,
        m_rr=4.710000e+24 / 1E7,
        m_tt=3.810000e+22 / 1E7,
        m_pp=-4.740000e+24 / 1E7,
        m_rt=3.990000e+23 / 1E7,
        m_rp=-8.050000e+23 / 1E7,
        m_tp=-1.230000e+24 / 1E7)

    st_bwd = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver, components=('Z', 'N', 'E', 'R', 'T'))

    np.testing.assert_allclose(st_bwd.select(component='Z')[0].data,
                               BWD_STRAIN_ONLY_TEST_DATA["Z"], rtol=1E-7,
                               atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='N')[0].data,
                               BWD_STRAIN_ONLY_TEST_DATA["N"], rtol=1E-7,
                               atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='E')[0].data,
                               BWD_STRAIN_ONLY_TEST_DATA["E"], rtol=1E-7,
                               atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='R')[0].data,
                               BWD_STRAIN_ONLY_TEST_DATA["R"], rtol=1E-7,
                               atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='T')[0].data,
                               BWD_STRAIN_ONLY_TEST_DATA["T"], rtol=1E-7,
                               atol=1E-12)


def test_incremental_bwd_force_source():
    """
    incremental tests of bwd mode with source force
    """
    instaseis_bwd = InstaSeisDB(os.path.join(DATA, "100s_db_bwd_displ_only"))

    receiver = Receiver(latitude=42.6390, longitude=74.4940)
    source = ForceSource(
        latitude=89.91, longitude=0.0, depth_in_m=12000,
        f_r=1.23E10,
        f_t=2.55E10,
        f_p=1.73E10)

    st_bwd = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver, components=('Z', 'N', 'E', 'R', 'T'))

    np.testing.assert_allclose(st_bwd.select(component='Z')[0].data,
                               BWD_FORCE_TEST_DATA["Z"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='N')[0].data,
                               BWD_FORCE_TEST_DATA["N"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='E')[0].data,
                               BWD_FORCE_TEST_DATA["E"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='R')[0].data,
                               BWD_FORCE_TEST_DATA["R"], rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_bwd.select(component='T')[0].data,
                               BWD_FORCE_TEST_DATA["T"], rtol=1E-7, atol=1E-12)


def test_finite_source():
    """
    incremental tests of bwd mode with source force
    """
    from obspy.signal.filter import lowpass
    instaseis_bwd = InstaSeisDB(os.path.join(DATA, "100s_db_bwd_displ_only"))

    receiver = Receiver(latitude=42.6390, longitude=74.4940)

    source = Source(
        latitude=89.91, longitude=0.0, depth_in_m=12000,
        m_rr=4.710000e+24 / 1E7,
        m_tt=3.810000e+22 / 1E7,
        m_pp=-4.740000e+24 / 1E7,
        m_rt=3.990000e+23 / 1E7,
        m_rp=-8.050000e+23 / 1E7,
        m_tp=-1.230000e+24 / 1E7)

    dt = instaseis_bwd.dt
    sliprate = np.zeros(1000)
    sliprate[0] = 1.
    sliprate = lowpass(sliprate, 1./100., 1./dt, corners=4)

    source.set_sliprate(sliprate, dt, time_shift=0., normalize=True)

    st_fin = instaseis_bwd.get_seismograms_finite_source(
        sources=[source], receiver=receiver,
        components=('Z', 'N', 'E', 'R', 'T'), dt=0.1)
    st_ref = instaseis_bwd.get_seismograms(
        source=source, receiver=receiver,
        components=('Z', 'N', 'E', 'R', 'T'), dt=0.1, reconvolve_stf=True)

    np.testing.assert_allclose(st_fin.select(component='Z')[0].data,
                               st_ref.select(component='Z')[0].data,
                               rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_fin.select(component='N')[0].data,
                               st_ref.select(component='N')[0].data,
                               rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_fin.select(component='E')[0].data,
                               st_ref.select(component='E')[0].data,
                               rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_fin.select(component='R')[0].data,
                               st_ref.select(component='R')[0].data,
                               rtol=1E-7, atol=1E-12)
    np.testing.assert_allclose(st_fin.select(component='T')[0].data,
                               st_ref.select(component='T')[0].data,
                               rtol=1E-7, atol=1E-12)


def test_get_band_code_method():
    """
    Dummy test assuring the band code is determined correctly.
    """
    codes = {
        0.0005: "F",
        0.001: "F",
        0.0011: "C",
        0.004: "C",
        0.0041: "H",
        0.0125: "H",
        0.0126: "B",
        0.1: "B",
        0.11: "M",
        0.99: "M",
        1.0: "L",
        10.0: "L",
        33.0: "L"
    }
    for sr, letter in codes.items():
        assert InstaSeisDB._get_band_code(1.0 / sr) == letter
