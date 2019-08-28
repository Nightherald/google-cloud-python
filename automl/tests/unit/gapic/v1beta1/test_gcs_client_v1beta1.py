# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pandas
import pytest
import re

from google.api_core import exceptions
from google.cloud import automl_v1beta1


class TestGcsClient(object):
    def gcs_client(self, client_attrs={}):
        client_mock = mock.Mock(**client_attrs)
        return automl_v1beta1.tables.gcs_client.GcsClient(client=client_mock)

    def test_ensure_bucket_exists(self):
        mock_bucket = mock.Mock()
        gcs_client = self.gcs_client(
            {
                "get_bucket.side_effect": exceptions.NotFound("err"),
                "bucket.return_value": mock_bucket,
            }
        )
        returned_bucket_name = gcs_client.ensure_bucket_exists(
            "my-project", "us-central1"
        )
        gcs_client.client.get_bucket.assert_called_with(
            "my-project-automl-tables-staging"
        )
        gcs_client.client.bucket.assert_called_with("my-project-automl-tables-staging")
        mock_bucket.create.assert_called_with(
            project="my-project", location="us-central1"
        )

        assert returned_bucket_name == "my-project-automl-tables-staging"

    def test_ensure_bucket_exists_bucket_already_exists(self):
        gcs_client = self.gcs_client()
        returned_bucket_name = gcs_client.ensure_bucket_exists(
            "my-project", "us-central1"
        )
        gcs_client.client.get_bucket.assert_called_with(
            "my-project-automl-tables-staging"
        )
        gcs_client.client.bucket.assert_not_called()
        assert returned_bucket_name == "my-project-automl-tables-staging"

    def test_upload_pandas_dataframe(self):
        mock_blob = mock.Mock()
        mock_bucket = mock.Mock(**{"blob.return_value": mock_blob})
        gcs_client = self.gcs_client({"get_bucket.return_value": mock_bucket})
        dataframe = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})

        gcs_uri = gcs_client.upload_pandas_dataframe(
            "my-bucket", dataframe, "my-file.csv"
        )

        gcs_client.client.get_bucket.assert_called_with("my-bucket")
        mock_bucket.blob.assert_called_with("my-file.csv")
        mock_blob.upload_from_string.assert_called_with(",col1,col2\n0,1,3\n1,2,4\n")
        assert gcs_uri == "gs://my-bucket/my-file.csv"

    def test_upload_pandas_dataframe_no_csv_name(self):
        mock_blob = mock.Mock()
        mock_bucket = mock.Mock(**{"blob.return_value": mock_blob})
        gcs_client = self.gcs_client({"get_bucket.return_value": mock_bucket})
        dataframe = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})

        gcs_uri = gcs_client.upload_pandas_dataframe("my-bucket", dataframe)
        generated_csv_name = gcs_uri.split("/")[-1]

        gcs_client.client.get_bucket.assert_called_with("my-bucket")
        mock_bucket.blob.assert_called_with(generated_csv_name)
        mock_blob.upload_from_string.assert_called_with(",col1,col2\n0,1,3\n1,2,4\n")
        assert re.match("gs://my-bucket/automl-tables-dataframe-([0-9]*).csv", gcs_uri)

    def test_upload_pandas_dataframe_not_type_dataframe(self):
        gcs_client = self.gcs_client()
        with pytest.raises(ValueError):
            gcs_client.upload_pandas_dataframe("my-bucket", "my-dataframe")
        gcs_client.client.upload_pandas_dataframe.assert_not_called()