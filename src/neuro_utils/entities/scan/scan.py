import json
from pathlib import Path
from typing import Union


class Scan:
    def __init__(
        self, path_to_nifti_file: Union[str, Path], auto_parse: bool = True
    ):
        """
        A class to represent an MRI scan.

        Parameters
        ----------
        path_to_nifti_file : str
            Path to the NIfTI file of the scan.
        """
        self.nifti_file = Path(path_to_nifti_file)
        if auto_parse:
            self.properties = self.get_properties_from_json()
        else:
            self.properties = {}

    def get_properties_from_json(
        self, path_to_json_file: Union[str, Path] = None
    ) -> dict:
        """
        Get the properties of the scan from the JSON file.

        Parameters
        ----------
        path_to_json_file : Union[str, Path], optional
            Path to the JSON file, by default None

        Returns
        -------
        dict
            The properties of the scan.
        """
        json_file = path_to_json_file or self.json_file
        with open(str(json_file), "r") as f:
            properties = json.load(f)
        return properties

    @property
    def is_gunzipped(self) -> bool:
        """
        Check if the NIfTI file is gunzipped.

        Returns
        -------
        bool
            True if the NIfTI file is gunzipped, False otherwise.
        """
        return "nii.gz" in self.nifti_file.name

    @property
    def json_file(self):
        """
        Get the path to the JSON file.

        Returns
        -------
        Path
            The path to the JSON file.
        """
        return self.nifti_file.parent / self.nifti_file.name.replace(
            self.extension, "json"
        )

    @property
    def extension(self):
        """
        Get the extension of the NIfTI file.

        Returns
        -------
        str
            The extension of the NIfTI file.
        """
        return "nii.gz" if self.is_gunzipped else "nii"
