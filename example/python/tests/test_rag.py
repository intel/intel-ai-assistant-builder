import unittest
import os
import json
from unittest.mock import MagicMock, patch
from helpers.rag import is_valid_file_path, upload_file_to_knowledge_base, remove_uploaded_file, list_uploaded_files

class TestRagHelpers(unittest.TestCase):

    @patch('helpers.rag.is_valid_file_path')
    @patch('helpers.rag.os.path.abspath')
    @patch('helpers.rag.sb.AddFilesRequest')
    @patch('helpers.rag.tqdm')
    def test_upload_file_to_knowledge_base(self, mock_tqdm, MockAddFilesRequest, mock_abspath, mock_is_valid_file_path):
        stub = MagicMock()
        mock_is_valid_file_path.side_effect = [True, False]
        mock_abspath.side_effect = lambda x: f"/abs/{x}"
        file_paths = ["file1", "file2"]
        upload_file_to_knowledge_base(stub, file_paths)
        mock_abspath.assert_any_call("file1")
        mock_abspath.assert_any_call("file2")
        mock_is_valid_file_path.assert_any_call("/abs/file1")
        mock_is_valid_file_path.assert_any_call("/abs/file2")
        MockAddFilesRequest.assert_called_once_with(filesToUpload=json.dumps(["/abs/file1"]))
        stub.AddFiles.assert_called_once_with(MockAddFilesRequest())

    @patch('helpers.rag.is_valid_file_path')
    @patch('helpers.rag.os.path.abspath')
    @patch('helpers.rag.sb.RemoveFilesRequest')
    def test_remove_uploaded_file(self, MockRemoveFilesRequest, mock_abspath, mock_is_valid_file_path):
        stub = MagicMock()
        mock_is_valid_file_path.side_effect = [True, False]
        mock_abspath.side_effect = lambda x: f"/abs/{x}"
        file_paths = ["file1", "file2"]
        remove_uploaded_file(stub, file_paths)
        mock_abspath.assert_any_call("file1")
        mock_abspath.assert_any_call("file2")
        mock_is_valid_file_path.assert_any_call("/abs/file1")
        mock_is_valid_file_path.assert_any_call("/abs/file2")
        MockRemoveFilesRequest.assert_called_once_with(filesToRemove=json.dumps(["/abs/file1"]))
        stub.RemoveFiles.assert_called_once_with(MockRemoveFilesRequest())

    @patch('helpers.rag.sb.GetFileListRequest')
    def test_list_uploaded_files(self, MockGetFileListRequest):
        stub = MagicMock()
        stub.GetFileList.return_value.fileList = json.dumps(["file1", "file2"])
        list_uploaded_files(stub)
        MockGetFileListRequest.assert_called_once_with(fileType="")
        stub.GetFileList.assert_called_once_with(MockGetFileListRequest())

if __name__ == '__main__':
    unittest.main()