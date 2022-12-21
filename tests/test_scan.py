from pathlib import Path
from unittest import TestCase

from neuro_utils.entities.scan import Scan


class TestScan(TestCase):
    NIFTI_PATH = Path(
        "tests/data/scans/sub-2321_ses-202202131331_ce-corrected_T1w.nii.gz"
    )  # noqa: E501

    def setUp(self) -> None:
        return super().setUp()

    def test_scan_exists(self):
        """
        Test that the scan exists.
        """
        scan = Scan(path_to_nifti_file=self.NIFTI_PATH)
        assert scan.nifti_path.exists()

    def test_scan_is_gunzipped(self):
        """
        Test that the scan is gunzipped.
        """
        scan = Scan(path_to_nifti_file=self.NIFTI_PATH)
        assert scan.is_gunzipped

    def test_scan_properties(self):
        """
        Test that the scan properties are retrieved.
        """
        scan = Scan(path_to_nifti_file=self.NIFTI_PATH)
        assert scan.properties

    def test_scan_properties_from_json(self):
        """
        Test that the scan properties are retrieved from the JSON file.
        """
        scan = Scan(path_to_nifti_file=self.NIFTI_PATH)
        assert len(scan.properties) > 0

    def test_scan_extension(self):
        """
        Test that the scan extention is retrieved.
        """
        scan = Scan(path_to_nifti_file=self.NIFTI_PATH)
        assert scan.extension == "nii.gz"

    def test_properties_without_auto_parse(self):
        """
        Test that the scan properties are retrieved without auto scan.
        """
        scan = Scan(path_to_nifti_file=self.NIFTI_PATH, auto_parse=False)
        assert len(scan.properties) == 0

    def test_missing_json_raises_error(self):
        """
        Test that the scan properties are retrieved without auto scan.
        """
        scan = Scan(path_to_nifti_file=self.NIFTI_PATH, auto_parse=False)
        with self.assertRaises(FileNotFoundError):
            scan.get_properties_from_json(path_to_json_file="missing.json")

    def test_missing_json_returns_empty_dict(self):
        """
        Test that the scan properties are retrieved without auto scan.
        """
        scan = Scan(path_to_nifti_file=self.NIFTI_PATH, auto_parse=False)
        assert (
            len(
                scan.get_properties_from_json(
                    path_to_json_file="missing.json", raise_error=False
                )
            )
            == 0
        )
