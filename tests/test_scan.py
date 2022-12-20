from neuro_utils.entities.scan import Scan


def test_scan():
    scan = Scan(
        path_to_nifti_file="tests/data/scans/sub-2321_ses-202202131331_ce-corrected_T1w.nii.gz"  # noqa: E501
    )
    assert scan.is_gunzipped
